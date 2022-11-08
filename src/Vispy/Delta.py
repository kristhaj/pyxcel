import copy

# Calculate delta of new and old data

class Delta:

    def Get_Delta(self, old, new):
        print('Calculating delta...')

        delta_dict = copy.copy(new)

        org_list = list(delta_dict['OrgIdGren'].values())
        old_org_list = list(old['OrgIdGren'].values())

        for orgId in org_list:

            data_index_new = list(delta_dict['OrgIdGren'].keys())[org_list.index(orgId)]
            data_index_old = old_org_list.index(orgId) if orgId in old_org_list else False

            #print(f'Processing: {delta_dict["ClubName"][data_index_new]}, with Gren: {orgId}, {delta_dict["GrenName"][data_index_new]} at i:{data_index_new}, j:{data_index_old}')

            if type(data_index_old) == int:
                # Store new and old counts
                o_u13 = old['Under13Gren'][data_index_old]
                n_u13 = new['Under13Gren'][data_index_new]
                o_o13 = old['Over13Gren'][data_index_old]
                n_o13 = new['Over13Gren'][data_index_new]

                
                # Get delta of new and old data
                d_u13 = n_u13 - o_u13
                d_o13 = n_o13 - o_o13
                #print(f'Under13: {n_u13}-{o_u13}\nOver13: {n_o13}-{o_o13}\nCalculated Delta\nu13: {d_u13}\no13: {d_o13}')
                # Update delta_dict with the new amount, unless it is lower, in which case it is 0
                delta_dict['Under13Gren'][data_index_new] = d_u13 if d_u13 > 0 else 0
                delta_dict['Over13Gren'][data_index_new] = d_o13 if d_o13 > 0 else 0
            else:
                print(f'{orgId} belongs to new club or gren')
            #print(f'New member counts\nu13: {delta_dict["Under13Gren"][data_index_new]}\no13: {delta_dict["Over13Gren"][data_index_new]}\n')
        print('Delta has been calculated.')

        return delta_dict
        