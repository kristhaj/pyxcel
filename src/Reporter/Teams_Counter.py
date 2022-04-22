# calculate count per team if relevant

class Teams_Counter:

    def Participation_Counter(self, processed_data, report):
        for i in list(processed_data['PersonID'].keys()):
                # if the current data set contains findims, use them instead of teams
                if processed_data['Findim'][0]:
                    current_grouping = processed_data['Findim'][i]
                else:
                    current_grouping = processed_data['Team'][i]
                # Iterate through each team registered to the member, by splitting on the separator
                for grouping in current_grouping.split('|'):
                    # add data structure to report if missing
                    if grouping not in list(report.keys()):
                        report.update({
                            grouping: {
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
                                    'paid': 0,
                                    'unpaid': 0
                                }
                            }
                        })
                    if processed_data['Gender'][i] == 'Kvinne':
                        if processed_data['HasPaid'][i] == True:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Female']['Paid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Female']['Paid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Female']['Paid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Female']['Paid']['20-25'] += 1
                            elif processed_data['Age'][i] >= 26:
                                report[grouping]['Female']['Paid']['26-'] += 1
                            report[grouping]['Totals']['paid'] += 1
                        else:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Female']['Unpaid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Female']['Unpaid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Female']['Unpaid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Female']['Unpaid']['20-25'] += 1
                            elif processed_data['Age'][i] >= 26:
                                report[grouping]['Female']['Unpaid']['26-'] += 1
                            report[grouping]['Totals']['unpaid'] += 1
                    elif processed_data['Gender'][i] == 'Mann':
                        if processed_data['HasPaid'][i] == True:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Male']['Paid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Male']['Paid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Male']['Paid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Male']['Paid']['20-25'] += 1
                            elif processed_data['Age'][i] >= 26:
                                report[grouping]['Male']['Paid']['26-'] += 1
                            report[grouping]['Totals']['paid'] += 1
                        else:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Male']['Unpaid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Male']['Unpaid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Male']['Unpaid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Male']['Unpaid']['20-25'] += 1
                            elif processed_data['Age'][i] >= 26:
                                report[grouping]['Male']['Unpaid']['26-'] += 1
                            report[grouping]['Totals']['unpaid'] += 1
                    else:
                        if processed_data['HasPaid'][i] == True:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Unspecified']['Paid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Unspecified']['Paid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Unspecified']['Paid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Unspecified']['Paid']['20-25'] += 1
                            elif processed_data['Age'][i] >= 26:
                                report[grouping]['Unspecified']['Paid']['26-'] += 1
                            report[grouping]['Totals']['paid'] += 1
                        else:
                            if processed_data['Age'][i] in range(0,6):
                                report[grouping]['Unspecified']['Unpaid']['0-5'] += 1
                            elif processed_data['Age'][i] in range(6,13):
                                report[grouping]['Unspecified']['Unpaid']['6-12'] += 1
                            elif processed_data['Age'][i] in range(13,20):
                                report[grouping]['Unspecified']['Unpaid']['13-19'] += 1
                            elif processed_data['Age'][i] in range(20,26):
                                report[grouping]['Unspecified']['Unpaid']['20-25'] += 1
                            elif processed_data['Age'][i] in range(26, 300):
                                report[grouping]['Unspecified']['Unpaid']['26-'] += 1
                            else:
                                print('Not counting PersonMerge')
                                # correct count for merged entity
                                report[grouping]['Totals']['unpaid'] -= 1
                            report[grouping]['Totals']['unpaid'] += 1
        print(f'Teams data has been counted for {len(list(report.keys()))-4} Teams')
        return report