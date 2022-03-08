import pandas as pd

class Write:

    def Kommune_Rapport(self, path, data):
        df = pd.DataFrame.from_dict(data)
        print(f'Writing report to {path}...')
        with pd.ExcelWriter(path) as writer: # pylint: disable=abstract-class-instantiated
            df.to_excel(writer, index=False)
        print('Done.')

    def Paid_Members_Report(self, path, data, report):
        print(f'Writing file to target: {path}')
        # Create Data Frames from provided dictionaries
        df_data = pd.DataFrame.from_dict(data)
        df_report = pd.DataFrame.from_dict(report)

        # Create Writer
        writer = pd.ExcelWriter(path, engine="xlsxwriter", date_format='DD.MM.YYYY', datetime_format='DD.MM.YYYY') # pylint: disable=abstract-class-instantiated

        # Write DataFrames to respective sheets
        df_data.to_excel(writer, sheet_name='Data', index=False)
        df_report.to_excel(writer, sheet_name='Report', index=False)

        # Attempt Write to File
        try:
            writer.save()
            print(f'\nAll Done, file is available at {path}')
        except:
            print(f'\nWriting to file has failed... Oopsy')