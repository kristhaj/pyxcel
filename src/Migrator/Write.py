# Write collated data to new file

import pandas as pd

class Write:


    # Write the collated and formated data to a new file
    def To_File(self, data_dict, dir):
        for club in data_dict:
            print(f'Writing Processed Data for {club} to File in directory "{dir}" ....')
            data = data_dict[club]
            # Create separate DataFrames for each sheet in the Migration Template
            df_member = pd.DataFrame.from_dict(data['Member'])
            df_membership = pd.DataFrame.from_dict(data['Membership'])
            df_membership_category = pd.DataFrame.from_dict(data['Membership Category'])
            df_teams = pd.DataFrame.from_dict(data['Teams'])
            df_training_fee = pd.DataFrame.from_dict(data['Training fee'])
            df_training_locations = pd.DataFrame.from_dict(data['Training Locations'])
            df_department = pd.DataFrame.from_dict(data['Department info'])
            df_club = pd.DataFrame.from_dict(data['Club info'])
            df_committees = pd.DataFrame.from_dict(data['Committees'])
            df_grens = pd.DataFrame.from_dict(data['Grens'])
            df_style = pd.DataFrame.from_dict(data['Style'])
            df_op_duration = pd.DataFrame.from_dict(data['Op - Duration type'])
            df_op_invoice = pd.DataFrame.from_dict(data['Op - Invoice Duration Type'])
            df_op_memcat = pd.DataFrame.from_dict(data['Op - Membership Category'])
            df_op_yn = pd.DataFrame.from_dict(data['Op - Yes_No'])
            df_op_gender = pd.DataFrame.from_dict(data['Op - Gender'])

            path = dir + data['Club info']['Name of club'][1] + ".xlsx"

            # create writer
            writer = pd.ExcelWriter(path, engine='xlsxwriter') # pylint: disable=abstract-class-instantiated

            # write each df to the respective sheet
            df_member.to_excel(writer, sheet_name='Member', index=False)
            df_membership.to_excel(writer, sheet_name='Membership', index=False)
            df_membership_category.to_excel(writer, sheet_name='Membership Category', index=False)
            df_teams.to_excel(writer, sheet_name='Teams', index=False)
            df_training_fee.to_excel(writer, sheet_name='Training fee', index=False)
            df_training_locations.to_excel(writer, sheet_name='Training Locations', index=False)
            df_department.to_excel(writer, sheet_name='Department info', index=False)
            df_club.to_excel(writer, sheet_name='Club info', index=False)
            df_committees.to_excel(writer, sheet_name='Committees', index=False)
            df_grens.to_excel(writer, sheet_name='Grens', index=False)
            df_style.to_excel(writer, sheet_name='Style', index=False)
            df_op_duration.to_excel(writer, sheet_name='Op - Duration type', index=False)
            df_op_invoice.to_excel(writer, sheet_name='Op - Invoice Duration Type', index=False)
            df_op_memcat.to_excel(writer, sheet_name='Op - Membership Category', index=False)
            df_op_yn.to_excel(writer, sheet_name='Op - Yes_No', index=False)
            df_op_gender.to_excel(writer, sheet_name='Op - Gender', index=False)




            # close writer and write to file
            try:
                writer.save()
                print(f'Migration Data was successfully written to {path} !\n---\n')
            except:
                print(f'Something went wrong while writing to file.....\n---')

    def Basis_To_File(self, data, dir):
        print ('Perparing Data Basis for Writing to Collated File....')
        df = pd.DataFrame()
        for key in list(data.keys()):

            # Make a dict of NifOrgID and row index for the current club
            org_dict = {'NifOrgID': {}}
            for index in list(data[key]['Etternavn'].keys()):
                org_dict['NifOrgID'].update({index: key})
            current_club_data = data[key]
            # Append column with NifOrgID to data basis of current club
            current_club_data.update(org_dict)

            # Add the NifOrgID of the current club as a column with the member data, for later differentiation
            temp_df = pd.DataFrame.from_dict(current_club_data)

            # Append the current clubs data to the bottom of the DataFrame
            df = df.append(temp_df)
        print('Done.')

        path = dir + 'combined_data_basis.xlsx'
        print(f'Writing Data Basis to Collated File to {path}...')
        with pd.ExcelWriter(path) as writer: # pylint: disable=abstract-class-instantiated
            df.to_excel(writer, index=False)

        print('Done.\n-----')