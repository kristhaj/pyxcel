# Write processed data into final output format defined by the given template

import pandas as pd

class Write:

    # Write Visma formatted files
    def Visma_Format(self, path, data):
        df = pd.DataFrame.from_dict(data)
        writer = pd.ExcelWriter(path, engine='xlsxwriter', date_format='DD.MM.YYYY', datetime_format='DD.MM.YYYY') # pylint: disable=abstract-class-instantiated'
        df.to_excel(writer, sheet_name='Fakturagrunnlag', index=False)

        # Attempt Write to File
        try:
            writer.save()
            print(f'\nAll Done, file is available at {path}')
        except:
            print(f'\nWriting to file has failed... Oopsy')