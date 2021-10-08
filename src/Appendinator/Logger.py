class Logger:

    def Log(self, missing_output, bad_data):

        if len(list(missing_output.keys())) >= 1:
            print(f'Missing  output for thise orgIDs: {missing_output}\n')
            for org in list(missing_output.keys()):
                print(f'{org}:')
                for sheet in list(org.keys()):
                    print(f'Missing data in {sheet}: \n Total: {sheet[0]} \n Locations: {sheet[1]} \n ---')
        print(f'Registered bad data at {bad_data}')
        for org in list(bad_data.keys()):
            for sheet in list(bad_data[org].keys()):
                print(f'Bad data for {org} in sheet {sheet}\n Total count: {bad_data[sheet][0]} \n Data Point \t Bad Data Count\n-------------------')
                for col in list(bad_data[sheet][1].keys()):
                    print(f'{col}\t{bad_data[sheet][1][col]}')