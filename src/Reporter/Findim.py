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
            not_applicable_teams = ['Unknown', 'Støttemedlem 2021', 'Barnebursdag pakke 2', 'SKAL IKKE BRKES NB !!!    3101 Turn Nybegynner Strømsø 6-9 H21']
            for team in participated_in_list:
                if team not in not_applicable_teams:
                    map_index = team_list.index(team)
                    if findim_list[map_index] not in  matched_findims:
                        if matched_findims != "":
                            matched_findims += f"|{findim_list[map_index]}"
                        else:
                            matched_findims += findim_list[map_index]
            
            members['Findim'].update({member_index: matched_findims})
        print('Findims have been processed.')
        return members