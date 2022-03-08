import pandas as pd

class Write:

    def Kommune_Rapport(self, path, data):
        df = pd.DataFrame.from_dict(data)
        print(f'Writing report to {path}...')
        with pd.ExcelWriter(path) as writer: # pylint: disable=abstract-class-instantiated
            df.to_excel(writer, index=False)
        print('Done.')

    def Paid_Members_Report(self, path, data, report, template):
        df_data = pd.DataFrame.from_dict(data)