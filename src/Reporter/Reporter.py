import os
import datetime
import dateutil
from Load import Load
from Write import Write

class Reporter:

    def __init__(self):
        self.postal_data_path = os.getenv("POSTAL_DATA")
        self.data_path = os.getenv("MEMBERS")
        self.destination_path = os.getenv("DESTINATION_PATH")

    def Kommune(self):
        print('Generating rapport of members with Kommune')

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





Reporter().Kommune()