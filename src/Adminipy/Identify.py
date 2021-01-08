class Identify:

    def __init__(self, batch):
        self.batch = batch

    # Cross reference the dataframes for callees against imported clubs
    # returns indices of people identified as admins
    def IdentifyAdmins(self, df_call, df_ql):
        #Identifier in col A in df_ql
        batchID = self.batch
        rel_clubs = self.getRelevantClubs(batchID, df_ql)
        #optimize callee dataframe, based upon given batch identifier
        callees = self.getCallees(df_call, 2, rel_clubs)
        #print degree of match
        self.getMatchRate(rel_clubs, callees, batchID)

        club_indices = list(rel_clubs.keys())
        callee_indices = list(callees.keys())
        matched_indices = []
        for i in callee_indices:
            for j in club_indices:
                if callees[i][0].replace(' ', '').lower() == rel_clubs[j][0].replace(' ', '').lower():
                    matched_indices.append(i)
        print(f'Identified admins at indices: {matched_indices} \n\n{len(matched_indices)} in total.')

        return callees, rel_clubs, matched_indices, batchID

    def getMatchRate(self, rel_clubs, callees, batchID):
        print('\n=====\nCalculating Match Rating....\n')
        #TEST matching
        missing = []
        surplus = []
        matched = []
        for k in list(rel_clubs.keys()):
            missing.append(rel_clubs[k][0].replace(' ', '').lower())
        print(f'Clubs in need of admins: {len(missing)}')
        needed_failed = len(missing)
        for j in list(callees.keys()):
            surplus.append(callees[j][0].replace(' ', '').lower())
        print(f'Potential Clubs in {batchID}: {len(surplus)}\n-----')
        for club in missing:
            if club in surplus:
                matched.append(club)
                del(surplus[surplus.index(club)])
        #clean up missing
        for match in matched:
            if match in missing:
                del(missing[missing.index(match)])
        print(f'Clubs with potential admins: {len(matched)}\nClubs without match: {len(missing)}\nClubs not imported or not matched: {len(surplus)}\nPotential admin match rate: {round(len(matched)/needed_failed, 3)}\n------')
        for m in missing:
            print(f'Club requiring manual input: {m}')
        print('=====')


    # Return only the relevant data to the current data set
    def getCallees(self, dataframe, batchID, clubs):
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

    def getRelevantClubs(self, batchID, df_ql):
        index = 0
        rel_clubs = {}
        print(f'Getting clubs from: {batchID}...')
        for val in df_ql.Pulje.values:
            if val == batchID:
                rel_clubs[index] = [df_ql.Klubbnavn.values[index], df_ql.Bruker.values[index]]
                #print(f'Identified {df_ql.Klubbnavn.values[index]} at index {index}.')
            index += 1
        print('Done.')

        return rel_clubs