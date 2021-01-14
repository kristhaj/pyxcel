import pandas as pd

class Write:
    # Write admin data to new file
    def Write_New(self, dictionary, batch):
        data = {'Header': ['Klubbnavn', 'Kontaktperson', 'Mobil', 'Epost', 'Fødselsdato']}
        data.update(dictionary)
        temp_df = pd.DataFrame.from_dict(data, orient='index')
        print(f'\n=====\nWriting completish list of admin information for {batch}...\n=====\n')
        # appended comment to make pyLint ignore false positive problem
        with pd.ExcelWriter(f'files/admin/Admin_{batch}.xlsx') as writer: # pylint: disable=abstract-class-instantiated
                temp_df.to_excel(writer, index=False, header=False)
    
    # Append admin data to existing file
    def Append_File(self, dictionary, batch, df_migrated, path):
        # Format data to input into existing file.
        admin_users = {}
        for key in dictionary:
            if len(dictionary[key]) == 5:
                admin_users.update({key: f'{dictionary[key][1]} / {dictionary[key][4]}'})
        # Make df to append admin info as new sheet
        data = {'Header': ['Klubbnavn', 'Kontaktperson', 'Mobil', 'Epost', 'Fødselsdato']}
        data.update(dictionary)
        temp_df = pd.DataFrame.from_dict(data, orient='index')
        # Add admin data to df
        for index in admin_users:
            df_migrated.Bruker[index] = admin_users[index]
        print(f'\n=====\nAppending Admin user data for {batch} to existing file at {path}...')
        # Write user row, and admin data to new sheet
        with pd.ExcelWriter(path, engine='openpyxl', mode='a') as writer: # pylint: disable=abstract-class-instantiated
                df_migrated.to_excel(writer, sheet_name='Tabell', index=False, header=False, startcol=7, startrow=1)
                temp_df.to_excel(writer, sheet_name=f'Admin Info {batch}', index=False, header=False)
        print('\nDone.\n=====')

