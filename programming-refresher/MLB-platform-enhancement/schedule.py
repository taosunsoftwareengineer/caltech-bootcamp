class Schedule:
    def __init__(self, match_id, teams, match_date, match_location):
        self.match_id = match_id
        self.teams = teams
        self.match_date = match_date
        self.match_location = match_location
        
    def change_date(self, new_match_date):
        self.match_date = new_match_date
        
    def change_location(self, new_match_location):
        self.match_location = new_match_location
        
    def get_match_details(self):
        return {
            "match_id": self.match_id,
            "teams": self.teams,
            "match_date": self.match_date,
            "match_location": self.match_location
        }