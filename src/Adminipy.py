# Cross reference call list with member data to identify administrator and relevant information.

# read files of callees and member data to cross reference
# returns extrapolatet list of callee names and DataFrame of member data
# read only necessary columns for member data to opimize resulting data frame
# NOTE: batch 1 is differently formated than the others
def LoadDataFrames(path_call, path_members):

    pass

# Cross reference the list names with member data
# returns indices of people identified as admins
def IdentifyAdmins(names, data):

    pass

# Reads the relevant data from data file, and then appends data frame to existing xlsx file
# NOTE:test first in separate file to avoid breaking status
def CommitAdmins(indices, path, destination):

    pass


# Do the thing
def Main():
    call_path = ''
    #set for each batch to process
    member_data_path = ''
    destination_path = ''


Main()