# Append seperate files into a single master file

import os
import pandas as pd

class Appendinator:

    def __init__(self) -> None:
        #Get dir and destination from ENV vars
        self.data_dir = os.getenv("DATA_DIR")
        self.target_path = os.getenv("TARGET_PATH")

    def Main(self):

        df = pd.DataFrame()
        shape = df.shape
        print(f'Reading data from {self.data_dir} ...')
        files = os.listdir(self.data_dir)
        files_handled = 0
        for f in files:
            path = f'{self.data_dir}/'+f
            data = pd.read_excel(path, sheet_name=None)
            print (type(data))
            #d_shape = data.shape
            df = df.append(data, ignore_index=True)
            files_handled += 1
            print(f'Processed {files_handled} out of {len(files)} files.')
        print(f'Finished Processing All Data\n===\n')

        print(f'Writing data to target: {self.target_path} ...')
        with pd.ExcelWriter(self.target_path) as writer: # pylint: disable=abstract-class-instantiated
            df.to_excel(writer, index=False, date_format='YYYY.MM.DD', datetime_format='YYYY.MM.DD')
        print('DONE')
        pass






Appendinator().Main()