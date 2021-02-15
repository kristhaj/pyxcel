# Compare two given files to catch discrepancies as a result from preparing the data for migration

import os
from Load import Load
from Write import Write
from Calculate import Calculate

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

        print(f'=====\nComparing columns {import_columns} for {identifier} \nin {self.imported_file}, \nto columns {original_columns} \nin {self.original_file}\n-----')
        imported_data = Load.Import_File(self, self.imported_file, import_columns, import_headers, identifier)
        original_data = Load.Original_File(self, self.original_file, original_columns)

        # Calculate the relevant data deviation
        # TODO: Review proper formatting
        deviating_data = Calculate.Guardian_Discrepancy(self, imported_data, original_data)


        pass
                            



Compare().Two()