# Extrapolate trainingsdata from data foundation and apply to relevant members



class Trainings:

    # Extrapolate trainings data from data foundation
    def Get_Data(self, data, training_sheet, gren_sheet, _style_sheet):
        print(f'Processing Training Fee Data for:')
        multi_gren_clubs = {'Status': False, 'Clubs': []}
        for key in list(data.keys()):
            print(f'{key}....')
            Trainings.Set_Styles(self, data[key]['Gren/Stilart/Avd/Parti - Gren/Stilart/Avd/Parti'], key, _style_sheet)
            Trainings.Set_Grens(self, data[key]['Gren/Stilart/Avd/Parti - Gren/Stilart/Avd/Parti'], key, gren_sheet, multi_gren_clubs)
            
            if multi_gren_clubs['Status'] and key in multi_gren_clubs['Clubs']:
                Trainings.Set_Products(self, data[key], key, gren_sheet, training_sheet, True)
            else:
                Trainings.Set_Products(self, data[key], key, gren_sheet, training_sheet)
        print(f'All relevant Training Fee Data Processed.\n')
        return training_sheet, gren_sheet, _style_sheet, multi_gren_clubs

    # Extrapolate Style data
    def Set_Styles(self, data, id, styles):
        processed_styles = []
        for val in list(data.values()):
            if type(val) != float and '/' in val:
                g_val = val.split('/')[0]
                val = val.split('/')[1]
                next_index = len(styles['Club'])
                if val not in processed_styles:
                    processed_styles.append(val)
                    styles['Name of style'].update({next_index: val})
                    styles['Gren'].update({next_index: g_val})
                    #styles['Start date'].update({next_index: None})
                    #styles['End date'].update({next_index: None})
                    styles['Club'].update({next_index: id})

    # Extrapolate Gren data
    def Set_Grens(self, data, id, grens, multi_gren_clubs):
        processed_grens = []
        for val in list(data.values()):
            if type(val) != float:
                val = val.split('/')[0]
                next_index = len(grens['ClubID'])
                if val not in processed_grens:
                    processed_grens.append(val)
                    grens['Name of Gren'].update({next_index: val})
                    grens['ClubID'].update({next_index: id})
                    if len(processed_grens) > 1:
                        multi_gren_clubs['Status'] = True
                        multi_gren_clubs['Clubs'].append(id)
        if len(processed_grens) > 1:
            print(f'WARNING: Multiple Grens Processed: {processed_grens}. Training Fee Control is Advised!')

    # Extrapolate Training fee data
    def Set_Products(self, data, id, gren_sheet, trainings, is_multi_gren=False):
        processed_trainings = []
        for key in list(data['Medlemsnummer'].keys()):
            val = data['Kontraktstype'][key]
            if type(val) != float:
                g_val = data['Gren/Stilart/Avd/Parti - Gren/Stilart/Avd/Parti'][key]
                if type(g_val) != float:
                    g_val = g_val.split('/')[0]
                next_index = len(trainings['NIFOrgId'])
                if is_multi_gren:
                    val = f'{val} - {g_val}'
                if val not in processed_trainings:
                    processed_trainings.append(val)
                    trainings['NIFOrgId'].update({next_index: id})
                    trainings['Name traning fee'].update({next_index: val})
                    trainings['Sports'].update({next_index: g_val})
                    trainings['Membership category'].update({next_index: data['Medlemskategori navn'][key]})
                    trainings['Amount in Kr'].update({next_index: data['Kontraktsbeløp'][key]})
                    trainings['Traningsship length'].update({next_index: 1})
                    trainings['Length type'].update({next_index: 'Måned'})
                    trainings['Invoice frequence'].update({next_index: 1})
                    trainings['Invoice frequence type'].update({next_index: 'Måned'})
                    trainings['Renewal'].update({next_index: 'Ja'})
                    trainings['Startup package'].update({next_index: 'Nei'})

    # Apply the correct trainings to the correct members
    def Apply_Product(self, product, index, member_sheet, gren=None, onboarded=None):
        member_sheet['Old traning fee name'].update({index: product})
        if gren != None:
            product = f'{product} - {gren}'
            member_sheet['Training fee name'].update({index: product})
        else:
            member_sheet['Training fee name'].update({index: product})
