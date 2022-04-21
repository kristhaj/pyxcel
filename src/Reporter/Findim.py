# map members to gren by financial dimensions from Team

class Findim:

    # itereate though members and add each unique findim to the member's data, by matching teams the member participated in to the team_findim_map
    def Map_Findim(self, members, map):
        team_list = list(map['Team'].values())
        findim_list = list(map['findim'].values())

        for member_index in list(members['PersonID'].keys()):

            matched_findims = ""
            #make list of teams the current member participated in by splitting on separator
            participated_in_list = members['Team'][member_index].split('|')
            # iterate though said list and match teams in the map, to get map_index
            for team in participated_in_list:
                #TODO: Fix issue with not matching the correct team names
                map_index = team_list.index(team)
                if findim_list[map_index] not in  matched_findims:
                    matched_findims += f"|{findim_list[map_index]}"
            
            members['Findim'].update({member_index: matched_findims})
        print('Findims have been processed.')
        return members