import pandas as pd

class Load:

    # read files of callees and member data to cross reference
    # returns extrapolatet list of callee names and DataFrame of member data
    # read only necessary columns for member data to opimize resulting data frame
    # NOTE: batch 1 is differently formated than the others
    def LoadDataFrames(self, path_call, path_members, qualifier_path):
        df_call = pd.read_excel(path_call, usecols='A,C,H:J,T:V')
        df_data = pd.read_excel(path_members, usecols='A,D:H,J')
        df_ql = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='A,B,H')
        df_org = pd.read_excel(path_members, sheet_name='Club info', usecols='A,B,D')

        return df_call, df_data, df_ql, df_org