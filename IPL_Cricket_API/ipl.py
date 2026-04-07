import numpy as np
import pandas as pd
import json


# ipl_data = "https://drive.google.com/file/d/1lbdXoBE6JzfmIZ7HhtMxnK28cz6NWayk/view?usp=drive_link"

ipl = pd.read_csv("ipl-matches.csv")
# print(ipl.head(3))



# converting into python dictionary, because it is very similar to json
def teams_API():
    teams =  list(set(list(ipl['Team1']) + list(ipl['Team2'])))
    dict_teams = {
        'teams':teams
    }
    
    return dict_teams

def team_vs_team_API(team1, team2):
    valid_teams =  list(set(list(ipl['Team1']) + list(ipl['Team2'])))
    if team1 in valid_teams and team2 in valid_teams:
    
        temp_df = ipl[(ipl['Team1'] == team1) & (ipl['Team2'] == team2) | (ipl['Team1'] == team1) & (ipl['Team2'] == team2)]
        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draw = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
            'total_matches': total_matches,
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            'draws': str(draw)
        }
        return response
    
    else:
        return {'message': 'Invalid team name'}