# Use in order to fetch actual member data for migration, submited via google forms and compared to existing member data
# requires pandas and xlrd packages
# install these with: "pip/pip3 install [package name]"

import pandas as pd

#read excel-file, and store relevant values
def Load_Names(path):
    
    # usecol arg refers to column header of relevant data in input file
    # fetch full name of submited members from given column
    df_full_name_new = pd.read_excel(path, index_col=None, usecols="BB").dropna()
    # fetch full name of existing members from given column
    df_full_name_old = pd.read_excel(path, index_col=None, usecols="AE").dropna()

    new= df_full_name_new.T.values[0]
    old= df_full_name_old.T.values[0]

    return new, old



#make lists compareable
def Trim_Name_List(new, old):

    trimmed_names = []
    trimmed_old_names = []

    #make elements lowercase and remove whitespace
    for n in new:
        name = n.lower()
        trimmed_names.append(name.replace(" ", ""))
    for on in old:
        name = on.lower()
        trimmed_old_names.append(name.replace(" ", ""))

    return trimmed_names, trimmed_old_names
    
#compare the lists
def Compare_Lists(new, new_trimmed, old_trimmed):
    
    actual_new_members = {}
    current_index = 0

    for i in new_trimmed:
        #selects submited names that are not already members, and skips duplicate entries
        if i not in old_trimmed and i not in actual_new_members:
            #populates dict with key == original index and values == full names as submited, with double spaces replaces with singular
            actual_new_members[current_index] = new[current_index].replace("  ", " ")
        current_index += 1

    print(f"new members submited count: {len(new)} \nactual new member count: {len(actual_new_members)}")

    return actual_new_members


#create a new dict with the migration relevant data from input file,
#in preparation on writing new file
def Compile_Relevant_Data(path, members_to_migrate):

     #fetch keys from members to migrate to use as values for header arg
    row_indices= list(members_to_migrate.keys())

    #read the relevant column headers from input file and manually enter into list
    #order the list in the order that the data will be input into the migration file
    #input headers as single string separated with comma
    #subsequent headers may be input as ranges, and are inclusive on both sides
    relevant_columns="F,G,J,K,H,I,P:T,L,M"

    #load the migration relevant data from input file, based upon relevant submited members
    df= pd.read_excel(path, usecols=relevant_columns)

    return df, row_indices

#write new file to use for member data in later migration
def Write_Sheet(DataFrame, indices):

    migration_df = DataFrame.loc[indices]

    print(migration_df)

    with pd.ExcelWriter('files/Migration_List_Unsorted.xlsx', date_format='YYYY-MM-DD', datetime_format='YYYY-MM-DD') as writer:
        migration_df.to_excel(writer)

def Main(path):

    new_names_list = []
    old_names_list = []

    #populates lists with data in given file
    new_names_list, old_names_list = Load_Names(path)

    new_compare = []
    old_compare = []

    #make comparable lists from base data
    new_compare, old_compare = Trim_Name_List(new_names_list, old_names_list)

    #make dict with row number in input file and full name of submited members that are actually new
    relevant_names = Compare_Lists(new_names_list, new_compare, old_compare)

    #make dict of the migration relevant data for new members, based upon the dict of new members, then write
    df, indices = Compile_Relevant_Data(path, relevant_names)
    Write_Sheet(df, indices)
    


#replace arg with path to input file with google form data and existing IMS member data
Main('files/medlemsdata.xlsx')