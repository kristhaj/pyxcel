# Divide a single large excel document into smaller individual ones

import pandas as pd

# Read master file
def Load_Master(path):

    df_master = pd.read_excel(path, sheet_name=0, usecols='B')
    return df_master


# Parse significant data from Data Frame into dict
def Parse_Keys(df):

    values = df.KlubbID.values
    identifiers = {}

    for i in values:
        if i not in list(identifiers.keys()):
            identifiers[i] = None
            print(f'Adding club ID: {i} as identifier.')
    
    print(f'\n------\nTotal clubs identified: {len(list(identifiers.keys()))}\nExpected: 95\n------\n')
    return identifiers


# Populate dict with row indices relevant to keys
def Populate_Indices(id, df):

    for key in list(id.keys()):
        indices = []
        current_index = 0
        # Row indices will be at -2 compared to row number in work book: starts at 0 and first row used as column names
        for val in df.KlubbID.values:
            if val == key:
                indices.append(current_index)
            current_index += 1
        id[key] = indices
    return id

# Iterate through keys and fetch data based on row indices
def Make_Files(meta, path):

    significant_values = list(meta.keys())
    df = pd.read_excel(path, sheet_name=0)

    print('Writing files...')
    for id in significant_values:
        df_filtered = df.loc[meta[id]]
        make_path = f'pyxcel/files/KA/Migration File_{id}_KA.xlsx'
        with pd.ExcelWriter(make_path, date_format='YYYY.MM.DD', datetime_format='YYYY.MM.DD') as writer:
            df_filtered.to_excel(writer, index=False)
    print('Done.')

# Do the thing
def Main():
    master_path = 'pyxcel/files/KA/h21_batch1'
    
    df_master = Load_Master(master_path)
    identifiers = Parse_Keys(df_master)
    meta_data = Populate_Indices(identifiers, df_master)
    Make_Files(meta_data, master_path)



Main()