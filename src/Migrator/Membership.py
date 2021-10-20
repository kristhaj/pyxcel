# Extrapolate  membership data for current organization and apply to relevant members




class Membership:


    # Extrapolate membership data from data base
    def Get_Data(self, data, sheet, cat_sheet, info, member_sheet=None):
        print(f'Processing Membership Products and Categories for:')
        for key in list(data.keys()):
            c_name = info[key][0]
            print(f'{c_name}....')
            Membership.Set_Categories(self, data[key], [key, c_name], cat_sheet)
            Membership.Set_Products(self, data[key], key, sheet, member_sheet)
        
        print(f'All relevant Membership Product Data Processed.\n')
        return sheet, cat_sheet
    
    # Extrapolate Membership Category and relating data
    def Set_Categories(self, data, club_info, categories):
        processed_categories = []
        for val in list(data['Medlemskategori navn'].values()):
            next_key = len(categories['NIFOrgId'])
            if val not in processed_categories:
                processed_categories.append(val)
                categories['NIFOrgId'].update({next_key: club_info[0]})
                categories['Membership Category'].update({next_key: val})
                categories['Club Name'].update({next_key: club_info[1]})
                categories['Status'].update({next_key: 'Aktiv'})
                categories['Defualt membership '].update({next_key: 'Nei'})
                categories['Defualt Training '].update({next_key: 'Nei'})

    # Extrapolate Membership Product data 
    def Set_Products(self, data, id, memberships, member_sheet):
        processed_memberships = []
        for key in list(data['Etternavn'].keys()):
            next_key = len(memberships['NIFOrgId'])
            membership = data['Kont.sats'][key].replace('  ', ' ')
            if membership not in processed_memberships:
                processed_memberships.append(membership)
                memberships['NIFOrgId'].update({next_key: id})
                memberships['Membership Name'].update({next_key: membership})
                memberships['Membership Category'].update({next_key: data['Medlemskategori navn'][key]})
                memberships['Price in NOK'].update({next_key: data['Kont.pris'][key]})
                memberships['Duration'].update({next_key: 1})
                memberships['Duration type'].update({next_key: 'År'})
                memberships['Invoice Duration'].update({next_key: 1})
                memberships['Invoice Duration type'].update({next_key: 'År'})
                memberships['Renewal'].update({next_key: 'Ja'})
                memberships['Family membership'].update({next_key: 'Nei'})
                memberships['Status'].update({next_key: 'Aktiv'})
        

    # Apply the correct memberships to the correct members
    def Apply_Product(self, product, onboarded, index, member_sheet):

        product = product.replace('  ', ' ')
        member_sheet['Membership name'].update({index: product})
        member_sheet['Membership on-boarding date'].update({index: onboarded})