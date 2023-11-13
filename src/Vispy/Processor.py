# Process data from given detail, and append to main data set

from datetime import datetime, timedelta

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
                'inv_num': details['Fakturanummer'][i],
                'gren_data': {}
            }
            # iterate thorugh and process gren data
            for data_index in range(0, len(org_list)):
                if org_list[data_index] == current_org:
                    gren_id = data['OrgIdGren'][data_index]
                    org_data['gren_data'].update({
                        gren_id: {
                            'gren_num': int(data['OrgNoGren'][data_index][-3:]),
                            'under13': data['Under13Gren'][data_index],
                            'over13': data['Over13Gren'][data_index]
                        }
                    })
            processed_data.update({current_org: org_data})
        return processed_data

    # Process product details from federation and concat to main data set
    def Process_NKF_Products(self, data, details, gren_data):
        product_list = list(details['produkt'].values())
        for org in list(data.keys()):
            total_over13 = 0
            org_product_data = {'Forsikring': {}}
            for gren in list(data[org]['gren_data'].keys()):
                if data[org]['gren_data'][gren]['gren_num'] in list(gren_data.keys()):
                    product = gren_data[data[org]['gren_data'][gren]['gren_num']]
                else:
                    product = 'Fleridretter'
                total_over13 += data[org]['gren_data'][gren]['over13']
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
            # process productinfo for relevant sections in club
            for product in list(org_product_data.keys()):
                details_index = product_list.index(product)
                member_count = 0
                if product == 'Forsikring':
                    member_count = total_over13
                else:
                    member_count = org_product_data[product]['under13']+org_product_data[product]['over13']                
                amount = details['pris'][details_index] * member_count
                org_product_data[product].update({
                    'price': details['pris'][details_index],
                    'inv_date': details['fakturadato'][details_index],
                    'due_in': datetime.strptime(details['fakturadato'][details_index], '%d.%m.%y') + timedelta(days=details['forfallstid(dager)'][details_index]),
                    'item_num': details['Varenummer'][details_index],
                    'desc': details['Transaksjonsbeskrivelse'][details_index],
                    'dim': details['Kostnadsbærer'][details_index],
                    'count': member_count,
                    'total_amount': amount,
                    'account': details['Varenummer'][details_index]
                })
            data[org].update({'Products': org_product_data})
        return data