from datetime import datetime

# TODO: finish DOB lookup
class Lookup:

    #Look up missing information based upon 
    def getAdminInfo(self, callees, matched_indices, df, org, batch):
        missing_data = []
        for k in matched_indices:
            for info in callees[k]:
                if type(info) is float and k not in missing_data:
                    missing_data.append(k)
                    #print(f'{callees[k]} does not have sufficient data.')
        print(f'{len(missing_data)} clubs have poor data quality.\n-----')
        
        #Fill in missing names and contact info
        callees = self.getMissingData(callees, matched_indices, df, org)
        #Write_Temp_Contacts(callees, batch)

    #TODO: do lookup in df with built in method  or
    # convert Dataframe to dict, in order to iterate through information headers as keys instead of subset of Dataframe
    def getMissingData(self, callees, indices, df, org):
        print(f'======\nGetting missing contact information...')
        failed = 0
        success = 0
        for call_index in indices:
            identifier = {}
            missing = []
            #print(f'Handling {callees[call_index][0]}\n-----')
            j = 0
            for info in callees[call_index]:
                #ignore club name
                if j != 0:
                    #assign identifier if not assigned
                    if type(info) != float and identifier == {}:
                        if j == 1:
                            identifier.Name = info
                        elif j == 2:
                            identifier = ['Mobile', info]
                        elif j == 3:
                            identifier = ['Email', info]
                        #print(f'Setting {identifier} as identifier.')
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
            #if missing != []:
                #print(f'{missing} requires lookup in member registry.')
            # Get current year to filter out children of callee with same contact information
            current_year = datetime.now().year
            matched = False
            #look up missing information by matching identifier
            #TODO: improve lookup in member data basis to improve hit rate
            # Multiple identifiers? IR?
            if identifier[0] == 'Name':
                for index in range(df.shape[0]):
                    comp_name = f'{df.Firstname[index]} {df.Lastname[index]}'
                    if identifier[1].replace(' ', '').lower() == comp_name.replace(' ', '').lower():
                        callees[call_index].append(index)
                    # print(f'Found match at {index} for {identifier[1]} on {comp_name}.')
                        matched = True
                        success += 1
                        break
            elif identifier[0] == 'Mobile':
                for index in range(df.shape[0]):
                    # Assume that by the time they are 18 potential children of callee have input their own contact information
                    if str(identifier[1]) == str(df.Mobile[index]) and current_year - int(df.Birthdate[index].split('.')[2]) > 18:
                        callees[call_index].append(index)
                        #print(f'Found match at {index} for {identifier[1]} on {df.Mobile[index]}.')
                        matched = True
                        success += 1
                        break
            elif identifier[0] == 'Email':
                for index in range(df.shape[0]):
                    # Assume that by the time they are 18 potential children of callee have input their own contact information
                    if identifier[1] == df.Email[index] and current_year - int(df.Birthdate[index].split('.')[2]) > 18:
                        callees[call_index].append(index)
                        #print(f'Found match at {index} for {identifier[1]} on {df.Email[index]}.')
                        matched = True
                        success += 1
                        break
            if matched == False:
                #print(f'No match found for {identifier[1]} in member registry...')
                failed += 1
            # actually get missing information where a match has been made
            #if missing != []:
                #for category in missing:


        print(f'---\nfailed lookup: {failed}\nsuccessful lookup: {success}\nrating: {round(success/(success+failed), 3)}\n---')
        return callees