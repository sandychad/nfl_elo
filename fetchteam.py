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
    
    # append nfl.game objecs with each individual game to the list of games 
    for row in df.itertuples(index=False):
        games.append (nfl.Game(row[1], row[0], row[3], row[2], row[5], row[4]))
        
    # print out games
    for game in games:
        if game.away_team == 'SEA' or game.home_team == 'SEA':
            print(game)
        

# __main__
if __name__ == "__main__":
    main()