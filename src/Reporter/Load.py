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