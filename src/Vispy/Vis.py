# Calculate and format importable data for Federation invoicing in the given Visma format

import os
from Load import Load
from Processor import Processor
from Formatter import Formatter
from Write import Write


class Vispy:


    def __init__(self):
        self.data_path = os.getenv("DATA_PATH")
        self.client_path = os.getenv("CLIENT_DETAILS_PATH")
        self.product_path = os.getenv("PRODUCT_DETAILS_PATH")
        self.template_path = os.getenv("TEMPLATE_PATH")
        self.destination_path = os.getenv("DESTINATION_PATH")

    # do the thing
    def Vispy(self):

        # set relevant columns
        data_columns = []
        
        # Load necessary data
        data = Load.Data_Basis(self, self.data_path, data_columns)
        client_details = Load.Client_Details(self, self.client_path)
        product_details = Load.Product_Details(self, self.product_path)
        template = Load.Template(self, self.template_path)

        # Process data
        data = Processor.Process_Clients(self, data, client_details)
        data = Processor.Process_Products(self, data, product_details)

        # Format data
        data = Formatter.Visma_Format(self, data, template)


        # Write data
        Write.Visma_Format(self, self.destination_path, data)



Vispy.Vispy()