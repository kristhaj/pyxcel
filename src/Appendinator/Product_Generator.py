# Generates generic products for clubs that have no previous product data to import

class Product_Generator:

    # Generate a generic category
    def Category(self, data, org):
        gen_cat = {
            'NIFOrgId': org, 
            'Medlemskategori': 'Medlem', 
            'Navn på klubb': data['Navn på klubb'][0], 
            'Alder fra': 0, 
            'Alder til ': 0, 
            'Status': 'Aktiv', 
            'Standard medlemskap': 'Medlemskontingent', 
            'Standard trening': 'Treningsavgift'}
        data = data.append(gen_cat, ignore_index=True)

        return data

    # Generate a generic membership    
    def Membership(self, data, org):
        gen_membership = [org,'Medlemskontingent','Medlem',50,1,'År',1,'År','','','','','','','','','Ja','Nei','Aktiv']
        data.loc[0] = gen_membership
        return data

    # Generate a generic training fee
    def Training_Fee(self, data, org):
        gen_training_fee = [org,'Treningsavgift','','Medlem',0,1,'Måned',1,'Måned','','','','','','','','Ja','Nei']
        data.loc[0] = gen_training_fee
        return data