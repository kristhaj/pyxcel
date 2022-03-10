import pandas as pd

class Load:

    def Members(self, path, columns):
        print(f'Loading member data from {path}')

        df = pd.read_excel(path, usecols=columns, parse_dates=True)
        data = df.to_dict()

        ('Formatting birthdates...')
        for key in list(data['BirthDate'].keys()):
            data['BirthDate'][key] = data['BirthDate'][key].to_pydatetime()
        print('Done.')
        return data


    def Kommuner(self, path, columns):
        print('Loading postal data...')

        df = pd.read_excel(path, sheet_name="Sheet1", usecols=columns)
        data = {}

        print('Formatting data...')
        for i in range(0, len(df)):
            data.update({df.Postnummer[i]: df.Kommune[i]})

        print('Done.\n')
        return data

    def Invoices(self, path, columns):
        print(f'Loading Invoicing Data from {path}....')

        df = pd.read_excel(path, sheet_name="membership_invoicing", usecols=columns)
        data = df.to_dict()

        print('Done, and converted to dictionary.')
        return data

    def All_Members(self, path, columns):
        print(f'Loading ALL members from {path}...')

        df = pd.read_excel(path, sheet_name="all_members", usecols=columns)
        data = df.to_dict()

        print('Done, and converted to dictionary.\n')
        return data

    def Paid_Members_Template(self, path):
        print(f'Loading SA template from {path}...')

        df = pd.read_excel(path)

        print('Done.')
        return df

    def Training_Fees(self, path, columns):
        print(f'\nLoading Training Fees from {path}...')

        df = pd.read_excel(path, usecols=columns)
        data = df.to_dict()

        print('Done.')
        return data