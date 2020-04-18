def tally(rows):
    teams = {}

    for (home_team, away_team, result) in [row.split(';') for row in rows]:
        for team in (home_team, away_team):
            if team not in teams:
                teams[team] = Team(team)
            teams[team].matches_played += 1

        if result == 'win':
            teams[home_team].wins += 1
            teams[away_team].losses += 1
        if result == 'loss':
            teams[home_team].losses += 1
            teams[away_team].wins += 1
        if result == 'draw':
            teams[home_team].draw += 1
            teams[away_team].draw += 1

    [team.calculate_points for team in teams.values()]

    return Table(teams).rows()


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

class Table:
    def __init__(self, teams):
        self.teams = teams
        self.table = []

    @staticmethod
    def spacing():
        return "{:31}| {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"

    @staticmethod
    def header():
        return f"{Table.spacing()}".format("Team", "MP", "W", "D", "L", "P")

    def rows(self):
        self.table.append(Table.header())

        for team in self.teams.values():
            row = f"{Table.spacing()}".format(
                team.name, 
                team.matches_played, 
                team.wins, 
                team.draws, 
                team.losses, 
                team.points
            )
            self.table.append(row)
        return self.table

