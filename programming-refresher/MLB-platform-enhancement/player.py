class Player:
    def __init__(self, player_id, name, team) -> None:
        self.player_id = player_id
        self.name = name
        self.team = team
        self.statistics = {}
        
    def update_team(self, newTeam):
        self.team = newTeam
        
    def add_statistic(self, name, value):
        self.statistics[name] = value
        
    def get_statistics(self):
        return self.statistics
    