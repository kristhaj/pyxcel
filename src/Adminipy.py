# Cross reference call list with member data to identify administrator and relevant information.

import pandas as pd

# read files of callees and member data to cross reference
# returns extrapolatet list of callee names and DataFrame of member data
# read only necessary columns for member data to opimize resulting data frame
# NOTE: batch 1 is differently formated than the others
def LoadDataFrames(path_call, path_members, qualifier_path):
    df_call = pd.read_excel(path_call, usecols='A,C,H:J,T:V')
    df_data = pd.read_excel(path_members, usecols='B,C,H,M')
    df_ql = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='A,B,H')

    return df_call, df_data, df_ql

# Cross reference the list names with member data
# returns indices of people identified as admins
def IdentifyAdmins(names, data, ql):
    #Identifier in col A in ql
    batchID = 'Pulje 2'
    rel_clubs = getRelevantClubs(batchID, ql)
    #optimize callee dataframe, based upon given batch identifier
    callees = getCallees(names, 2, rel_clubs)
    #print degree of match
    getMatchRate(rel_clubs, callees, batchID)


    
        
    pass

def getMatchRate(rel_clubs, callees, batchID):
    print('\n=====\nCalculating Match Rating....\n')
    #TEST matching
    missing = []
    surplus = []
    matched = []
    for k in list(rel_clubs.keys()):
        missing.append(rel_clubs[k][0].replace(' ', '').lower())
    print(f'Clubs in need of admins: {len(missing)}')
    needed_count = len(missing)
    for j in list(callees.keys()):
        surplus.append(callees[j][0].replace(' ', '').lower())
    missing_count = len(missing)
    print(f'Potential Clubs in {batchID}: {len(surplus)}\n-----')
    for club in missing:
        if club in surplus:
            matched.append(club)
            del(surplus[surplus.index(club)])
    #clean up missing
    for match in matched:
        if match in missing:
            del(missing[missing.index(match)])
    print(f'Clubs with potential admins: {len(matched)}\nClubs without match: {len(missing)}\nClubs not imported or not matched: {len(surplus)}\nPotential admin match rate: {round(len(matched)/needed_count, 3)}')
    #for m in missing:
        #print(f'-----\nClub requiring manual input: {m}')
    print('=====')


# Return only the relevant data to the current data set
def getCallees(dataframe, batchID, clubs):
    #key==Club name, values==name, phone, email
    callee_info = {}
    index = 0
    print(f'Getting callee information for: Pulje {batchID}...')
    for val in dataframe.Pulje.values:
        if val == batchID:
            callee_info[index] = [dataframe.Navn.values[index], 
            dataframe.Kontaktperson.values[index], 
            dataframe.Telefon.values[index], 
            dataframe.Epost.values[index]]
            #emtpy cells are read as NaN with type float, so if there exists other contact information 
            #it is assumed that this is either the same contact person or a more relevant person
            if type(dataframe.Kontaktperson2.values[index]) is not float:
                callee_info[index][1] = dataframe.Kontaktperson2.values[index]
            if type(dataframe.Mobil2.values[index]) is not float:
                callee_info[index][2] = dataframe.Mobil2.values[index]
            if type(dataframe.Epost2.values[index]) is not float:
                callee_info[index][3] = dataframe.Epost2.values[index]
            #print(f'Identified {callee_info[index][1]} as callee for {callee_info[index][0]}.')
        index += 1
    print('Done.')
    return callee_info

def getRelevantClubs(batchID, ql):
    index = 0
    rel_clubs = {}
    print(f'Getting clubs from: {batchID}...')
    for val in ql.Pulje.values:
        if val == batchID:
            rel_clubs[index] = [ql.Klubbnavn.values[index], ql.Bruker.values[index]]
            #print(f'Identified {ql.Klubbnavn.values[index]} at index {index}.')
        index += 1
    print('Done.')

    return rel_clubs
    


# Reads the relevant data from data file, and then appends data frame to existing xlsx file
# NOTE:test first in separate file to avoid breaking status
def setAdmins(indices, path, destination):

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