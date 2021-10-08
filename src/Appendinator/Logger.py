class Logger:

    def Log(self, missing_output, bad_data):

        if len(list(missing_output.keys())) >= 1:
            print(f'Missing  output for thise orgIDs: {missing_output}\n')
            for org in list(missing_output.keys()):
                print(f'{org}:')
                for sheet in list(org.keys()):
                    print(f'Missing data in {sheet}:\nTotal: {sheet[0]}\nLocations: {sheet[1]}\n ---')
        print(f'Registered bad data at {bad_data}')
        for org in list(bad_data.keys()):
            for sheet in list(bad_data[org].keys()):
                print(f'---\nBad data for {org} in sheet {sheet}\nTotal count: {bad_data[org][sheet][0]}\n\nData Point\t|\t\t\tBad Data Count\n--------------------------------------------------')
                for col in list(bad_data[org][sheet][1].keys()):
                    print(f'{col}\t|\t\t\t{bad_data[org][sheet][1][col]}')