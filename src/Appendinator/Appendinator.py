# Append seperate files into a single master file

import os
import pandas as pd

class Appendinator:

    def __init__(self) -> None:
        #Get dir and destination from ENV vars
        self.data_dir = os.getenv("DATA_DIR")
        self.target_path = os.getenv("TARGET_PATH")
        self.format_path = os.getenv("FORMAT_PATH")

    def Main(self):

        df = pd.read_excel(self.format_path, sheet_name=None, skiprows=1, keep_default_na=False)
        print(f'Reading data from {self.data_dir} ...')
        files = os.listdir(self.data_dir)
        files_handled = 0
        for f in files:
            path = f'{self.data_dir}/'+f
            data = pd.read_excel(path, sheet_name=None, skiprows=1, keep_default_na=False)
            #d_shape = data.shape
            for key in list(data.keys()):
                last_row = 0
                for row in data[key].values:
                    val = row[0]
                    #if key == 'Club info' or key == 'Grens':
                        #print('data?')
                    if val == '' or pd.isna(val):
                        break
                    else:
                        last_row += 1
                
                real_data = data[key].iloc[:last_row]
                df[key] = df[key].append(real_data, ignore_index=True)
                print( f'{key} Shapes: processed: {df[key].shape}, raw: {data[key].shape}')
            files_handled += 1
            print(f'\nProcessed {files_handled} out of {len(files)} files.\n---\n')
            
        print(f'Finished Processing All Data\n===\n')

        print(f'Writing data to target: {self.target_path} ...')
        # Write the collated and formated data to a new file
        # Create separate DataFrames for each sheet in the Migration Template
        df_member = pd.DataFrame.from_dict(df['Member'])
        df_membership = pd.DataFrame.from_dict(df['Membership'])
        df_membership_category = pd.DataFrame.from_dict(df['Membership Category'])
        df_teams = pd.DataFrame.from_dict(df['Teams'])
        df_training_fee = pd.DataFrame.from_dict(df['Training fee'])
        df_training_locations = pd.DataFrame.from_dict(df['Training locations'])
        df_department = pd.DataFrame.from_dict(df['Department info'])
        df_club = pd.DataFrame.from_dict(df['Club info'])
        df_committees = pd.DataFrame.from_dict(df['Committees'])
        df_grens = pd.DataFrame.from_dict(df['Grens'])
        df_style = pd.DataFrame.from_dict(df['Style'])
        df_op_duration = pd.DataFrame.from_dict(df['Op - Duration type'])
        df_op_invoice = pd.DataFrame.from_dict(df['Op - Invoice Duration Type'])
        df_op_memcat = pd.DataFrame.from_dict(df['Op - Membership Category'])
        df_op_yn = pd.DataFrame.from_dict(df['Op - Yes_No'])
        df_op_gender = pd.DataFrame.from_dict(df['Op - Gender'])

        # create writer
        writer = pd.ExcelWriter(self.target_path, engine='xlsxwriter', date_format='YYYY.MM.DD', datetime_format='YYYY.MM.DD') # pylint: disable=abstract-class-instantiated

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
            print(f'Migration Data was successfully written to {self.target_path} !\n---\n')
        except:
            print(f'Something went wrong while writing to file.....\n---')

        print('DONE')
        pass






Appendinator().Main()