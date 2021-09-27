# Append seperate files into a single master file

import os
import time
import pandas as pd

class Appendinator:

    def __init__(self) -> None:
        #Get dir and destination from ENV vars
        self.data_dir = os.getenv("DATA_DIR")
        self.target_path = os.getenv("TARGET_PATH")
        self.format_path = os.getenv("FORMAT_PATH")
        self.kao_dir = os.getenv("KAO_DIR")
        self.kao_meta = os.getenv("KAO_META")

        #set start time for logging run time
        self.start_time = time.time()

    def Handle_OutputIDs(self, path):
        df = pd.read_excel(path, usecols="B,C", keep_default_na=False)
        org_output_id = {}
        for i in range(df.shape[0]):
            orgID = df.Orgid.values[i]
            outputID = df.outputID.values[i]
            if type(outputID) == int:
                org_output_id.update({orgID: outputID})
            else:
                org_output_id.update({orgID: orgID})
        return org_output_id



    # get person IDs from KA Output
    def Get_PersonIDs(self, dir):
        pid_dict = {}
        files = os.listdir(dir)
        files_handled = 0
        for file in files:
            path = dir + '/' + file
            print(f'Reading PersonIDs at {path} ...')
            #TODO: fix csv reading
            df = pd.read_csv(path, sep=",")

            for i in df.Id.values:
                index = i-1
                org = df.OrgId.values[index]
                row_pid_pairing = {index: [df.PersonId.values[index], df.FirstName.values[index] ,df.LastName.values[index]]}
                if org not in list(pid_dict.keys()):
                    pid_dict[org]= row_pid_pairing
                else:
                    pid_dict[org].update(row_pid_pairing)

            files_handled += 1
            print(f'Read personID from {files_handled} of {len(files)} clubs.\n')

        return pid_dict

    def Main(self):
        postKA = False
        if postKA:
            output_ID = self.Handle_OutputIDs(self.kao_meta)
            personIDs = self.Get_PersonIDs(self.kao_dir)
        df = pd.read_excel(self.format_path, sheet_name=None, skiprows=1, keep_default_na=False)
        print(f'Reading data from {self.data_dir} ...')
        files = os.listdir(self.data_dir)
        files_handled = 0
        # dict for logging missing personIDs, where keys are OrgID and values are indices
        missing_output = {}
        # dict for logging clubs and areas with bad data, to be printed at the end of run
        # format {clubID: {sheet: {column: [rows]}}}
        bad_data = {}
        for f in files:
            path = f'{self.data_dir}/'+f
            data = pd.read_excel(path, sheet_name=None, skiprows=1, keep_default_na=False)
            data['Membership'].columns.values[18] = 'Status'
            current_org = data['Member'].NIFOrgId.values[0]
            bad_data.update({current_org: {}})
            for key in list(data.keys()):
                bad_data_count = 0
                bad_data_locations= []
                last_row = 0
                for row in data[key].values:
                    val = row[0]
                    if val == '' or pd.isna(val):
                        break
                    else:
                        if key == 'Member':
                            # check for missing birthdates and log if True
                            if data[key]['Fødselsdato'][last_row] == '':
                                print(f'{current_org}: Bad Birthdate at {last_row}, {data[key]["Fødselsdato"][last_row]}')
                                bad_data_count += 1
                                bad_data_locations.append('Fødselsdato')
                            
                            # check if new membership and Training fee has valid product names
                            mem = data[key]['Kontingent navn'][last_row]
                            mem_list = list(data['Membership']['Navn på kontigent'].values)
                            if  mem not in mem_list:
                                for m_product in mem_list:
                                    if mem.lower().replace(' ', '') == m_product.lower().replace(' ', ''):
                                        data[key]['Kontingent navn'][last_row] = m_product
                                        break
                                print(f'{current_org}: Bad Membership at {last_row}, old product: "{mem}", new product: "{data[key]["Kontingent navn"][last_row]}"')
                            tf = data[key]['Treningsavgift navn'][last_row]
                            tf_list = list(data['Training fee']['Navn på Treningsvgift'].values)
                            if tf not in tf_list:
                                for t_product in tf_list:
                                    if tf.lower().replace(' ', '') == t_product.lower().replace(' ', ''):
                                        data[key]['Treningsavgift navn'][last_row] = t_product
                                        break
                                print(f'{current_org}: Bad Training Fee at {last_row}, old product: "{tf}", new product: "{data[key]["Treningsavgift navn"][last_row]}"')
                            if postKA:
                                # check for existance of output data for current org
                                if current_org in list(output_ID.keys()):
                                    oid = output_ID[current_org]
                                    if oid in list(personIDs.keys()):
                                        org_data = personIDs[oid]
                                        num_pid= len(org_data)
                                        # set PersonID for member if available in output file
                                        if last_row < num_pid:
                                            data[key]['NIF ID'][last_row] = org_data[last_row][0]
                                        #check for erronious last names, and attempt correction (based upon rules for last name in Folkereg.)
                                        lastname = data[key].Etternavn.values[last_row]
                                        lastname_count = len(lastname.split())
                                        real_lastname = org_data[last_row][2]
                                        real_firstname = org_data[last_row][1]
                                        if lastname_count > 1 and lastname != real_lastname:
                                            print(f'{current_org}: Bad name at {last_row}, old: {lastname}, new: {real_lastname}')
                                            data[key]['Fornavn- og middelnavn'].values[last_row] = real_firstname
                                            data[key].Etternavn.values[last_row] = real_lastname
                                            bad_data_count += 1
                                            bad_data_locations.append('Navn')
                                # log clubs without indentifiable output from KA
                                else:
                                    missing_output.update({current_org: last_row})
                        elif key == 'Training fee':
                            #set TF duration to 1 if missing
                            if data[key]['Varighet (putt inn heltall)'][last_row] == '':
                                 #print(f'{current_org}: Missing Duration for Training Fee at {last_row}')
                                data[key]['Varighet (putt inn heltall)'][last_row] = 1
                            # check for missing data values, and set to defaults if True
                            if data[key]['Automatisk fornybar'][last_row] == '':
                                data[key]['Automatisk fornybar'][last_row] = 'Ja'
                            if data[key]['Oppstartspakke'][last_row] == '':
                                data[key]['Oppstartspakke'][last_row] = 'Nei'
                            #check for invalid data types
                            if type(data[key]['Beløp i kroner'][last_row]) != int:
                                data[key]['Beløp i kroner'][last_row] = 0
                                bad_data_count += 1
                                bad_data_locations.append('TF Price')
                        elif key == 'Membership Category':
                            # check for missing age ranges, and set defaults if missing
                            if data[key]['Alder fra'][last_row] == '':
                                data[key]['Alder fra'][last_row] = 0
                            if data[key]['Alder til '][last_row] == '':
                                data[key]['Alder til '][last_row] = 0

                        elif key == 'Membership':
                            # check for missing data values, and set to defaults if True
                            if data[key]['Varighet (putt inn heltall)'][last_row] == '':
                                data[key]['Varighet (putt inn heltall)'][last_row] = 1
                            if data[key]['Automatisk fornybar'][last_row] == '':
                                data[key]['Automatisk fornybar'][last_row] = 'Ja'
                            if data[key]['Familiemedlem'][last_row] == '':
                                data[key]['Familiemedlem'][last_row] = 'Nei'
                            if data[key]['Status'][last_row] == '':
                                data[key]['Status'][last_row] = 'Active'
                            
                            # check for price that will not count at SR
                            if data[key]['Beløp i kroner'][last_row] < 50 or type(data[key]['Beløp i kroner'][last_row]) != int:
                                data[key]['Beløp i kroner'][last_row] = 50
                                bad_data_count += 1
                                bad_data_locations.append('Membership Price')

                        last_row += 1
                        if bad_data_count > 0:
                            bad_data[current_org].update({key: [bad_data_count, bad_data_locations]})
                
                real_data = data[key].iloc[:last_row]
                df[key] = df[key].append(real_data, ignore_index=True)
                #print( f'{key} Shapes: processed: {df[key].shape}, raw: {data[key].shape}')
            files_handled += 1
            print(f'Processed {files_handled} out of {len(files)} files.\n')
            
        print(f'---\nFinished Processing All Data\n===\n')
        if len(list(missing_output.keys())) >= 1:
            print(f'Missing  output for thise orgIDs: {missing_output}\n')
        print(f'Registered bad data at {bad_data}')
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
        print(f'Elapsed time: {time.time() - self.start_time}')
        pass






Appendinator().Main()