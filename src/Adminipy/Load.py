import pandas as pd

class Load:

    # read files of callees and member data to cross reference
    # returns extrapolated list of callee names and DataFrame of member data
    # read only necessary columns for member data to opimize resulting data frame
    # NOTE: batch 1 is differently formated than the others
    def LoadDataFrames(self, path_call, path_members, qualifier_path, org_path):
        print('Loading data:\n-----')
        print('Loading Callees...')
        df_call = pd.read_excel(path_call, usecols='A,C,H:J,T:V')
        print('Loading Qualifying Clubs...')
        df_ql = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='A,B,H')
        print('Loading Club Org Info...')
        df_org = pd.read_excel(org_path, sheet_name='Club info', usecols='A,B,D')
        print('Loading Member Data...\n')
        # NOTE: set nrows for each batch
        df_data = pd.read_excel(path_members, usecols='A,D:H,J', nrows=1026)
        print('Loading Club Admin User Row')
        df_migrated = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='H')
        
        print('Done.\n-----')
        return df_call, df_data, df_ql, df_org, df_migrated