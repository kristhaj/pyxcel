class Counter:

    def Report_Generator(self, processed_data):

        report = {
            'Female': {
                'Paid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    },
                'Unpaid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    }
                },
            'Male': {
                'Paid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    },
                'Unpaid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    }
                },
             'Unspecified': {
                'Paid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    },
                'Unpaid': {
                    '0-5': 0,
                    '6-12': 0,
                    '13-19': 0,
                    '20-25': 0,
                    '26-':0
                    }
                },
            'Totals': {
                'Male': 0,
                'Female': 0,
                'Unspecified': 0,
                'Paid': 0,
                'Unpaid': 0,
                '0-5': 0,
                '6-12': 0,
                '13-19': 0,
                '20-25': 0,
                '26-': 0,
                'Total': 0
            }       
            }

        # count occurences at the lowest level of the report per gender
        for i in list(processed_data['PersonID'].keys()):
            if processed_data['Gender'][i] == 'Kvinne':
                if processed_data['HasPaid'][i] == True:
                    if processed_data['Age'][i] in range(0,6):
                        report['Female']['Paid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Female']['Paid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Female']['Paid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Female']['Paid']['20-25'] += 1
                    elif processed_data['Age'][i] >= 26:
                        report['Female']['Paid']['26-'] += 1
                else:
                    if processed_data['Age'][i] in range(0,6):
                        report['Female']['Unpaid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Female']['Unpaid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Female']['Unpaid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Female']['Unpaid']['20-25'] += 1
                    elif processed_data['Age'][i] >= 26:
                        report['Female']['Unpaid']['26-'] += 1
            elif processed_data['Gender'][i] == 'Mann':
                if processed_data['HasPaid'][i] == True:
                    if processed_data['Age'][i] in range(0,6):
                        report['Male']['Paid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Male']['Paid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Male']['Paid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Male']['Paid']['20-25'] += 1
                    elif processed_data['Age'][i] >= 26:
                        report['Male']['Paid']['26-'] += 1
                else:
                    if processed_data['Age'][i] in range(0,6):
                        report['Male']['Unpaid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Male']['Unpaid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Male']['Unpaid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Male']['Unpaid']['20-25'] += 1
                    elif processed_data['Age'][i] >= 26:
                        report['Male']['Unpaid']['26-'] += 1
            else:
                if processed_data['HasPaid'][i] == True:
                    if processed_data['Age'][i] in range(0,6):
                        report['Unspecified']['Paid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Unspecified']['Paid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Unspecified']['Paid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Unspecified']['Paid']['20-25'] += 1
                    elif processed_data['Age'][i] >= 26:
                        report['Unspecified']['Paid']['26-'] += 1
                else:
                    if processed_data['Age'][i] in range(0,6):
                        report['Unspecified']['Unpaid']['0-5'] += 1
                    elif processed_data['Age'][i] in range(6,13):
                        report['Unspecified']['Unpaid']['6-12'] += 1
                    elif processed_data['Age'][i] in range(13,20):
                        report['Unspecified']['Unpaid']['13-19'] += 1
                    elif processed_data['Age'][i] in range(20,26):
                        report['Unspecified']['Unpaid']['20-25'] += 1
                    elif processed_data['Age'][i] in range(26, 300):
                        report['Unspecified']['Unpaid']['26-'] += 1
                    else:
                        print('Not counting PersonMerge')

        # calculate totals
        for gender in ['Male', 'Female', 'Unspecified']:
            for status in list(report[gender].keys()):
                for age_group in list(report[gender][status].keys()):
                    report['Totals'][age_group] += report[gender][status][age_group]
                    report['Totals'][status] += report[gender][status][age_group]
                    report['Totals'][gender] += report[gender][status][age_group]
        report['Totals']['Total'] = report['Totals']['Male'] + report['Totals']['Female'] + report['Totals']['Unspecified']
        
        return report