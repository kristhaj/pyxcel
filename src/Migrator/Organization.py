# Identify Organizational data for the relevant entities

class Organization:

    # Get data from specified organizations or from all
    def Get_Data(self, orgID, club_meta, sheet):
        print(f'Processing Club Info for:')
        print(f'{orgID}: {club_meta[0]}....')
        sheet['Name of club'].update({len(sheet['Name of club']): club_meta[0]})
        sheet['Offical name of club'].update({len(sheet['Offical name of club']): club_meta[0]})            
        sheet['NIF ClubID'].update({len(sheet['NIF ClubID']): orgID})
        print('All relevant Club Info Processed.\n')
        return sheet