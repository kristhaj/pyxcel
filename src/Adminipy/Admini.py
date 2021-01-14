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
        self.org_path = os.getenv('ORG_PATH')

    # Do the thing
    def getAdmins(self):
        # Read files given in env
        print(f'=====\nStarting Adminipy Routine...\n=====')
        df_call, df_members, df_ql, df_org , df_migrated= Load.LoadDataFrames(self, self.call_path, self.member_data_path, self.qualifier_path, self.org_path)

        # Identify clubs that need administrators, and potential administrators for these
        current_batch = Identify('Pulje 2')
        admins, indices = current_batch.IdentifyAdmins(df_call, df_ql, df_org)

        # Lookup missing information and DOB for the given admins
        adminable_data = Lookup.Admin_Info(Lookup(), admins, indices, df_members)

        # Write data to file
        # Write.Write_New(self, adminable_data, current_batch.batch)
        Write.Append_File(self, adminable_data, current_batch.batch, df_migrated, self.destination_path)


Adminipy().getAdmins()