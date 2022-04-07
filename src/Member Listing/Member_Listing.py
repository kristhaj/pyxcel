# Combine member data from old and new export, and format to the users needs

import os
import re
from tokenize import String
from Load import Load
from Write import Write

class Member_Listing:

    def __init__(self):
        self.beta_data_path = os.getenv("BETA_DATA_PATH")
        self.old_data_path = os.getenv("OLD_DATA_PATH")
        self.destination_path = os.getenv("DESTINATION_PATH")


    #do the thing
    def Spond_List(self):
        old_columns = ['NIF nummer', 'Navn', 'DOB']

        beta_data = Load.Member_File(self, self.beta_data_path)
        old_data = Load.Member_File(self, self.old_data_path, old_columns)

        print('Data Loaded.. \n\n Proceeding to format data.')

        spond_data = {
            'PersonID': {},
            'For- + Mellomnavn': {},
            'Etternavn': {},
            'Fødselsdato': {},
            'Kjønn': {},
            'Telefon': {},
            'e-post': {},
            'Adresse': {},
            'Postnr': {},
            'Poststed': {},
            'Medlemskap': {}
        }
        beta_member_list = list(beta_data['Navn'].values())
        old_member_list = list(old_data['Navn'].values())
        # Row in spond_data
        row = 0
        for member in beta_member_list:
            beta_index = beta_member_list.index(member)
            personID = beta_data['Person ID'][beta_index]
            old_index = False
            try:
                old_index = old_member_list.index(member)
            except:
                print(f'No name match for: {member}, {personID}')
            if not old_index:
                try:
                    old_index = old_member_list.index(personID)
                except:
                    print(f'No person id match for: {member}, {personID}')

            # Process names into distinct given names and surnames
            name_components = member.split(' ')
            given_name = ''
            for i in range(0, len(name_components)-1):
                given_name += f'{name_components[i]} '
            surname = name_components[-1]

            # Process Postal data
            postal_data = beta_data['Lokasjon'][beta_index]
            if type(postal_data) != float:
                postal_components = re.split('(\d+)', postal_data)
                postal_code = postal_components[1]
                postal_area = None
                if len(postal_components) > 2:
                    postal_area = postal_components[2]
                else:
                    print(f'Missing postal area for: {member}, {beta_data["Person ID"][beta_index]}')
            else:
                print('Missing Postal Data')
                postal_code = 'Missing data'
                postal_area = 'Missing data'
            # Update spond_data with member data
            spond_data['PersonID'].update({row: personID})
            spond_data['For- + Mellomnavn'].update({row: given_name})
            spond_data['Etternavn'].update({row: surname})
            if personID != False:
                spond_data['Fødselsdato'].update({row: old_data['DOB'][old_index]})
            else:
                spond_data['Fødselsdato'].update({row: 'No match'})
            spond_data['Kjønn'].update({row: beta_data['Kjønn'][beta_index]})
            spond_data['Telefon'].update({row: str(beta_data['Mobil'][beta_index])[2:-2]})
            spond_data['e-post'].update({row: beta_data['Epost'][beta_index]})
            spond_data['Adresse'].update({row: ''})
            spond_data['Postnr'].update({row: postal_code})
            spond_data['Poststed'].update({row: postal_area})
            spond_data['Medlemskap'].update({row: beta_data['Navn medlemskontingent'][beta_index]})
            row += 1
        # Write processed data to file
        print('\nData processed. Attempting to write to file...')

        Write.Spond_File(self, spond_data, self.destination_path)

        pass


Member_Listing().Spond_List()