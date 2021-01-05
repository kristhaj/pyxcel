# Cross reference call list with member data to identify administrator and relevant information.

import pandas as pd
from datetime import datetime

# read files of callees and member data to cross reference
# returns extrapolatet list of callee names and DataFrame of member data
# read only necessary columns for member data to opimize resulting data frame
# NOTE: batch 1 is differently formated than the others
def LoadDataFrames(path_call, path_members, qualifier_path):
    df_call = pd.read_excel(path_call, usecols='A,C,H:J,T:V')
    df_data = pd.read_excel(path_members, usecols='A,D:H,J')
    df_ql = pd.read_excel(qualifier_path, sheet_name='Tabell', usecols='A,B,H')
    df_org = pd.read_excel(path_members, sheet_name='Club info', usecols='A,B,D')

    return df_call, df_data, df_ql, df_org

# Cross reference the list names with member data
# returns indices of people identified as admins
def IdentifyAdmins(names, data, ql, org):
    #Identifier in col A in ql
    batchID = 'Pulje 2'
    rel_clubs = getRelevantClubs(batchID, ql)
    #optimize callee dataframe, based upon given batch identifier
    callees = getCallees(names, 2, rel_clubs)
    #print degree of match
    getMatchRate(rel_clubs, callees, batchID)

    club_indices = list(rel_clubs.keys())
    callee_indices = list(callees.keys())
    matched_indices = []
    for i in callee_indices:
        for j in club_indices:
            if callees[i][0].replace(' ', '').lower() == rel_clubs[j][0].replace(' ', '').lower():
                matched_indices.append(i)
    print(f'Identified admins at indices: {matched_indices} \n\n{len(matched_indices)} in total.')

    admin_info = getAdminInfo(callees, matched_indices, data, org, batchID)
    pass
#Look up missing information based upon 
def getAdminInfo(callees, matched_indices, df, org, batch):
    missing_data = []
    for k in matched_indices:
        for info in callees[k]:
            if type(info) is float and k not in missing_data:
                missing_data.append(k)
                #print(f'{callees[k]} does not have sufficient data.')
    print(f'{len(missing_data)} clubs have poor data quality.\n-----')
    
    #Fill in missing names and contact info
    callees = getMissingData(callees, list(callees.keys()), df, org)
    #Write_Temp_Contacts(callees, batch)
    

#Write temporary contact information to file
def Write_Temp_Contacts(dictionary, batch):
    data = {'Header': ['Klubbnavn', 'Kontaktperson', 'Mobil', 'Epost']}
    data.update(dictionary)
    temp_df = pd.DataFrame.from_dict(data, orient='index')
    print(f'\n=====\nWriting completish list of contact information for {batch}...\n=====\n')
    with pd.ExcelWriter(f'pyxcel/files/admin/kontaktinformasjon_{batch}.xlsx') as writer:
            temp_df.to_excel(writer, index=False, header=False)

#TODO: do lookup in df with built in method  or
# convert Dataframe to dict, in order to iterate through information headers as keys instead of subset of Dataframe
def getMissingData(callees, indices, df, org):
    print(f'======\nGetting missing contact information...')
    for call_index in indices:
        identifier = None
        missing = []
        print(f'\nHandling {callees[call_index][0]}\n-----')
        j = 0
        for info in callees[call_index]:
            #ignore club name
            if j != 0:
                #assign identifier if not assigned
                if type(info) != float and identifier == None:
                    if j == 1:
                        identifier = ['Name', info]
                    elif j == 2:
                        identifier = ['Mobile', info]
                    elif j == 3:
                        identifier = ['Email', info]
                    print(f'Setting {identifier} as identifier.')
                #identify which information if missing
                else:
                    if type(info) == float:
                        if j == 1:
                            missing.append('Name')
                        elif j == 2:
                            missing.append('Mobile')
                        elif j == 3:
                            missing.append('Email')
            j += 1
        if missing != []:
            print(f'{missing} requires lookup in member registry.')
        # Get current year to filter out children of callee with same contact information
        current_year = datetime.now().year
        matched = False
        #look up missing information by matching identifier
        #TODO: multiple identifiers?
        if identifier[0] == 'Name':
            for index in range(df.shape[0]):
                comp_name = f'{df.Firstname[index]} {df.Lastname[index]}'
                if identifier[1].replace(' ', '').lower() == comp_name.replace(' ', '').lower():
                    callees[call_index].append(index)
                    print(f'Found match at {index} for {identifier[1]} on {comp_name}.')
                    matched = True
                    break
        elif identifier[0] == 'Mobile':
            for index in range(df.shape[0]):
                # Assume that by the time they are 18 potential children of callee have input their own contact information
                if str(identifier[1]) == str(df.Mobile[index]) and current_year - int(df.Birthdate[index].split('.')[2]) > 18:
                    callees[call_index].append(index)
                    print(f'Found match at {index} for {identifier[1]} on {df.Mobile[index]}.')
                    matched = True
                    break
        elif identifier[0] == 'Email':
            for index in range(df.shape[0]):
                # Assume that by the time they are 18 potential children of callee have input their own contact information
                if identifier[1] == df.Email[index] and current_year - int(df.Birthdate[index].split('.')[2]) > 18:
                    callees[call_index].append(index)
                    print(f'Found match at {index} for {identifier[1]} on {df.Email[index]}.')
                    matched = True
                    break
        if matched == False:
            print(f'No match found for {identifier[1]} in member regisrty...')
        # actually get missing information where a match has been made
        #if missing != []:
            #for category in missing:



    return callees

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
    print(f'Clubs with potential admins: {len(matched)}\nClubs without match: {len(missing)}\nClubs not imported or not matched: {len(surplus)}\nPotential admin match rate: {round(len(matched)/needed_count, 3)}\n------')
    for m in missing:
        print(f'Club requiring manual input: {m}')
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
    # win rel path files*
    # linux rel path pyxcel/files*
    # prep: H==Kontaktperon, J==Epost, T==Kontaktperson2, U==Mobil2, V==Epost2
    call_path = 'files/admin/ringeliste.xlsx'
    # set for each batch to process
    # prep: D==Firstname, E==Lastname
    member_data_path = 'files/admin/pulje2.xlsx'
    # prep: remove whitespace from A
    qualifier_path = 'files/admin/migreringsoversikt.xlsx'
    destination_path = 'files/admin/testo.xlsx'

    callees, data, ql, org = LoadDataFrames(call_path, member_data_path, qualifier_path)

    IdentifyAdmins(callees, data, ql, org)


Main()