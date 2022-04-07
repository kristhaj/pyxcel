# Load data from files

import pandas as pd

class Load:

    def Member_File(self, path, columns = None):
        df = pd.read_excel(path, sheet_name=0, usecols=columns)
        data = df.to_dict()
        print(f'Data successfully read from {path}')
        return data