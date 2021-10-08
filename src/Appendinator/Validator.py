import pandas as pd

class Validate:

    def Member(self, data, current_org, missing_output, output_ID = None, personIDs = None):
        key = 'Member'
        bad_data_count = 0
        bad_data_locations= []
        last_row = 0
        for row in data[key].values:
            val = row[0]
            # exit when the last row has been reached
            if val == '' or pd.isna(val):
                break
            else:
                # check for missing birthdates and log if True
                if data[key]['Fødselsdato'][last_row] == '':
                    print(f'{current_org}: Bad Birthdate at {last_row}, {data[key]["Fødselsdato"][last_row]}')
                    bad_data_count += 1
                    bad_data_locations.append('Fødselsdato')
                
                # check if new membership and Training fee has valid product names
                mem = data[key]['Kontingent navn'][last_row]
                mem_list = list(data['Membership']['Navn på kontigent'].values)
                if  mem not in mem_list:
                    for m_product in mem_list:
                        if mem.lower().replace(' ', '') == m_product.lower().replace(' ', ''):
                            data[key]['Kontingent navn'][last_row] = m_product
                            break
                    print(f'{current_org}: Bad Membership at {last_row}, old product: "{mem}", new product: "{data[key]["Kontingent navn"][last_row]}"')
                    bad_data_count += 1
                    bad_data_locations.append('Kontingent navn')
                tf = data[key]['Treningsavgift navn'][last_row]
                tf_list = list(data['Training fee']['Navn på Treningsvgift'].values)
                if tf not in tf_list:
                    for t_product in tf_list:
                        if tf.lower().replace(' ', '') == t_product.lower().replace(' ', ''):
                            data[key]['Treningsavgift navn'][last_row] = t_product
                            break
                    print(f'{current_org}: Bad Training Fee at {last_row}, old product: "{tf}", new product: "{data[key]["Treningsavgift navn"][last_row]}"')
                    bad_data_count += 1
                    bad_data_locations.append('Treningsavgift')
                # check for missing address data and copy for street if so
                if data[key]['Adresse 1'][last_row] == "":
                    data[key]['Adresse 1'][last_row] = data[key]['Gatenavn'][last_row]
                    
                if output_ID != None:
                    # check for existance of output data for current org
                    if current_org in list(output_ID.keys()):
                        oid = output_ID[current_org]
                        if oid in list(personIDs.keys()):
                            org_data = personIDs[oid]
                            num_pid= len(org_data)
                            # set PersonID for member if available in output file
                            if last_row < num_pid:
                                data[key]['NIF ID'][last_row] = org_data[last_row][0]
                            #check for erronious last names, and attempt correction (based upon rules for last name in Folkereg.)
                            lastname = data[key].Etternavn.values[last_row]
                            lastname_count = len(lastname.split())
                            real_lastname = org_data[last_row][2]
                            real_firstname = org_data[last_row][1]
                            if lastname_count > 1 and lastname != real_lastname:
                                print(f'{current_org}: Bad name at {last_row}, old: {lastname}, new: {real_lastname}')
                                data[key]['Fornavn- og middelnavn'].values[last_row] = real_firstname
                                data[key].Etternavn.values[last_row] = real_lastname
                                bad_data_count += 1
                                bad_data_locations.append('Navn')
                    # log clubs without indentifiable output from KA
                    else:
                        missing_output.update({current_org: last_row})
                last_row += 1
        return data, last_row, bad_data_count, bad_data_locations, missing_output
        
    def Training_Fee(self, data, current_org):
        key = 'Training fee'
        bad_data_count = 0
        bad_data_locations= []
        last_row = 0
        for row in data[key].values:
            val = row[0]
            # exit when the last row has been reached
            if val == '' or pd.isna(val):
                break
            else:
                #set TF duration to 1 if missing
                if data[key]['Varighet (putt inn heltall)'][last_row] == '':
                    #print(f'{current_org}: Missing Duration for Training Fee at {last_row}')
                    data[key]['Varighet (putt inn heltall)'][last_row] = 1
                    bad_data_count += 1
                    bad_data_locations.append('Varightet trening')
                # check for missing data values, and set to defaults if True
                if data[key]['Automatisk fornybar'][last_row] == '':
                    data[key]['Automatisk fornybar'][last_row] = 'Ja'
                    bad_data_count += 1
                    bad_data_locations.append('Autoforny Trening')
                if data[key]['Oppstartspakke'][last_row] == '':
                    data[key]['Oppstartspakke'][last_row] = 'Nei'
                #check for invalid data types
                if type(data[key]['Beløp i kroner'][last_row]) != int:
                    data[key]['Beløp i kroner'][last_row] = 0
                    bad_data_count += 1
                    bad_data_locations.append('TF Price')
                # check for missing membershipcategories
                cat_list = list(data['Membership Category']['Medlemskategori'].values)
                tf_cat = data[key]['Medlemskategori'][last_row]
                if  tf_cat not in cat_list:
                    data['Membership Category']['NIFOrgId'][len(cat_list)] = current_org
                    data['Membership Category']['Medlemskategori'] = tf_cat
                    bad_data_count += 1
                    bad_data_locations.append('Membership Category')
                    print(f'{current_org}: Added missing category, "{tf_cat}" from {key}')
                last_row += 1
        return data, last_row, bad_data_count, bad_data_locations

    def Membership_Category(self, data):
        key = 'Membership Category'
        last_row = 0
        for row in data[key].values:
            val = row[0]
            # exit when the last row has been reached
            if val == '' or pd.isna(val):
                break
            else:
                # check for missing age ranges, and set defaults if missing
                if data[key]['Alder fra'][last_row] == '':
                    data[key]['Alder fra'][last_row] = 0
                if data[key]['Alder til '][last_row] == '':
                    data[key]['Alder til '][last_row] = 0
                last_row += 1
        return data, last_row

    def Membership(self, data, current_org):
        key = 'Membership'
        bad_data_count = 0
        bad_data_locations= []
        last_row = 0
        for row in data[key].values:
            val = row[0]
            # exit when the last row has been reached
            if val == '' or pd.isna(val):
                break
            else:
                # check for missing membershipcategories
                cat_list = list(data['Membership Category']['Medlemskategori'].values)
                mem_cat = data[key]['Medlemskategori'][last_row]
                if  mem_cat not in cat_list:
                    data['Membership Category']['NIFOrgId'][len(cat_list)] = current_org
                    data['Membership Category']['Medlemskategori'] = mem_cat
                    bad_data_count += 1
                    bad_data_locations.append('Membership Category')
                    print(f'{current_org}: Added missing category, "{mem_cat}" from {key}')
                # check for missing data values, and set to defaults if True
                if data[key]['Varighet (putt inn heltall)'][last_row] == '':
                    data[key]['Varighet (putt inn heltall)'][last_row] = 1
                    bad_data_count += 1
                    bad_data_locations.append('Varighet medlemskap')
                if data[key]['Automatisk fornybar'][last_row] == '':
                    data[key]['Automatisk fornybar'][last_row] = 'Ja'
                    bad_data_count += 1
                    bad_data_locations.append('Autoforny Medlemskap')
                if data[key]['Familiemedlem'][last_row] == '':
                    data[key]['Familiemedlem'][last_row] = 'Nei'
                if data[key]['Status'][last_row] == '':
                    data[key]['Status'][last_row] = 'Active'
                    bad_data_count += 1
                    bad_data_locations.append('Status medlemskap')
                
                # check for price that will not count at SR
                if type(data[key]['Beløp i kroner'][last_row]) != int or data[key]['Beløp i kroner'][last_row] < 50:
                    data[key]['Beløp i kroner'][last_row] = 50
                    bad_data_count += 1
                    bad_data_locations.append('Membership Price')
                last_row += 1
        return data, last_row, bad_data_count, bad_data_locations