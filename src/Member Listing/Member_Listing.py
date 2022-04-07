# Combine member data from old and new export, and format to the users needs

import os
from Load import Load
from Write import Write

class Member_Listing:

    def __init__(self):
        self.beta_data_path = os.getenv("BETA_DATA_PATH")
        self.old_data_path = os.getenv("OLD_DATA_PATH")
        self.destination_path = os.getenv("DESTINATION_PATH")


    #do the thing
    def Spond_List(self):
        old_columns = ['NIF nummer', 'Navn', 'DOB']

        beta_data = Load.Member_File(self, self.beta_data_path)
        old_data = Load.Member_File(self, self.old_data_path, old_columns)


        pass