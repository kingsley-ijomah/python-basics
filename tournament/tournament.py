class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.matches_played = 0
        self.points = 0

    def calculate_points(self):
        self.points = (self.wins * 3) + (self.draws * 1)

class TeamBuilder:
    def __init__(self, rows):
        self.rows = [row.split(';') for row in rows]
        self.teams = {}

    def build(self):
        for (home_team, away_team, result) in self.rows:
            for team in (home_team, away_team):
                if team not in self.teams:
                    self.teams[team] = Team(team)
                self.teams[team].matches_played += 1

            if result == 'win':
                self.teams[home_team].wins += 1
                self.teams[away_team].losses += 1
            if result == 'loss':
                self.teams[home_team].losses += 1
                self.teams[away_team].wins += 1
            if result == 'draw':
                self.teams[home_team].draws += 1
                self.teams[away_team].draws += 1
       
        # calculate points for each team
        [team.calculate_points() for team in self.teams.values()]

        return self.teams.values()

class Table:
    def __init__(self, teams):
        self.teams = teams
        self.table = []

    def spacing(self):
        return "{:31}| {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

    def header(self):
        return f"{self.spacing()}".format("Team", "MP", "W", "D", "L", "P")

    def sort_rows(self, teams):
        return sorted(teams, key=lambda x: (-x.points, x.name))

    def rows(self):
        self.table.append(self.header())

        for team in self.sort_rows(self.teams):
            row = f"{self.spacing()}".format(
                team.name, 
                team.matches_played, 
                team.wins, 
                team.draws, 
                team.losses, 
                team.points,
            )
            self.table.append(row)
        return(self.table)

def tally(rows):
    teams = TeamBuilder(rows).build()
    return Table(teams).rows()

