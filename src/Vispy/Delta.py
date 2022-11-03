import copy

# Calculate delta of new and old data

class Delta:

    def Get_Delta(self, old, new):
        print('Calculating delta...')

        delta_dict = copy.copy(new)

        org_list = list(delta_dict['OrgIdGren'].values())

        for orgId in org_list:

            data_index_new = list(delta_dict['OrgIdGren'].keys())[org_list.index(orgId)]
            data_index_old = False
            try:
                data_index_old = list(old['OrgIdGren'].keys())[org_list.index(orgId)]
            except:
                print(f'{orgId} belongs to new club')

            # Get delta of new and old data
            d_u13 = new['Under13Gren'][data_index_new] - old['Under13Gren'][data_index_old]
            d_o13 = new['Over13Gren'][data_index_new] - (old['Over13Gren'][data_index_old] if data_index_old else 0)

            # Update delta_dict with the new amount, unless it is lower, in which case it is 0
            delta_dict['Under13Gren'][data_index_new] = d_u13 if d_u13 > 0 else 0
            delta_dict['Over13Gren'][data_index_new] = d_o13 if d_o13 > 0 else 0
        
        print('Delta has been calculated.')

        return delta_dict
        