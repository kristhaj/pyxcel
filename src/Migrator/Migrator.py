# Prepare data for migration based upon given foundation for a given batch to migrate

import os
from Load import Load
from Organization import Organization
from Members import Members
from Membership import Membership
from Trainings import Trainings
from Write import Write
from Selector import Selector


class Migrator:

    def __init__(self):
        self.org_path = os.getenv("ORG_PATH")
        self.data_dir = os.getenv("DATA_DIR")
        self.destination_path = os.getenv("DESTINATION_PATH")
        self.org_category = os.getenv("ORG_CATEGORY")
        self.template_path = os.getenv("TEMPLATE_PATH")

    def Migrate(self):
        print('\n=====\nStarting Processing of Data to Migrate\n-----')
        ID = 21238
        # Read meta data for clubs to load
        org_meta = Selector.Select(self, self.org_path, ID, self.org_category)
        # Run Load for relevant files
        data_basis = Load.One(self, self.data_dir, org_meta)
        template = Load.Template(self, self.template_path)
        print(f'===\nBeginning to Process and Collate Migration Data from Data Base\n-----')
        # Read Org data
        template['Club info'] = Organization.Get_Data(self, org_meta, template['Club info'])
        # TODO:Read and format member data

        # Extrapolate membership data and TODO:apply to relevant members
        template['Membership'], template['Membership Category'] = Membership.Get_Data(self, data_basis, template['Membership'], template['Membership Category'], org_meta)
        # TODO:Extrapolate trainings data and apply to relevat members

        # TODO:Write collated data to new file


        pass
        

Migrator().Migrate()