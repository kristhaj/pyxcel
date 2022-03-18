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
            'Department': {},
            'Team': {}
            }

        #iterate through invoices and find matching members, finally add relevant data to processed_data
        for i in list(invoicing_data['PersonId'].keys()):
            if invoicing_data['PersonId'][i] in list(processed_data['PersonID'].values()):
                print(f'More than one membership invoice for {invoicing_data["PersonId"][i]} at {i} with status {invoicing_data["Status"][i]}')
                if invoicing_data['Status'][i] == 'Betalt':
                    if invoicing_data['Fakturabeløp'][i] >= 50:
                        processed_data['HasPaid'].update({i: True})
                    else:
                        print(f'{invoicing_data["PersonId"][i]}, {invoicing_data["Medlemsnavn"][i]}: Ammount for {invoicing_data["Fakturanummer"][i]} is not sufficient to count as paying member, at {invoicing_data["Fakturabeløp"][i]}')
            else:
                processed_data['PersonID'].update({i: invoicing_data['PersonId'][i]})
                processed_data['Name'].update({i: invoicing_data['Medlemsnavn'][i]})
                processed_data['InvoiceNum'].update({i: invoicing_data['Fakturanummer'][i]})
                processed_data['Product'].update({i: invoicing_data['Produkt'][i]})
                processed_data['IsInvoicedOn'].update({i: invoicing_data['Fakturadato'][i]})
                if invoicing_data['Status'][i] == 'Betalt':
                    if invoicing_data['Fakturabeløp'][i] >= 50:
                        processed_data['HasPaid'].update({i: True})
                    else:
                        print(f'{invoicing_data["PersonId"][i]}, {invoicing_data["Medlemsnavn"][i]}: Ammount for {invoicing_data["Fakturanummer"][i]} is not sufficient to count as paying member, at {invoicing_data["Fakturabeløp"][i]}')
                        processed_data['HasPaid'].update({i: False})
                else:
                    processed_data['HasPaid'].update({i: False})
                processed_data['PaymentStatus'].update({i: invoicing_data['Status'][i]})
                processed_data['Amount'].update({i: invoicing_data['Fakturabeløp'][i]})

            #find index in member_data of current PersonID
            member_personIDs = list(member_data['NIF nummer'].values())
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

    def Process_Team_Data(self, data, teams):
        team_personIDs = list(teams['PersonID'].values())
        for i in list(data['PersonID'].keys()):
            p = data['PersonID'][i]
            # Check for person merge
            if data['Gender'][i] == 'PersonMerge':
                data['Team'].update({i: 'PersonMerge'})
                print('Cannot apply Teams to PersonMerge entity')
            # Process participation in multiple teams
            participating_teams = ''
            for team_key in range(0, len(team_personIDs)):
                participant = team_personIDs[team_key]
                if data['PersonID'][i] == participant:
                    # check if string is empty, and handle multiple registrations to the same team
                    if participating_teams != '':
                        if teams["Partinavn"][team_key] in participating_teams:
                            print(f'{data["PersonID"][i]}, {data["Name"][i]}: duplicate registration for {teams["Partinavn"][team_key]}')
                        else:
                            participating_teams += f'|{teams["Partinavn"][team_key]}'
                    else:
                        participating_teams = teams["Partinavn"][team_key]
            if data['PersonID'][i] in team_personIDs:
                    team_key = team_personIDs.index(participant)
                    data['Team'].update({i: participating_teams})
            else:
                print(f'{data["PersonID"][i]}, {data["Name"][i]}: Could not find Team participation in 2021 for this personID')
                data['Team'].update({i: 'Unknown'})

        return data