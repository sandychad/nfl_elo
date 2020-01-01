# import statements
import pandas as pd
import nfl

# main function
def main():

    # load csv file into pandas data frame
    data = pd.read_csv(r'nfl_elo_latest.csv', nrows=256)
    df = pd.DataFrame(data, columns = ['team1', 'team2', 'score1', 'score2', 'elo_prob1', 'elo_prob2'])
    
    # initialize starting variables
    games = []
    wins = 0
    ties = 0
    losses = 0
    successfulInput = False
    
    # append dictionaries with game by game data to games list  
    for row in df.itertuples(index=False):
        games.append ({'home_team': row[0], 'away_team': row[1], 'home_score': row[2],
         'away_score': row[3], 'home_winprob': row[4], 'away_winprob':row[5]})

    # list of teams to check for valid input 
    teams = sorted(['CHI', 'GB', 'JAX', 'KC', 'CAR', 'LAR', 'CLE', 'TEN',
     'PHI', 'WSH', 'NYJ', 'BUF', 'MIN', 'ATL', 'MIA', 'BAL', 
     'SEA', 'CIN', 'LAC', 'IND', 'DAL', 'NYG', 'TB', 'SF', 
     'ARI', 'DET', 'NE', 'PIT', 'NO', 'HOU', 'OAK', 'DEN'])

    # isolate and print: home and away game scores | win probabilities for each team | game outcome
    while not successfulInput:      # infinite loop to allow for multiple attempts
        user_input = input("Which team's results would you like? ").upper()
        team = user_input
        
        # check whether input matches list of teams
        if team in teams:    
            print()         # blank line

            # get and display values
            for game in games:
                # get values
                away_name = game['away_team']
                away_score = game['away_score']
                away_winprob = game['away_winprob']
                
                home_name = game['home_team']
                home_score = game['home_score']
                home_winprob = game['home_winprob']

                # display values
                if home_name == team or away_name == team:
                    print(f"Away - {away_name:3} {away_score:02} at {home_name:3} {home_score:02} - Home", end=" | ")
                    
                    if home_name == team:
                        print(f"WP: {home_winprob:2.2%}", end=" | ")
                    elif away_name == team:
                        print(f"WP: {away_winprob:2.2%}", end=" | ")

                    # print game result
                    if home_name == team and home_score > away_score:
                        print("WIN", end="")
                        wins += 1
                    elif away_name == team and away_score > home_score:
                        print("WIN", end="")
                        wins += 1
                    elif away_score == home_score:
                        print("TIE", end="")
                        ties += 1
                    else:
                        print("LOSS", end="")
                    
                    print() # start new line

            successfulInput = True  # exit infinite loop 
        
        # team not found - remain in infinite loop and prompt user for new team
        else:
            print("Name must be given in short code form (2 or 3 letters). List of Teams:")  
            
            for t in teams:
                print(t, end=" ")
            print()

    # print season record      
    print()                 # blank line

    losses = 16 - wins - ties
    print(f"{team} Record: {wins}-{losses}", end="")
    if ties != 0: print(f"-{ties}", end="")  # print ties only if they exist
    
    print()                 # new line 
    print()                 # blank line


# __main__
if __name__ == "__main__":
    main()