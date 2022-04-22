import os
import datetime
import dateutil
from Load import Load
from Write import Write
from Counter import Counter
from Processor import Processor
from Formatter import Formatter
from Teams_Counter import Teams_Counter
from Findim import Findim

class Reporter:

    def __init__(self):
        self.postal_data_path = os.getenv("POSTAL_DATA")
        self.data_path = os.getenv("MEMBERS")
        self.destination_path = os.getenv("DESTINATION_PATH")
        self.invoice_path = os.getenv("INVOICE_PATH")
        self.members_path = os.getenv("ALL_MEMBERS")
        self.paid_members_template = os.getenv("PAID_MEMBERS_TEMPLATE")
        self.training_fees_path = os.getenv("TRAINING_FEES")
        self.team_path = os.getenv("TEAMS_PATH")
        self.findim_path = os.getenv("FINDIM_PATH")

    def Kommune(self):
        print('Generating report of members with Kommune')

        postal_cols = ['Postnummer', 'Kommune']
        members_cols = ['PersonID', 'FirstName', 'LastName', 'BirthDate', 'Gender', 'PostalCode', 'LastPaidDate', 'MembershipStatus']

        postal_data = Load.Kommuner(self, self.postal_data_path, postal_cols)
        member_data = Load.Members(self, self.data_path, members_cols)

        check_date = datetime.datetime(2020, 12, 31)
        print(f'Calculating ages per {check_date}...')
        member_data.update({'Age': {} })
        for key in list(member_data['PersonID'].keys()):
            time_diff = dateutil.relativedelta.relativedelta(check_date, member_data['BirthDate'][key])
            member_data['Age'].update({key: time_diff.years})
            
        print('Add Kommune data...')
        member_data.update({'Kommune': {} })
        for key in list(member_data['PostalCode'].keys()):
            postal_code = member_data['PostalCode'][key]
            if str(postal_code) == 'nan':
                member_data['Kommune'].update({key: 'Mangler postnummer'})
            else:
                postal_code = int(postal_code)
                try:
                    member_data['Kommune'].update({key: postal_data[postal_code]})
                except:
                    member_data['Kommune'].update({key: 'Mangler postnummer'})

        Write.Kommune_Rapport(self, self.destination_path, member_data)


    def Paid(self):
        print('\nGenerating report of members per given year, with payment status\n')

        invoicing_cols = ['PersonId', 'Medlemsnavn', 'Fakturanummer', 'Fakturadato', 'Fakturabeløp', 'Status', 'Produkt']
        member_cols = ['NIF nummer', 'Navn', 'År', 'Kjønn']
        
        

        invoicing_data = Load.Invoices(self, self.invoice_path, invoicing_cols)
        member_data = Load.All_Members(self, self.members_path, member_cols)

        paid_member_template = Load.Paid_Members_Template(self, self.paid_members_template)

        print('All Data Loaded.\nProceeding with processing...\n')

        processed_data = Processor.Process_Paid_Memberships(self, invoicing_data, member_data)

        if self.training_fees_path != "N/A":
            tf_columns = ['Person ID', 'Navn treningsavgift']
            training_fees = Load.Training_Fees(self, self.training_fees_path, tf_columns)
            print("\nGetting Departments from Training Fees...\n")
            processed_data = Processor.Process_Department_From_Training_Fee(self, processed_data, training_fees)
        else:
            processed_data['Department'].update({0: False})

        if self.team_path != "N/A":
            team_cols = ['Partinavn', 'Parti oppstartsdato', 'Parti sluttdato', 'PersonID', 'Partimedlem status', 'Partimedlem faktura status']
            teams = Load.Teams(self, self.team_path, team_cols)
            print('\nProcessing teams data per member...')
            processed_data = Processor.Process_Team_Data(self, processed_data, teams)
        else:
            processed_data['Team'].update({0: False})

        if self.findim_path != "N/A":
            findim_map = Load.Findims(self, self.findim_path)
            print('Processing findim data...')
            processed_data = Findim.Map_Findim(self, processed_data, findim_map)
        else:
            processed_data['Findim'].update({0: False})

        print('\nData Processing complete.\nGenerating Report...\n')

        report = Counter.Report_Generator(self, processed_data)
        if self.team_path != "N/A":
            print('Teams data detected, counting paid member data per team')
            report = Teams_Counter.Participation_Counter(self, processed_data, report)

        print(f'\nReport has been Generated.\nProceeding to format the data according to {self.paid_members_template}...')

        formatted_report = Formatter.Paid_Member_Formatting(self, paid_member_template, report)

        if self.team_path != "N/A":
            if self.findim_path != "N/A":
                formatted_report = Formatter.Team_Statistics_formatting(self, report, formatted_report, True)
            else:
                formatted_report = Formatter.Team_Statistics_formatting(self, report, formatted_report)

        print('\nFormatting complete.\nProceeding to Write...\n')

        Write.Paid_Members_Report(self, self.destination_path, processed_data, formatted_report)


Reporter().Paid()