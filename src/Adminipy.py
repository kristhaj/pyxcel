# Cross reference call list with member data to identify administrator and relevant information.

import pandas as pd

# read files of callees and member data to cross reference
# returns extrapolatet list of callee names and DataFrame of member data
# read only necessary columns for member data to opimize resulting data frame
# NOTE: batch 1 is differently formated than the others
def LoadDataFrames(path_call, path_members, qualifier_path):
    df_call = pd.read_excel(path_call, usecols='A,C,H,J,T')
    df_data = pd.read_excel(path_members, usecols='B,C,H,M')
    df_ql = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='A,B')

    return df_call, df_data, df_ql

# Cross reference the list names with member data
# returns indices of people identified as admins
def IdentifyAdmins(names, data, ql):
    #optimize callee dataframe, based upon given batch identifier
    relevant_callees = FilterCallees(names, 2, ql)

    pass

# Return only the relevant data to the current data set
def FilterCallees(dataframe, batch, ql):
    identifying_information = {}


    pass

# Reads the relevant data from data file, and then appends data frame to existing xlsx file
# NOTE:test first in separate file to avoid breaking status
def CommitAdmins(indices, path, destination):

    pass


# Do the thing
def Main():
    call_path = 'pyxcel/files/admin/ringeliste.xlsx'
    #set for each batch to process
    member_data_path = 'pyxcel/files/admin/pulje2.xlsx'
    qualifier_path = 'pyxcel/files/admin/migreringsoversikt.xlsx'
    destination_path = 'pyxcel/files/admin/testo.xlsx'

    callees, data, ql = LoadDataFrames(call_path, member_data_path, qualifier_path)

    IdentifyAdmins(callees, data, ql)


Main()