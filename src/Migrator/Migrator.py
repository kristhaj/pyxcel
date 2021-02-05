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

    def Migrate(self):
        print('Starting Processing of Data to Migrate\n-----')
        ID = 21238
        # Read meta data for clubs to load
        org_meta = Selector.Select(self, self.org_path, ID, self.org_category)
        # TODO:Run Load for relevant files
        org_base_data = Load.One(self, self.data_dir + org_meta[ID][1])
        # TODO:Read Org data

        # TODO:Read and format member data

        # TODO:Extrapolate membership data and apply to relevant members

        # TODO:Extrapolate trainings data and apply to relevat members

        # TODO:Write collated data to new file


        pass
        

Migrator().Migrate()