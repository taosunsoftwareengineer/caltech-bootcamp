class Team:
    def __init__(self, team_id, name):
        self.team_id = team_id,
        self.name = name
        self.players = []
        
    def add_player(self, player_id):
        if player_id not in self.players:
            self.players.append(player_id)
            
    def remove_player(self, player_id):
        if player_id in self.players:
            self.players.remove(player_id)
        
    def get_players(self):
        return self.players
    