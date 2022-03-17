# Format the processed data based on the given template

class Formatter:


    # Format data into Visma importable format
    def Visma_Format(self, data, template):
        row = 0
        for org in list(data.keys()):
            for product in list(data[org]['Products'].keys()):
                # set client info
                template['Kundenummer'].update({row: data[org]['client_num']})
                template['Kundenavn'].update({row: data[org]['name']})
                template['Kundens ref'].update({row: data[org]['client_ref']})
                template['Ekstern ref'].update({row: data[org]['ext_ref']})
                # set product info
                template['Bilagsdato'].update({row: data[org]['Products'][product]['inv_date']})
                template['Forfallsdato'].update({row: data[org]['Products'][product]['due_in']})
                template['Fakturatekst'].update({row: 'Faktura'})
                template['Varenr'].update({row: data[org]['Products'][product]['item_num']})
                template['Transaksjonsbeskrivelse'].update({row: data[org]['Products'][product]['desc']})
                template['Kostnadsbærer'].update({row: data[org]['Products'][product]['dim']})
                template['Antall'].update({row: data[org]['Products'][product]['count']})
                template['Pris pr stk'].update({row: data[org]['Products'][product]['price']})
                template['total'].update({row: data[org]['Products'][product]['total_amount']})
                template['Kontonr'].update({row: data[org]['Products'][product]['account']})

                # keep track of row number
                row += 1


        return template
