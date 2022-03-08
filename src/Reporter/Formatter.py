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
