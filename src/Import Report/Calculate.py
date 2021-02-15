# Calculate the discrepancy between the two data sets

class Calculate:

    def Guardian_Discrepancy(self, imported_data, original_data):

        print('Calculating Data Deviation for Guardian Information...')

        discrepancies = {'Identifier': {},
                        'Name': {},
                        'Birthdate': {},
                        'Og_Guardian1': {},
                        'Imported_Guardian1': {},
                        'Og_Guardian1_Mob': {},
                        'Imported_Guardian1_Mob': {},
                        'Og_Guardian1_Email': {},
                        'Imported_Guardian1_Email': {},
                        'Og_Guardian2': {},
                        'Imported_Guardian2': {},
                        'Og_Guardian2_Mob': {},
                        'Imported_Guardian2_Mob': {},
                        'Og_Guardian2_Email': {},
                        'Imported_Guardian2_Email': {}}

        import_keys = list(imported_data['NifOrgID'].keys())
        og_keys = list(original_data['Etternavn'].keys())

        deviating_keys = {'import': [], 'og': []}

        for key in import_keys:
            if key not in deviating_keys['import']:
                for og_key in og_keys:
                    if og_key not in deviating_keys['og']:
                        comparative_imported_name = (imported_data['fistname'][key] + imported_data['lastname'][key]).replace(' ', '').lower()
                        comparative_original_name = (original_data['Fornavn'][og_key] + original_data['Etternavn'][og_key]).replace(' ', '').lower()
                        index = len(list(discrepancies['Identifier'].keys()))
                        if comparative_imported_name == comparative_original_name:
                            # find number of digits in og_key 
                            digits = len(str(og_key)) 
                            # add zeroes to the end of key 
                            dkey = key * (10**digits)
                            # add og_key to dkey 
                            dkey += og_key
                            deviation = {'Identifier': {index: dkey},
                                        'Name': {index: original_data['Fornavn'][og_key] + original_data['Etternavn'][og_key]},
                                        'Birthdate': {index: original_data['Fødselsdato']},
                                        'Og_Guardian1': {index: None},
                                        'Imported_Guardian1': {index: None},
                                        'Og_Guardian1_Mob': {index: None},
                                        'Imported_Guardian1_Mob': {index: None},
                                        'Og_Guardian1_Email': {index: None},
                                        'Imported_Guardian1_Email': {index: None},
                                        'Og_Guardian2': {index: None},
                                        'Imported_Guardian2': {index: None},
                                        'Og_Guardian2_Mob': {index: None},
                                        'Imported_Guardian2_Mob': {index: None},
                                        'Og_Guardian2_Email': {index: None},
                                        'Imported_Guardian2_Email': {index: None}}
                            deviating = False
                            # Compare Guardian 1 Name
                            if imported_data['guardian1'] != original_data['Foresatt 1']:
                                deviation['Og_Guardian1'][index] = original_data['Foresatt 1']
                                deviation['Imported_Guardian1'][index] = imported_data['guardian1']
                                deviating = True
                            # Compare Guardian 1 Mobile
                            if imported_data['g1_mobile'] != original_data['Foresatt 1 telefon']:
                                deviation['Og_Guardian1_Mob'][index] = original_data['Foresatt 1 telefon']
                                deviation['Imported_Guardian1_Mob'][index] = imported_data['g1_mobile']
                                deviating = True
                            # Compare Guardian 1 Email
                            if imported_data['g1_email'] != original_data['Foresatt 1 epost']:
                                deviation['Og_Guardian1_Email'][index] = original_data['Foresatt 1 epost']
                                deviation['Imported_Guardian1_Email'][index] = imported_data['g1_email']
                                deviating = True
                            # Compare Guardian 2 Name
                            if imported_data['guardian2'] != original_data['Foresatt 2']:
                                deviation['Og_Guardian2'][index] = original_data['Foresatt 2']
                                deviation['Imported_Guardian2'][index] = imported_data['guardian2']
                                deviating = True
                            # Compare Guardian 2 Mobile
                            if imported_data['g2_mobile'] != original_data['Foresatt 2 telefon']:
                                deviation['Og_Guardian2_Mob'][index] = original_data['Foresatt 2 telefon']
                                deviation['Imported_Guardian2_Mob'][index] = imported_data['g2_mobile']
                                deviating = True
                            # Compare Guardian 2 Email
                            if imported_data['g2_email'] != original_data['Foresatt 2 epost']:
                                deviation['Og_Guardian2_Email'][index] = original_data['Foresatt 2 epost']
                                deviation['Imported_Guardian2_Email'][index] = imported_data['g2_email']
                                deviating = True
                            
                            if deviating:
                                deviating_keys['import'].append(key)
                                deviating_keys['og'].append(og_key)

                                for data in list(deviation.keys()):
                                    discrepancies[data].update(deviation[data])
        
        
        print('Done.\n===')
        return discrepancies