# do the thing
import os
from Load import Load
from Write import Write

class System_Check:

    def __init__(self):
        self.club_path = os.getenv("CLUB_PATH")
        self.system_path = os.getenv("SYSTEM_PATH")
        self.destination = os.getenv("DESTINATION_PATH")

    def System_Check(self):
        print('Checking member systems...')
        
        data = {
            'NifOrgID': {},
            'Klubbnavn': {},
            'Medlemssystem': {},
            'Buypass-avtale': {},
            'Styrets epost': {}
        }
        club_data = Load.File(self, self.club_path, ['Klubbnavn', 'NIFOrgID'])
        system_data = Load.File(self, self.system_path, ['Idrettslag', 'Medlemssystem', 'BuyPass-status', 'id', '@'])

        print('Files have been loaded.\n Proceeding to process data...')

        # Process data based upon NifORgID
        i = 0
        for org in list(club_data['NIFOrgID'].values()):
            if org in list(system_data['id'].values()):
                row = list(system_data['id'].values()).index(org)
                data['NifOrgID'].update({i: system_data['id'][row]})
                data['Klubbnavn'].update({i: system_data['Idrettslag'][row]})
                data['Medlemssystem'].update({i: system_data['Medlemssystem'][row]})
                data['Buypass-avtale'].update({i: system_data['BuyPass-status'][row]})
                data['Styrets epost'].update({i: system_data['@'][row]})
            else:
                row = i
                data['NifOrgID'].update({i: club_data['NIFOrgID'][row]})
                data['Klubbnavn'].update({i: club_data['Klubbnavn'][row]})
                data['Medlemssystem'].update({i: ''})
                data['Buypass-avtale'].update({i: ''})
                data['Styrets epost'].update({i: ''})
            i += 1

        print(f'Data has been processed for {i+1} clubs.\nWriting to file...')

        Write.NTN(self, self.destination, data)

System_Check().System_Check()