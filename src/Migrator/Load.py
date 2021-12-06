# Load data frame from one, many or all files in a directory

import pandas as pd


class Load:

    # Read a single specified file
    def One(self, _dir, meta):
        print(f'Loading Data Basis from {meta[list(meta.keys())[0]][1]}')
        path = _dir + meta[list(meta.keys())[0]][1]
        df = pd.read_csv(path, encoding='utf-8', sep=';', parse_dates=True, infer_datetime_format=True, dayfirst=True)
        data = {list(meta.keys())[0]: df.to_dict()}
        print(f'Finished Loading Data.\n-----')
        return data

    # TODO:Read many specified files
    def Many(self, dir, meta):
        print(f'Loading Data Basis from {len(list(meta.keys()))} clubs...')
        data = {}
        for key in list(meta.keys()):
            if type(key) != int:
                print(f'Missing, or no available, Org Data for {meta[key]}. NO DATA WILL BE READ')
            else:
                path = dir + meta[key][1]
                df = pd.read_csv(path, encoding='unicode_escape', sep=';', parse_dates=True, infer_datetime_format=True, dayfirst=True)
                data.update({key: df.to_dict()})
        print(f'Finished Loading Data.\n-----')
        return data

    def Template(self, path):
        print(f'Loading Migration Template from {path} ...')
        df = pd.read_excel(path, sheet_name=None)
        data = {}
        # Make template dictionary of dictionaries where template.keys() would return the sheet names
        sheets = list(df.keys())
        for key in sheets:
            data.update({key: df[key].to_dict()})
        print(f'Finished loading Template.\n-----')
        return data