# Load data basis, details and templates
import pandas as pd

class Load:

    # Read relevant columns in data basis from ISD
    def Data_Basis(self, path, columns):
        df = pd.read_excel(path, sheet_name=0, usecols=columns)

        data = df.to_dict()
        
        print(f'Data Basis successfully read from {path}')
        return data

    # Read client details provided by NKF and NIF
    def Client_Details(self, path):
        df = pd.read_excel(path, sheet_name=0)
        data = df.to_dict()
        print(f'Client Details successfully read from {path}')
        return data

    # Read product details provided by NKF
    def Product_Details(self, path):
        df = pd.read_excel(path, sheet_name=0)
        data = df.to_dict()
        print(f'Product Details successfully read from {path}')
        return data

    # Read template for final output
    def Template(self, path):
        df = pd.read_excel(path, sheet_name=0)
        data = df.to_dict()
        print(f'Template successfully read from {path}')
        return data