# Write relevant data and results to new file

import pandas as pd

class Write:

    # TODO: Write the compared data to a given destination
    def Result(self, data, destination):
        temp_df = pd.DataFrame.from_dict(data)
        print(f'Writing Report of Deviating Data to {destination}...')
        with pd.ExcelWriter(destination) as writer: # pylint: disable=abstract-class-instantiated
            temp_df.to_excel(writer, index=False)
        print('Done.\n=====')