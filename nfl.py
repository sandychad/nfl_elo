class Game:
    def __init__ (self, away_team, home_team, away_score, home_score, away_wp, home_wp):
        self.away_team = away_team
        self.home_team = home_team
        self.away_score = away_score
        self.home_score = home_score
        self.away_wp = away_wp
        self.home_wp = home_wp

    def __repr__ (self):
        st = "Away - {0:3} {1:02} at {2:3} {3:02} - Home".format(self.away_team, self.away_score, self.home_team, self.home_score)
        return st

class Team:
    def __init__ (self, name, wins, losses, ties):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties



        