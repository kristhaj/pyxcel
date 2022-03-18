import pandas as pd

class Formatter:
    
    # Populate the formatted DataFrame from template with the data from the report dictionary
    def Paid_Member_Formatting(self, template, report):
        # Set Male Paid, Unpaid statistics
        template.iat[2, 2]= report['Male']['Paid']['0-5']
        template.iat[3, 2]= report['Male']['Unpaid']['0-5']
        template.iat[2, 3]= report['Male']['Paid']['6-12']
        template.iat[3, 3]= report['Male']['Unpaid']['6-12']
        template.iat[2, 4]= report['Male']['Paid']['13-19']
        template.iat[3, 4]= report['Male']['Unpaid']['13-19']
        template.iat[2, 5]= report['Male']['Paid']['20-25']
        template.iat[3, 5]= report['Male']['Unpaid']['20-25']
        template.iat[2, 6]= report['Male']['Paid']['26-']
        template.iat[3, 6]= report['Male']['Unpaid']['26-']

        # Set Female Paid, Unpaid Statistics
        template.iat[2, 8]= report['Female']['Paid']['0-5']
        template.iat[3, 8]= report['Female']['Unpaid']['0-5']
        template.iat[2, 9]= report['Female']['Paid']['6-12']
        template.iat[3, 9]= report['Female']['Unpaid']['6-12']
        template.iat[2, 10]= report['Female']['Paid']['13-19']
        template.iat[3, 10]= report['Female']['Unpaid']['13-19']
        template.iat[2, 11]= report['Female']['Paid']['20-25']
        template.iat[3, 11]= report['Female']['Unpaid']['20-25']
        template.iat[2, 12]= report['Female']['Paid']['26-']
        template.iat[3, 12]= report['Female']['Unpaid']['26-']

        # Set Unspecified gender Paid, Unpaid Statistics
        template.iat[2, 14]= report['Unspecified']['Paid']['0-5']
        template.iat[3, 14]= report['Unspecified']['Unpaid']['0-5']
        template.iat[2, 15]= report['Unspecified']['Paid']['6-12']
        template.iat[3, 15]= report['Unspecified']['Unpaid']['6-12']
        template.iat[2, 16]= report['Unspecified']['Paid']['13-19']
        template.iat[3, 16]= report['Unspecified']['Unpaid']['13-19']
        template.iat[2, 17]= report['Unspecified']['Paid']['20-25']
        template.iat[3, 17]= report['Unspecified']['Unpaid']['20-25']
        template.iat[2, 18]= report['Unspecified']['Paid']['26-']
        template.iat[3, 18]= report['Unspecified']['Unpaid']['26-']

        # Set Totals
        template.iat[2, 20]= report['Totals']['Paid']
        template.iat[3, 20]= report['Totals']['Unpaid']

        template.iat[9, 2]= report['Totals']['Male']
        template.iat[9, 3]= report['Totals']['Female']
        template.iat[9, 4]= report['Totals']['Unspecified']
        template.iat[9, 5]= report['Totals']['Paid']
        template.iat[9, 6]= report['Totals']['Unpaid']
        template.iat[9, 7]= report['Totals']['0-5']
        template.iat[9, 8]= report['Totals']['6-12']
        template.iat[9, 9]= report['Totals']['13-19']
        template.iat[9, 10]= report['Totals']['20-25']
        template.iat[9, 11]= report['Totals']['26-']
        template.iat[9, 12]= report['Totals']['Total']

        return template

    # Format teams member statistics
    def Team_Statistics_formatting(self, report, template):
        template_dict = template.to_dict()
        # step to offset rows per team statistics
        step = 0
        # Format data per team into the template
        for team_index in range(4, len(list(report.keys()))):
            current_team = list(report.keys())[team_index]
            row = 15+step
            # Set headers for each bulk
            
            template_dict['Gender'].update({row: 'Gender'})
            template_dict['Menn'].update({row: 'Menn'})
            template_dict['Kvinner'].update({row: 'Kvinner'})
            template_dict['Gender Not Mentioned'].update({row: 'Gender Not Mentioned'})
            # set age metrics
            template_dict['Gender'].update({row+1: 'AgeMetric'})
            template_dict['Menn'].update({row+1: '0 - 5'})
            template_dict['Menn.1'].update({row+1: '6 - 12'})
            template_dict['Menn.2'].update({row+1: '13 - 19'})
            template_dict['Menn.3'].update({row+1: '20 - 25'})
            template_dict['Menn.4'].update({row+1: '26 -'})
            template_dict['Kvinner'].update({row+1: '0 - 5'})
            template_dict['Kvinner.1'].update({row+1: '6 - 12'})
            template_dict['Kvinner.2'].update({row+1: '13 - 19'})
            template_dict['Kvinner.3'].update({row+1: '20 - 25'})
            template_dict['Kvinner.4'].update({row+1: '26 -'})
            template_dict['Gender Not Mentioned'].update({row+1: '0 - 5'})
            template_dict['Gender Not Mentioned.1'].update({row+1: '6 - 12'})
            template_dict['Unnamed: 16'].update({row+1: '13 - 19'})
            template_dict['Unnamed: 17'].update({row+1: '20 - 25'})
            template_dict['Unnamed: 18'].update({row+1: '26 -'})
            template_dict['Unnamed: 20'].update({row+1: 'Totals'})
            # set left hand legend
            template_dict['Gender'].update({row+2: 'TeamName'})
            template_dict['Gender'].update({row+3: current_team})
            template_dict['Gender'].update({row+4: current_team})
            template_dict['Unnamed: 1'].update({row+2: 'InvoiceStatus'})
            template_dict['Unnamed: 1'].update({row+3: 'Paid'})
            template_dict['Unnamed: 1'].update({row+4: 'Unpaid'})
            template_dict['Gender'].update({row+5: ''})
            template_dict['Unnamed: 1'].update({row+5: ''})
            template_dict['Gender'].update({row+6: ''})
            template_dict['Unnamed: 1'].update({row+6: ''})

            # set team member counts
            # Set Male Paid, Unpaid statistics
            template_dict['Menn'].update({row+3: report[current_team]['Male']['Paid']['0-5']})
            template_dict['Menn.1'].update({row+3: report[current_team]['Male']['Paid']['6-12']})
            template_dict['Menn.2'].update({row+3: report[current_team]['Male']['Paid']['13-19']})
            template_dict['Menn.3'].update({row+3: report[current_team]['Male']['Paid']['20-25']})
            template_dict['Menn.4'].update({row+3: report[current_team]['Male']['Paid']['26-']})
            template_dict['Menn'].update({row+4: report[current_team]['Male']['Unpaid']['0-5']})
            template_dict['Menn.1'].update({row+4: report[current_team]['Male']['Unpaid']['6-12']})
            template_dict['Menn.2'].update({row+4: report[current_team]['Male']['Unpaid']['13-19']})
            template_dict['Menn.3'].update({row+4: report[current_team]['Male']['Unpaid']['20-25']})
            template_dict['Menn.4'].update({row+4: report[current_team]['Male']['Unpaid']['26-']})
            # populate empty rows to account for DF conversion
            template_dict['Menn'].update({row+5: ''})
            template_dict['Menn.1'].update({row+5:''})
            template_dict['Menn.2'].update({row+5: ''})
            template_dict['Menn.3'].update({row+5: ''})
            template_dict['Menn.4'].update({row+5: ''})
            template_dict['Menn'].update({row+6: ''})
            template_dict['Menn.1'].update({row+6:''})
            template_dict['Menn.2'].update({row+6: ''})
            template_dict['Menn.3'].update({row+6: ''})
            template_dict['Menn.4'].update({row+6: ''})

            # Set Female Paid, Unpaid Statistics
            template_dict['Kvinner'].update({row+3: report[current_team]['Female']['Paid']['0-5']})
            template_dict['Kvinner.1'].update({row+3: report[current_team]['Female']['Paid']['6-12']})
            template_dict['Kvinner.2'].update({row+3: report[current_team]['Female']['Paid']['13-19']})
            template_dict['Kvinner.3'].update({row+3: report[current_team]['Female']['Paid']['20-25']})
            template_dict['Kvinner.4'].update({row+3: report[current_team]['Female']['Paid']['26-']})
            template_dict['Kvinner'].update({row+4: report[current_team]['Female']['Unpaid']['0-5']})
            template_dict['Kvinner.1'].update({row+4: report[current_team]['Female']['Unpaid']['6-12']})
            template_dict['Kvinner.2'].update({row+4: report[current_team]['Female']['Unpaid']['13-19']})
            template_dict['Kvinner.3'].update({row+4: report[current_team]['Female']['Unpaid']['20-25']})
            template_dict['Kvinner.4'].update({row+4: report[current_team]['Female']['Unpaid']['26-']})
            # populate empty rows to account for DF conversion
            template_dict['Kvinner'].update({row+5: ''})
            template_dict['Kvinner.1'].update({row+5:''})
            template_dict['Kvinner.2'].update({row+5: ''})
            template_dict['Kvinner.3'].update({row+5: ''})
            template_dict['Kvinner.4'].update({row+5: ''})
            template_dict['Kvinner'].update({row+6: ''})
            template_dict['Kvinner.1'].update({row+6:''})
            template_dict['Kvinner.2'].update({row+6: ''})
            template_dict['Kvinner.3'].update({row+6: ''})
            template_dict['Kvinner.4'].update({row+6: ''})


            # Set Unspecified gender Paid, Unpaid Statistics
            template_dict['Gender Not Mentioned'].update({row+3: report[current_team]['Unspecified']['Paid']['0-5']})
            template_dict['Gender Not Mentioned.1'].update({row+3: report[current_team]['Unspecified']['Paid']['6-12']})
            template_dict['Unnamed: 16'].update({row+3: report[current_team]['Unspecified']['Paid']['13-19']})
            template_dict['Unnamed: 17'].update({row+3: report[current_team]['Unspecified']['Paid']['20-25']})
            template_dict['Unnamed: 18'].update({row+3: report[current_team]['Unspecified']['Paid']['26-']})
            template_dict['Gender Not Mentioned'].update({row+4: report[current_team]['Unspecified']['Unpaid']['0-5']})
            template_dict['Gender Not Mentioned.1'].update({row+4: report[current_team]['Unspecified']['Unpaid']['6-12']})
            template_dict['Unnamed: 16'].update({row+4: report[current_team]['Unspecified']['Unpaid']['13-19']})
            template_dict['Unnamed: 17'].update({row+4: report[current_team]['Unspecified']['Unpaid']['20-25']})
            template_dict['Unnamed: 18'].update({row+4: report[current_team]['Unspecified']['Unpaid']['26-']})
            # populate empty rows to account for DF conversion
            template_dict['Gender Not Mentioned'].update({row+5: ''})
            template_dict['Gender Not Mentioned.1'].update({row+5:''})
            template_dict['Unnamed: 16'].update({row+5: ''})
            template_dict['Unnamed: 17'].update({row+5: ''})
            template_dict['Unnamed: 18'].update({row+5: ''})
            template_dict['Gender Not Mentioned'].update({row+6: ''})
            template_dict['Gender Not Mentioned.1'].update({row+6:''})
            template_dict['Unnamed: 16'].update({row+6: ''})
            template_dict['Unnamed: 17'].update({row+6: ''})
            template_dict['Unnamed: 18'].update({row+6: ''})

            # set totals per team
            template_dict['Unnamed: 20'].update({row+3: report[current_team]['Totals']['paid']})
            template_dict['Unnamed: 20'].update({row+4: report[current_team]['Totals']['unpaid']})
            template_dict['Unnamed: 20'].update({row+5: ''})
            template_dict['Unnamed: 20'].update({row+6: ''})
            
            # increase step i avoid overwriting statistics
            step += 8
        template = pd.DataFrame.from_dict(template_dict)
        return template
