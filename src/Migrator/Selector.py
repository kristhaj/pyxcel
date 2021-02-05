# Read metadata to select clubs to migrate

import pandas as pd

class Selector:


    # Select meta data to handle based upon given identifier
    # identifier has to be org ID or official name
    def Select(self, path, identifier, category):
        print(f'Reading Meta Data for {identifier}...')
        df_meta = pd.read_excel(path, sheet_name=category, usecols="A:C", keep_default_na=False)
        converted_meta = df_meta.to_dict()
        relevant_meta = None
        if type(identifier) == int:
            for key in converted_meta['NifOrgID']:
                if converted_meta['NifOrgID'][key] == identifier:
                    relevant_meta = {converted_meta['NifOrgID'][key]: [converted_meta['official_name'][key], converted_meta['file_path'][key]]}
        else:
            for key in converted_meta['official_name']:
                if converted_meta['official_name'][key].replace(' ', '').lower() == identifier.replace(' ', '').lower():
                    relevant_meta = {converted_meta['NifOrgID'][key]: [converted_meta['official_name'][key], converted_meta['file_path'][key]]}
        return relevant_meta

    # Select meta data to handle based upon given identifies
    def Select_Many(self, path, identifiers, category):
        print(f'Reading Meta Data for {len(identifiers)} clubs...')
        df_meta = pd.read_excel(path, sheet_name=category, usecols="A:C", keep_default_na=False)
        converted_meta = df_meta.to_dict()
        relevant_meta = {}
        for ID in identifiers:
            if type(ID) == int:
                for key in converted_meta['NifOrgID']:
                    if converted_meta['NifOrgID'][key] == ID:
                        relevant_meta = {converted_meta['NifOrgID'][key]: [converted_meta['official_name'][key], converted_meta['file_path'][key]]}
            else:
                for key in converted_meta['official_name']:
                    if converted_meta['official_name'][key].replace(' ', '').lower() == ID.replace(' ', '').lower():
                        relevant_meta.update({converted_meta['NifOrgID'][key]: [converted_meta['official_name'][key], converted_meta['file_path'][key]]})
            return relevant_meta

    # TODO:Select meta data for given row indexes
    def Select_Rows(self, path, identifiers, category):
        pass