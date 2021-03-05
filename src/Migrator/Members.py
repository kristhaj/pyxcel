# Get the general memeber data from foundation of a given club, and structure in a given format

from Membership import Membership
from Trainings import Trainings

class Members:
    

    # Get the relevant member data based upon clubs to migrate
    def Get_Data(self, data, members, multi_gren_clubs=None):
        print(f'Processing Member data for:')
        for key in list(data.keys()):
            print(f'{key}....')
            for m_key in list(data[key]['Medlemsnummer'].keys()):
                next_index = len(members['NIFOrgId'])
                members['NIFOrgId'].update({next_index: key})

                Members.Set_Personalia(self, 
                data[key]['Medlemsnummer'][m_key],
                data[key]['Etternavn'][m_key], 
                data[key]['Fornavn'][m_key], 
                data[key]['Kjønn'][m_key], 
                data[key]['Fødselsdato'][m_key],
                next_index, members)
                
                Members.Set_Contact_Information(self, 
                data[key]['Mobil'][m_key],
                data[key]['Epost'][m_key],
                data[key]['Telefon'][m_key],
                next_index, members)

                Members.Set_Location(self,
                data[key]['Adresse 2'][m_key],
                data[key]['Postnr'][m_key],
                data[key]['Sted'][m_key],
                next_index, members)

                Members.Set_Guardians(self,
                data[key]['Foresatte'][m_key],
                data[key]['Foresatte epost'][m_key],
                data[key]['Foresatte mobil'][m_key],
                data[key]['Foresatte nr 2'][m_key],
                data[key]['Foresatte nr 2 mobil'][m_key],
                next_index, members)
                


                # Apply Products
                Membership.Apply_Product(self, 
                data[key]['Kont.sats'][m_key], 
                data[key]['Innmeldtdato'][m_key], 
                next_index, members)
                
                if multi_gren_clubs != None and key in multi_gren_clubs:
                    g_val = data[key]['Gren/Stilart/Avd/Parti - Gren/Stilart/Avd/Parti'][m_key]
                    if type(g_val) != float:
                        g_val = g_val.split('/')[0]
                    Trainings.Apply_Product(self, 
                    data[key]['Kontraktstype'][m_key],
                    next_index, members, g_val)
                else:
                    Trainings.Apply_Product(self, 
                    data[key]['Kontraktstype'][m_key],
                    next_index, members)
        
        print(f'All Personal Member Data has been Processed and Products have been Applied.')
        return members


    def Set_Personalia(self, memberID, lastname, firstname, gender, bdate, index, sheet):
        sheet['External MemberID'].update({index: memberID})
        sheet['Firstname and middlename'].update({index: firstname})
        sheet['Last name'].update({index: lastname})
        sheet['Gender'].update({index: gender})
        sheet['Birthdate'].update({index: bdate})


    def Set_Contact_Information(self, mobile, email, phone, index, sheet):
        # Handle Type error in mobile and phone numbers, and empty cells stored as floats
        if len(str(mobile).split('.')[0]) != 3:
            if type(mobile) == str:
                mobile = mobile.split(' ')[0]
            try:
                sheet['Mobile'].update({index: int(mobile)})
            except:
                print('Club is bad at inputing data')
        else:     
            sheet['Mobile'].update({index: mobile})
        if len(str(phone).split('.')[0]) != 3:
            if type(phone) == str:
                phone = phone.replace(' ', '')
            try:
                sheet['Phone'].update({index: int(phone)})
            except:
                print('Club is bad at inputing data')
        else:     
            sheet['Phone'].update({index: phone})

        sheet['Email'].update({index: email})

    # Migration Template does not currently handel postal_name, so arg remains unused. Hence commented out
    def Set_Location(self, address, postal_code, postal_name, index, sheet):
        sheet['Street'].update({index: address})
        # Handle postal codes in Oslo
        try:
            p = str(int(postal_code)).rjust(4, '0')
            sheet['Zip code'].update({index: p})
        except:
            print('Club is bad at inputing data')
        # sheet[''].update({index: postal_name})


    def Set_Guardians(self, g1_name, g1_email, g1_mobile, g2_name, g2_mobile, index, sheet):
        sheet['Guardian 1 name'].update({index: g1_name})
        sheet['Guardian 1 email'].update({index: g1_email})
        sheet['Guardian 2 name'].update({index: g2_name})

        # Handle Type error in mobile and phone numbers, and empty cells stored as floats
        if len(str(g1_mobile).split('.')[0]) != 3:
            try:
                sheet['Guardian 1 mobile'].update({index: int(g1_mobile)})
            except:
                print('Club is bad at inputing data')
        else:     
            sheet['Guardian 1 mobile'].update({index: g1_mobile})
        if len(str(g2_mobile).split('.')[0]) != 3:
            try:
                sheet['Gueardian 2 mobile'].update({index: int(g2_mobile)})
            except:
                print('Club is bad at inputing data')
        else:     
            sheet['Gueardian 2 mobile'].update({index: g2_mobile})



