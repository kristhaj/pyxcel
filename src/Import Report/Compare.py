# Compare two given files to catch discrepancies as a result from preparing the data for migration

import os
from Load import Load
from Write import Write

class Compare:

    def __init__(self):
        self.imported_file = os.getenv("MIGRATION_FILE")
        self.original_file = os.getenv("DATA_BASIS")


    # TODO: Compare two files
    def Two(self):
        # Relevant columns
        import_columns = "A,D,E,J,O:T"
        import_headers = ['NifOrgID', 'fistname', 'lastname', 'age', 'guardian1', 'g1_mobile', 'g1_email', 'guardian2', 'g2_mobile', 'g2_email']
        original_columns = ['Etternavn', 'Fornavn', 'Fødselsdato', 'Foresatt 1', 'Foresatt 1 epost', 'Foresatt 1 telefon', 'Foresatt 2', 'Foresatt 2 epost', 'Foresatt 2 telefon']
        identifier = 24811

        print(f'=====\nComparing {import_columns} for {identifier} in {self.imported_file}, to {original_columns} in {self.original_file}\n-----')
        # imported_data = Load.Import_File(self, self.imported_file, import_columns, import_headers, identifier)
        original_data = Load.Original_File(self, self.original_file, original_columns)
        
        pass


Compare().Two()