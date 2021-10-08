# Divide a single large excel document into smaller individual ones
import os
import pandas as pd

class Divide_File:

    def __init__(self) -> None:
        #Get dir and destination from ENV vars
        self.data_path = os.getenv("DATA")
        self.target_path = os.getenv("TARGET_PATH")
        self.ka_template = os.getenv("KA_TEMPLATE")

    # Read master file
    def Load_Master(self, path):

        df_master = pd.read_excel(path, sheet_name=0, usecols="A,D,E,F,G,H,J,M,V,W,AC")
        df_club = pd.read_excel(path, sheet_name='Club info', usecols="A,D")
        return df_master, df_club

    def Load_Template(self, path):
        df = pd.read_excel(path, sheet_name=0, nrows=1, usecols="A:N")
        return df


    # Parse significant data from Data Frame into dict
    def Parse_Keys(self, df):

        values = df['NIF Klubbnummer'].values
        identifiers = {}

        index = 0
        for i in values:
            if i not in list(identifiers.keys()):
                identifiers[i] = df.Klubbnavn.values[index]
                print(f'Adding club ID: {i} as identifier for {df.Klubbnavn.values[index]}.')
                index += 1
        
        print(f'\n------\nTotal clubs identified: {len(list(identifiers.keys()))}\nExpected: {values.size}\n------\n')
        return identifiers


    # Populate dict with row indices relevant to keys
    def Populate_Indices(self, id, df):

        for key in list(id.keys()):
            indices = []
            current_index = 0
            # Row indices will be at -2 compared to row number in work book: starts at 0 and first row used as column names
            for val in df.NIFOrgId.values:
                if val == key:
                    indices.append(current_index)
                current_index += 1
            id[key] = indices
        return id

    # Iterate through keys and fetch data based on row indices
    def Make_Files(self, meta, path, df_master, club):

        significant_values = list(meta.keys())


        print('Writing files...')
        for id in significant_values:
            df_template = self.Load_Template(path).to_dict()
            df_filtered = df_master.loc[meta[id]]
            for row in meta[id]:
                index = row - meta[id][0]
                df_template['Klubb'].update({index: club[id]})
                df_template['KlubbID'][index] = df_filtered['NIFOrgId'][row]
                df_template['Kjønn'][index] = df_filtered['Kjønn'][row]
                df_template['Født'][index] = df_filtered['Fødselsdato'][row]
                df_template['Etternavn'][index] = df_filtered['Etternavn'][row]
                df_template['Fornavn'][index] = df_filtered['Fornavn- og middelnavn'][row]
                df_template['Gateadresse'][index] = df_filtered['Gatenavn'][row]
                df_template['Postnr'][index] = df_filtered['Postnummer'][row]
                df_template['Tlf privat'][index] = df_filtered['Telefon'][row]
                df_template['Tlf mobil'][index] = df_filtered['Mobil'][row]
                df_template['E-post'][index] = df_filtered['E-post'][row]
                df_template['Medlem fom'][index] = df_filtered['Medlemskap registreringsdato'][row]

            # Update for each batch
            make_path = f'{self.target_path}{club[id]}_{id}_KA.xlsx'
            df = pd.DataFrame.from_dict(df_template).copy()
            df['Kjønn'].replace({'Mann': 'M', 'Kvinne': 'K', 'mann': 'M', 'kvinne': 'K'}, inplace=True)
            with pd.ExcelWriter(make_path, date_format='DD.MM.YYYY', datetime_format='DD.MM.YYYY') as writer:
                df.to_excel(writer,sheet_name='Medlemmer', index=False)
            print(f'{club[id]} is done...')
        print('Done.')

    # Do the thing
    def Main(self):
        df_master, df_club = self.Load_Master(self.data_path)
        identifiers = self.Parse_Keys(df_club)
        club_id= identifiers.copy()
        meta_data = self.Populate_Indices(identifiers, df_master)
        self.Make_Files(meta_data, self.ka_template, df_master, club_id)


Divide_File().Main()