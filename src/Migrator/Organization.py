# Identify Organizational data for the relevant entities

class Organization:

    # Get data from specified organizations or from all
    def Get_Data(self, data, sheet):
        print(f'Processing Club Info for:')
        for key in list(data.keys()):
            print(f'{data[key][0]}....')
            sheet['Name of club'].update({len(sheet['Name of club']): data[key][0]})
            sheet['Offical name of club'].update({len(sheet['Offical name of club']): data[key][0]})
            sheet['NIF ClubID'].update({len(sheet['NIF ClubID']): key})
        print('All relevant Club Info Processed.\n===')
        return sheet