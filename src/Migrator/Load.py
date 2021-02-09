# Load data frame from one, many or all files in a directory

import pandas as pd


class Load:

    # Read a single specified file
    def One(self, path):
        print(f'Loading Data Basis from {path.split("/")[-1]}')
        df = pd.read_csv(path, encoding='ISO-8859-1', sep=';', parse_dates=True, infer_datetime_format=True, dayfirst=True)
        data = df.to_dict()
        print(f'Finished Loading Data.\n-----')
        return data

    # Read many specified files
    def Many(self, paths):
        pass

    # Read all files in directory
    def All(self):
        pass