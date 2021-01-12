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
