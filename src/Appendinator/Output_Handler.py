import pandas as pd
import numpy as np
import os


class Handle:

    def OutputIDs(self, path):
        df = pd.read_excel(path, usecols="B,C", keep_default_na=False)
        org_output_id = {}
        for i in range(df.shape[0]):
            orgID = df.Orgid.values[i]
            outputID = df.outputID.values[i]
            valid_data_types = [int, np.int64]
            if type(outputID) in valid_data_types:
                org_output_id.update({orgID: outputID})
            else:
                org_output_id.update({orgID: orgID})
        return org_output_id



    # get person IDs from KA Output
    def PersonIDs(self, dir):
        pid_dict = {}
        files = os.listdir(dir)
        files_handled = 0
        for file in files:
            path = dir + '/' + file
            print(f'Reading PersonIDs at {path} ...')
            types = {'Id':np.int64, 'OrgId': np.int64, 'PersonId': np.int64, 'BirthDate': str}
            df = pd.read_csv(path, sep=",", dtype=types)

            for i in df.Id.values:
                index = i-1
                org = df.OrgId.values[index]
                row_pid_pairing = {index: [df.PersonId.values[index], df.FirstName.values[index] ,df.LastName.values[index], df.Gender.values[index], df.BirthDate.values[index]]}
                if org not in list(pid_dict.keys()):
                    pid_dict[org]= row_pid_pairing
                else:
                    pid_dict[org].update(row_pid_pairing)

            files_handled += 1
            print(f'Read personID from {files_handled} of {len(files)} clubs.\n')

        return pid_dict