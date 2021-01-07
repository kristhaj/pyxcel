import pandas as pd

class Write:
    #Write temporary contact information to file
    def Temp_Contacts(self, dictionary, batch):
        data = {'Header': ['Klubbnavn', 'Kontaktperson', 'Mobil', 'Epost']}
        data.update(dictionary)
        temp_df = pd.DataFrame.from_dict(data, orient='index')
        print(f'\n=====\nWriting completish list of contact information for {batch}...\n=====\n')
        # appended comment to make pyLint ignore false positive problem
        with pd.ExcelWriter(f'pyxcel/files/admin/kontaktinformasjon_{batch}.xlsx') as writer: # pylint: disable=abstract-class-instantiated
                temp_df.to_excel(writer, index=False, header=False)