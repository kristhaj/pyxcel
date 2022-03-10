class Processor:

    def Process_Paid_Memberships(self, invoicing_data, member_data):
        processed_data = {
            'PersonID': {},
            'Name': {}, 
            'Age': {}, 
            'Gender': {},
            'InvoiceNum': {}, 
            'Product': {},
            'IsInvoicedOn': {}, 
            'HasPaid': {},
            'PaymentStatus': {},
            'Amount': {},
            'Department': {}
            }

        #iterate through invoices and find matching members, finally add relevant data to processed_data
        for i in list(invoicing_data['PersonId'].keys()):
            if invoicing_data['PersonId'][i] in list(processed_data['PersonID'].values()):
                print(f'More than one membership invoice for {invoicing_data["PersonId"][i]} at {i} with status {invoicing_data["Status"][i]}')
                if invoicing_data['Status'][i] == 'Betalt':
                    processed_data['HasPaid'].update({i: True})
            else:
                processed_data['PersonID'].update({i: invoicing_data['PersonId'][i]})
                processed_data['Name'].update({i: invoicing_data['Medlemsnavn'][i]})
                processed_data['InvoiceNum'].update({i: invoicing_data['Fakturanummer'][i]})
                processed_data['Product'].update({i: invoicing_data['Produkt'][i]})
                processed_data['IsInvoicedOn'].update({i: invoicing_data['Fakturadato'][i]})
                if invoicing_data['Status'][i] == 'Betalt':
                    processed_data['HasPaid'].update({i: True})
                else:
                    processed_data['HasPaid'].update({i: False})
                processed_data['PaymentStatus'].update({i: invoicing_data['Status'][i]})
                processed_data['Amount'].update({i: invoicing_data['Fakturabeløp'][i]})

            #find index in member_data of current PersonID
            member_personIDs = list(member_data['PersonID'].values())
            try:
                member_key = member_personIDs.index(invoicing_data['PersonId'][i])
                processed_data['Age'].update({i: member_data['År'][member_key]})
                processed_data['Gender'].update({i: member_data['Kjønn'][member_key]})
            except:
                print(f'Person merge detected for PersonID: {invoicing_data["PersonId"][i]}\n')
                processed_data['Age'].update({i: 999})
                processed_data['Gender'].update({i: 'PersonMerge'})

        return processed_data

    def Process_Department_From_Training_Fee(self, data, training_fees):
        tf_personIDs = list(training_fees['Person ID'].values())
        for i in list(data['PersonID'].keys()):
            # Check for person merge
            if data['Gender'][i] == 'PersonMerge':
                data['Department'].update({i: 'PersonMerge'})
                print('Cannot apply department to PersonMerge entity')
            if data['PersonID'][i] in tf_personIDs:
                department_key = tf_personIDs.index(data['PersonID'][i])
                training_fee = training_fees['Navn treningsavgift'][department_key]
                # check if training fee not empty.
                if type(training_fee) == str:
                    # Get suffixed department  
                    department = training_fee.split(' ')[0]
                    # Handle affixed departments
                    if department in ['6', '12', 'Barn']:
                        department = training_fee.split(' ')[-1]
                    data['Department'].update({i: department})
                else:
                    data['Department'].update({i: 'Unknown'})
                    print(f'{data["PersonID"][i]}, {data["Name"][i]}: Product name missing from export or not set.')
            else:
                print(f'{data["PersonID"][i]}, {data["Name"][i]}: Has, or have had, no Active or Cancelled Training Fee')
                data['Department'].update({i: 'Unknown'})
        return data