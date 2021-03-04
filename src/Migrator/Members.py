# Get the general memeber data from foundation of a given club, and structure in a given format



class Members:
    

    # Get the relevant member data based upon clubs to migrate
    def Get_Data(self, data, members, memberships=None, trainings=None):
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
            sheet['Mobile'].update({index: int(mobile)})
        else:     
            sheet['Mobile'].update({index: mobile})
        if len(str(phone).split('.')[0]) != 3:
            sheet['Phone'].update({index: int(phone)})
        else:     
            sheet['Phone'].update({index: phone})

        sheet['Email'].update({index: email})

    # Migration Template does not currently handel postal_name, so arg remains unused. Hence commented out
    def Set_Location(self, address, postal_code, postal_name, index, sheet):
        sheet['Street'].update({index: address})
        sheet['Zip code'].update({index: postal_code})
        # sheet[''].update({index: postal_name})


    def Set_Guardians(self, g1_name, g1_email, g1_mobile, g2_name, g2_mobile, index, sheet):
        sheet['Guardian 1 name'].update({index: g1_name})
        sheet['Guardian 1 email'].update({index: g1_email})
        sheet['Guardian 2 name'].update({index: g2_name})

        # Handle Type error in mobile and phone numbers, and empty cells stored as floats
        if len(str(g1_mobile).split('.')[0]) != 3:
            sheet['Guardian 1 mobile'].update({index: int(g1_mobile)})
        else:     
            sheet['Guardian 1 mobile'].update({index: g1_mobile})
        if len(str(g2_mobile).split('.')[0]) != 3:
            sheet['Gueardian 2 mobile'].update({index: int(g2_mobile)})
        else:     
            sheet['Gueardian 2 mobile'].update({index: g2_mobile})



