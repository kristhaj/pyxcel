# Process data from given detail, and append to main data set

class Processor:

    # Process client details from ISD dump into main data set
    def Process_Clients(self, data, details):
        processed_data = {}
        org_list = list(data['OrgIdClub'].values())
        for i in list(details['NIFOrgID'].keys()):
            current_org = details['NIFOrgID'][i]

            org_data = {
                'name': details['Kundenavn'][i],
                'client_num': details['Kundenummer'][i],
                'client_ref': details['kund_ref'][i],
                'ext_ref': details['ekst_ref'][i],
                'gren_data': {}
                
        
            }
            # iterate thorugh and process gren data
            for data_index in range(0, len(org_list)):
                if org_list[data_index] == current_org:
                    gren_id = data['OrgIdGren'][data_index]
                    org_data['gren_data'].update({
                        gren_id: {
                            'gren_num': data['OrgNoGren'][data_index][-3:],
                            'under13': data['Under13Gren'][data_index],
                            'over13': data['Over13Gren'][data_index]
                        }
                    })
            
            processed_data.update({current_org: org_data})

        return processed_data

        

    # Process product details from federation and concat to main data set
    def Process_NKF_Products(self, data, details, gren_data):
        for org in list(data.keys()):
            org_product_data = {}
            for gren in list(data[org]['gren_data'].keys()):
                product = gren_data[data[org]['gren_data'][gren]['gren_num']]
                
                # check if club has members registered for the same product already
                if product in list(org_product_data.keys()):
                    org_product_data[product]['under13'] = org_product_data[product]['under13'] + data[org]['gren_data'][gren]['under13']
                    org_product_data[product]['over13'] = org_product_data[product]['over13'] + data[org]['gren_data'][gren]['over13']
                else:
                    org_product_data.update({
                        product: {
                            'under13': data[org]['gren_data'][gren]['under13'],
                            'over13': data[org]['gren_data'][gren]['over13']
                        }
                    })

        pass