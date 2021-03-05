# Prepare data for migration based upon given foundation for a given batch to migrate

import os
import time
from Load import Load
from Organization import Organization
from Members import Members
from Membership import Membership
from Trainings import Trainings
from Write import Write
from Selector import Selector
from Dates import Dates


class Migrator:

    def __init__(self):
        # Get env file paths
        self.org_path = os.getenv("ORG_PATH")
        self.data_dir = os.getenv("DATA_DIR")
        self.destination_path = os.getenv("DESTINATION_PATH")
        self.org_category = os.getenv("ORG_CATEGORY")
        self.template_path = os.getenv("TEMPLATE_PATH")

        # Get env dates
        self.membership_start_date = os.getenv("MEMBERSHIP_START_DATE")
        self.membership_end_date = os.getenv("MEMBERSHIP_END_DATE")
        self.membership_invoiceing_date = os.getenv("MEMBERSHIP_INVOICEING_DATE")
        self.training_start_date = os.getenv("TRAINING_START_DATE")
        self.training_end_date = os.getenv("TRAINING_END_DATE")
        self.training_invoiceing_date = os.getenv("TRAINING_INVOICEING_DATE")

    def Migrate(self):
        start_time = time.time()
        print('\n=====\nStarting Processing of Data to Migrate\n-----')
        
        #ID = 24568

        # Read meta data for clubs to load
        org_meta = Selector.Select_Many(self, self.org_path, self.org_category)
        # Run Load for relevant files
        data_basis = Load.Many(self, self.data_dir, org_meta)
        template = Load.Template(self, self.template_path)
        print(f'===\nBeginning to Process and Collate Migration Data from Data Base\n-----')
        # Read Org data
        template['Club info'] = Organization.Get_Data(self, org_meta, template['Club info'])

        # Extrapolate membership data and apply to relevant members
        template['Membership'], template['Membership Category'] = Membership.Get_Data(self, data_basis, template['Membership'], template['Membership Category'], org_meta)
        # Extrapolate trainings data and apply to relevat members
        template['Training fee'], template['Grens'], template['Style'], multi_gren_clubs = Trainings.Get_Data(self, data_basis, template['Training fee'], template['Grens'], template['Style'])
        # Read and format member data
        if multi_gren_clubs['Status']:
            # Handle clubs with more than one grens
            template['Member'] = Members.Get_Data(self, data_basis, template['Member'], multi_gren_clubs['Clubs'])
        else:
            template['Member'] = Members.Get_Data(self, data_basis, template['Member'])
        # Set start, end, and invoicing dates
        template['Member'] = Dates.Set_Membership_Dates(self, self.membership_start_date, self.membership_end_date, self.membership_invoiceing_date, template['Member'])
        template['Member'] = Dates.Set_Training_Dates(self, self.training_start_date, self.training_end_date, self.training_invoiceing_date, template['Member'])

        print(f'All Available Data has been Processed for the given Clubs!\n====\n')
        # Write collated data to new file
        Write.To_File(self, template, self.destination_path)

        print('Birds have migrated South. See you next time!\n=====')
        print(f'\n\nElapsed Time: {time.time() - start_time} seconds.\n')
        

Migrator().Migrate()