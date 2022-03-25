# Load data
import pandas as pd

class Load:

    def File(self, path, columns):

        df = pd.read_excel(path, usecols=columns)

        data =df.to_dict()

        return data