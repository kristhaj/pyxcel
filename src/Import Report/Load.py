# Read specified files

import pandas as pd

class Load:

    # TODO: Read the specified data in a given .xlsx file
    def Import_File(self, path, columns, headers, identifier = None):
        print(f'Reading relevant data from {path}...')

        # Skip all rows before relevant club, and set amount of rows for the club
        # TODO: handle rows based upon identifier
        df = pd.read_excel(path, sheet_name='Member', usecols=columns, parse_dates=True, names=headers, skiprows=13399, nrows=1071)
        data = df.to_dict()

        print('Done.\n---')
        return data

    # TODO: Read the relevant data from original file
    def Original_File(self, path, columns):
        print(f'Reading relevant data from {path}...')

        df = pd.read_csv(path, encoding='utf-8', sep=';', usecols=columns, parse_dates=True, infer_datetime_format=True, dayfirst=True)
        data = df.to_dict()

        print('Done.\n---')
        return data