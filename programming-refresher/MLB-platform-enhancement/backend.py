from datetime import datetime
from booking import Booking
from player import Player
from team import Team
from schedule import Schedule
from ticket import Ticket
import uuid

class Backend:
    def __init__(self):
        self.players = {}
        self.schedules = {}
        self.tickets = {}
        self.teams = {}
        self.reports = {}
        self.bookings = Booking()
        
    def add_player(self, player: Player):
        self.players[player.player_id] = player
        
    def add_team(self, team: Team):
        self.teams[team.team_id] = team
        
    def add_schedule(self, schedule: Schedule):
        self.schedules[schedule.match_id] = schedule
        
    def add_ticket(self, ticket: Ticket):
        self.tickets[ticket.ticket_id] = ticket
        
    def book_ticket(self, ticket_id, buyer_id):
        if ticket_id in self.tickets.keys():
            ticket = self.tickets[ticket_id]
            ticket.__class__ = Ticket
            ticket.book(buyer_id)
            self.bookings.book_ticket(ticket.match_id, ticket_id)
            
    def generate_player_report(self, player_id):
        if player_id in self.players.keys():
            player = self.players[player_id]
            player.__class__ = Player
            self.reports[player_id] = player.statistics
            

# show examples of use fo your classes:
backend = Backend()
player1 = Player(uuid.uuid4(), "John Smith", "Boss Team")
player2 = Player(uuid.uuid4(), "Anna May", "Eagle")
backend.add_player(player1)
backend.add_player(player2)

player1.add_statistic("number of wins", 5)
player1.add_statistic("home state", "CA")

player2.add_statistic("home city", "Los Angeles")
player2.add_statistic("age", 22)
player2.add_statistic("years in team", 5)

team1 = Team(uuid.uuid4(), "A Game")
team2 = Team(uuid.uuid4(), "Winners")

backend.add_team(team1)
backend.add_team(team2)

team1.add_player(player1)
team2.add_player(player2)

schedule = Schedule(uuid.uuid4(), [team1, team2], datetime(2024, 8, 5), "San Diego, CA, USA")
backend.add_schedule(schedule)

ticket = Ticket(uuid.uuid4(), schedule.match_id, "D15", 120.88)
backend.add_ticket(ticket)

backend.book_ticket(ticket.ticket_id, uuid.uuid4())

backend.generate_player_report(player1.player_id)
print(backend.reports)