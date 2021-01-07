# Cross reference call list with member data to identify administrator and relevant information.
import os
import Load, Identify, Lookup, Write

class Adminipy:

    def __init__(self):
        self.call_path = os.getenv('CALL_PATH')
        self.member_data_path = os.getenv('MEMBER_DATA_PATH')
        self.qualifier_path = os.getenv('QUALIFIER_PATH')
        self.destination_path = os.getenv('DESTINATION_PATH')

    # Reads the relevant data from data file, and then appends data frame to existing xlsx file
    # NOTE:test first in separate file to avoid breaking status
    def setAdmins(self, indices, path, destination):

        pass


    # Do the thing
    def Main(self):
        print('hello?')

Adminipy().Main()