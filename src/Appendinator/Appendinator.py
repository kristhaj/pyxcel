# Append seperate files into a single master file

import os
import time
import pandas as pd
import numpy as np
from Validator import Validate
from Write import Write
from Output_Handler import Handle
from Logger import Logger

class Appendinator:

    def __init__(self) -> None:
        #Get dir and destination from ENV vars
        self.data_dir = os.getenv("DATA_DIR")
        self.target_path = os.getenv("TARGET_PATH")
        self.format_path = os.getenv("FORMAT_PATH")
        self.kao_dir = os.getenv("KAO_DIR")
        self.kao_meta = os.getenv("KAO_META")

        #set start time for logging run time
        self.start_time = time.time()

    def Main(self):
        postKA = False
        if postKA:
            output_ID = Handle.OutputIDs(self, self.kao_meta)
            personIDs = Handle.PersonIDs(self, self.kao_dir)
        df = pd.read_excel(self.format_path, sheet_name=None, skiprows=1, keep_default_na=False)
        print(f'Reading data from {self.data_dir} ...')
        files = os.listdir(self.data_dir)
        files_handled = 0
        # dict for logging missing personIDs, where keys are OrgID and values are indices
        missing_output = {}
        # dict for logging clubs and areas with bad data, to be printed at the end of run
        # format {clubID: {sheet: {column: [rows]}}}
        bad_data = {}
        for f in files:
            path = f'{self.data_dir}/'+f
            data = pd.read_excel(path, sheet_name=None, skiprows=1, keep_default_na=False)
            data['Membership'].columns.values[18] = 'Status'
            current_org = data['Member'].NIFOrgId.values[0]
            bad_data.update({current_org: {}})
            for key in list(data.keys()):
                bad_data_count = 0
                bad_data_locations= []
                last_row = 0
                if key == 'Member':
                    if postKA:
                        data, last_row, bad_data_count, bad_data_locations, missing_output = Validate.Member(self, data, current_org, missing_output, output_ID, personIDs)
                    else:
                        data, last_row, bad_data_count, bad_data_locations, missing_output = Validate.Member(self, data, current_org, missing_output)
                elif key == 'Training fee':
                    data, last_row, bad_data_count, bad_data_locations = Validate.Training_Fee(self, data, current_org)
                elif key == 'Membership Category':
                    data, last_row = Validate.Membership_Category(self, data)
                elif key == 'Membership':
                    data, last_row, bad_data_count, bad_data_locations = Validate.Membership(self, data, current_org)
                else:
                    for row in data[key].values:
                        val = row[0]
                        # exit when the last row has been reached
                        if val == '' or pd.isna(val):
                            break
                        else:
                            last_row += 1
                if bad_data_count > 0:
                    bad_data_loc_count = {}
                    for loc in bad_data_locations:
                        if loc not in list(bad_data_loc_count.keys()):
                            bad_data_loc_count.update({loc: 1})
                        else:
                            bad_data_loc_count[loc] += 1
                    bad_data[current_org].update({key: [bad_data_count, bad_data_loc_count]})
                
                real_data = data[key].iloc[:last_row]
                df[key] = df[key].append(real_data, ignore_index=True)
                #print( f'{key} Shapes: processed: {df[key].shape}, raw: {data[key].shape}')
            files_handled += 1
            print(f'Processed {files_handled} out of {len(files)} files.\n')
            
        print(f'---\nFinished Processing All Data\n===\n')
        Logger.Log(self, missing_output, bad_data)
        Write.Write(self, df, self.target_path)

        print('DONE')
        print(f'Elapsed time: {time.time() - self.start_time}')
        pass






Appendinator().Main()