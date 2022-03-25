# write the file
import pandas as pd

class Write:

    def NTN(self, path, data):
        df  = pd.DataFrame.from_dict(data)
        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Medlemssystem', index=False)

        # attempt writing to file
        try:
            writer.save()
            print(f'Done. File written at  {path}')

        except:
            print(f"Couldn't write file to {path}")