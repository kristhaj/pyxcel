# Cross reference call list with member data to identify administrator and relevant information.
import os
from Load import Load
from Identify import Identify
from Lookup import Lookup
from Write import Write

class Adminipy:

    def __init__(self):
        self.call_path = os.getenv('CALL_PATH')
        self.member_data_path = os.getenv('MEMBER_DATA_PATH')
        self.qualifier_path = os.getenv('QUALIFIER_PATH')
        self.destination_path = os.getenv('DESTINATION_PATH')

    # Reads the relevant data from data file, and then appends data frame to existing xlsx file
    # NOTE:test first in separate file to avoid breaking status
    def setAdmins(self, indices, path, destination):

        pass


    # Do the thing
    def getAdmins(self):
        # Read files given in env
        df_call, df_members, df_ql = Load.LoadDataFrames(self, self.call_path, self.member_data_path, self.qualifier_path)

        # Identify clubs that need administrators, and potential administrators for these
        current_batch = Identify('Pulje 2')
        current_batch.IdentifyAdmins(df_call, df_ql)

        # TODO: fix Lookup after ooping



Adminipy().getAdmins()