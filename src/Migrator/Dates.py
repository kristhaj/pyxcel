# Set start, end, and invoicing dates for all members and relevant products



class Dates:


    def Set_Membership_Dates(self, start, end, invoice, sheet):
        print(f'\n---\nApplying given Dates to Membership Start ( {start} ), End ( {end} ) and Invoiceing Dates ( {invoice} )....')
        for key in list(sheet['NIFOrgId'].keys()):
            sheet['Membership start date'].update({key: start})
            sheet['Membership end date'].update({key: end})
            sheet['Membership next invoice date'].update({key: invoice})
            
        print('Membership Dates have been applied to all Processed Members.\n')

        return sheet


    def Set_Training_Dates(self, start, end, invoice, sheet):
        print(f'Applying given Dates to Training Start ( {start} ), End ( {end} ) and Invoiceing Dates ( {invoice} )....')
        for key in list(sheet['NIFOrgId'].keys()):
            sheet['Traning fee start date'].update({key: start})
            sheet['Traning fee end date'].update({key: end})
            sheet['Traning fee next invoice date'].update({key: invoice})
            
        print('Training Dates have been applied to all Processed Members.\n---\n')
        return sheet