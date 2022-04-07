# write data to file, with desired format

import pandas as pd


class Write:

    def Spond_File(self, data, path):
        print(f'Writing file to target: {path}')
        # Create Data Frames from provided dictionaries
        df_data = pd.DataFrame.from_dict(data)

        # Create Writer
        writer = pd.ExcelWriter(path, engine="xlsxwriter", date_format='DD.MM.YYYY', datetime_format='DD.MM.YYYY') # pylint: disable=abstract-class-instantiated
        df_data.to_excel(writer, sheet_name='Members', index=False)

        # Attempt Write to File
        try:
            writer.save()
            print(f'\nAll Done, file is available at {path}')
        except:
            print(f'\nWriting to file has failed... Oopsy')
        