from datetime import datetime

# TODO: check if there are other ways to improve matching
class Lookup:

    def __init__(self):
        self.failed = 0
        self.success = 0
        # Get current year to filter out children of callee with same contact information
        self.current_year = datetime.now().year

    # Look up missing information based upon 
    def Admin_Info(self, admins, matched_indices, df):
        missing_data = []
        for k in matched_indices:
            for info in admins[k]:
                if type(info) is float and k not in missing_data:
                    missing_data.append(k)
                    # print(f'{admins[k]} does not have sufficient data.')
        print(f'{len(missing_data)} clubs have poor data quality.\n-----')
        
        # Fill in missing names and contact info
        admins = self.getMissingData(admins, matched_indices, df)
        return admins

    # TODO: do lookup in df with built in method  or
    # convert Dataframe to dict, in order to iterate through information headers as keys instead of subset of Dataframe
    def getMissingData(self, admins, indices, df):
        print(f'======\nGetting missing contact information...')
        for admin_index in indices:
            identifier = {'Name': None, 'Mobile': None, 'Email': None}
            missing = []
            print(f'-----\nHandling {admins[admin_index][0]}')
            j = 0
            for info in admins[admin_index]:
                # ignore club name
                if j != 0:
                    # assign identifier if not assigned
                    if type(info) != float:
                        if j == 1:
                            identifier['Name'] = info
                        elif j == 2:
                            identifier['Mobile'] = info
                        elif j == 3:
                            identifier['Email'] = info
                    # identify which information if missing
                    else:
                        if type(info) == float:
                            if j == 1:
                                missing.append('Name')
                            elif j == 2:
                                missing.append('Mobile')
                            elif j == 3:
                                missing.append('Email')
                j += 1
            print(f'Setting {identifier} as identifier.')
            # if missing != []:
                # print(f'{missing} requires lookup in member registry.')
            matched = False
            # look up missing information by matching identifier
            if identifier['Name'] != None and matched == False:
                for index in range(df.shape[0]):
                    comp_name = f'{df.Firstname[index]} {df.Lastname[index]}'
                    if identifier['Name'].replace(' ', '').lower() == comp_name.replace(' ', '').lower():
                        admins[admin_index].append(index)
                    # print(f'Found match at {index} for {identifier[1]} on {comp_name}.')
                        matched = True
                        self.success += 1
                        break
            # TODO: Lookup based on NifOrgID
            if identifier['Mobile'] != None and matched == False:
                # check last line in xlsx
                for index in range(1, df.shape[0]):
                    if type(df.Birthdate[index]) == str:
                        year = int(df.Birthdate[index].split('.')[2])
                    elif type(df.Birthdate[index]) == datetime:
                        year = df.Birthdate[index].year
                    else:
                        if df.Birthdate[index] != None:
                            year = int(str(df.Birthdate[index]).split('.')[2])
                    # Assume that by the time they are 18 potential children of callee have input their own contact informatio
                    if str(identifier['Mobile']) == str(df.Mobile[index]) and self.current_year - year > 18:
                        admins[admin_index].append(index)
                        # print(f'Found match at {index} for {identifier[1]} on {df.Mobile[index]}.')
                        matched = True
                        self.success += 1
                        break
            if identifier['Email'] != None and matched == False:
                for index in range(df.shape[0]):
                    if type(df.Birthdate[index]) == str:
                        year = int(df.Birthdate[index].split('.')[2])
                    elif type(df.Birthdate[index]) == datetime:
                        year = df.Birthdate[index].year
                    else:
                        if df.Birthdate[index] != None:
                            year = int(str(df.Birthdate[index]).split('.')[2])
                    # Assume that by the time they are 18 potential children of callee have input their own contact information
                    if identifier['Email'].lower() == str(df.Email[index]).lower() and self.current_year - year > 18:
                        admins[admin_index].append(index)
                        # print(f'Found match at {index} for {identifier[1]} on {df.Email[index]}.')
                        matched = True
                        self.success += 1
                        break
            if matched == False:
                print(f'No match found for {identifier}, at {admins[admin_index][0]} in member registry...')
                self.failed += 1
            # actually get missing information where a match has been made
            if missing != []:
                print(f'Getting missing information from Member Data...')
                for category in missing:
                    if len(admins[admin_index]) == 5:
                        if category == 'Name':
                            admins[admin_index][1] = f'{df.Firstname[admins[admin_index][4]]} {df.Lastname[admins[admin_index][4]]}'
                        elif category == 'Mobile':
                            admins[admin_index][2] = df.Mobile[admins[admin_index][4]]
                        elif category == 'Email':
                            admins[admin_index][3] = df.Mobile[admins[admin_index][4]]
            # get DoB
            if len(admins[admin_index]) == 5:
                admins[admin_index][4] = (df.Birthdate[admins[admin_index][4]])
            print(f'Done with {admins[admin_index][0]}.')
        print(f'---\nfailed lookup: {self.failed}\nsuccessful lookup: {self.success}\nrating: {round(self.success/(self.success+self.failed), 3)}\n---')
        return admins