# Calculate and format importable data for Federation invoicing in the given Visma format

import os
from Load import Load
from Processor import Processor
from Formatter import Formatter
from Write import Write
from Delta import Delta


class Vispy:


    def __init__(self):
        self.data_dir = os.getenv("DATA_DIR")
        self.old_data_path = os.getenv("OLD_DATA_PATH")
        self.new_data_path = os.getenv("NEW_DATA_PATH")
        self.client_path = os.getenv("CLIENT_DETAILS_PATH")
        self.product_path = os.getenv("PRODUCT_DETAILS_PATH")
        self.template_path = os.getenv("TEMPLATE_PATH")
        self.destination_path = os.getenv("DESTINATION_PATH")

    # do the thing
    def Vispy(self):
        print('Vispy will process data for federation level invoicing.\n')

        # overview of grens and codes, related to products
        gren_data = {
            521: 'Karate',
            843: 'Karate',
            844: 'Karate',
            522: 'Taekwondo WT',
            845: 'Taekwondo WT',
            846: 'Taekwondo WT',
            523: 'Jujutsu',
            524: 'Taekwondo ITF'
        }
        # set relevant columns
        data_columns = ['OrgIdClub', 'ClubName', 'OrgIdGroup', 'GroupName', 'OrgIdGren', 'OrgNoGren', 'GrenName', 'Under13Gren', 'Over13Gren']

        # Load necessary data
        print('Reading files....')
        data = Load.Data_Basis(self, self.old_data_path, data_columns)
        if self.new_data_path.split('/')[-1] in os.listdir(self.data_dir):
            new_data = Load.Data_Basis(self, self.new_data_path, data_columns)
        else:
            new_data = False
        client_details = Load.Client_Details(self, self.client_path)
        product_details = Load.Product_Details(self, self.product_path)
        template = Load.Template(self, self.template_path)

        print('All files have been read.\nProceeding with data processing...\n')

        #Calculate delta
        if new_data:
            delta = Delta.Get_Delta(self, data, new_data)
            # Process data
            processed_data = Processor.Process_Clients(self, delta, client_details)
            processed_data = Processor.Process_NKF_Products(self, processed_data, product_details, gren_data)
        else:
            # Process data
            processed_data = Processor.Process_Clients(self, data, client_details)
            processed_data = Processor.Process_NKF_Products(self, processed_data, product_details, gren_data)
        print('All client and product data has been processed!\n Proceeding to format data based upon given template...\n')

        # Format data
        formatted_data = Formatter.Visma_Format(self, processed_data, template)

        print(f'Data processing and formatting is complete!\n Proceeding to Write output to {self.destination_path}...')
        # Write data
        Write.Visma_Format(self, self.destination_path, formatted_data)



Vispy().Vispy()