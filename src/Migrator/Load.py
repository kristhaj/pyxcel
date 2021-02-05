# Load data frame from one, many or all files in a directory

import pandas as pd


class Load:

    # Read a single specified file
    def One(self, path):
        # TODO: fix encoding error (can't read utf-8)
        df = pd.read_csv(path, parse_dates=True, infer_datetime_format=True, dayfirst=True)
        
        return None

    # Read many specified files
    def Many(self, paths):
        pass

    # Read all files in directory
    def All(self):
        pass