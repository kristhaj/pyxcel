# Write collated data to new file

import pandas as pd

class Write:


    # Write the collated and formated data to a new file
    def To_File(self, data, dir):
        print(f'Writing Processed Data to File in directory "{dir}" ....')

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

        path = dir + 'testing_invoiceless.xlsx'

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
        



    # Final formatting of complete file before writing
    def Format(self, data):
        pass