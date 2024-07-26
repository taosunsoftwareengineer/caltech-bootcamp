class Booking:
    def __init__(self):
        self.bookings = {}
        
    def book_ticket(self, match_id, ticket_id):
        if match_id not in self.bookings:
            self.bookings[match_id] = [ticket_id]
        else:
            self.bookings[match_id].append(ticket_id)

    def cancel_ticket(self, match_id, ticket_id):
        if match_id in self.bookings and ticket_id in self.bookings[match_id]:
            self.bookings[match_id].remove(ticket_id)
            
    def get_match_tickets(self, match_id):
        if match_id in self.bookings:
            return self.bookings[match_id]
        
    def get_all_matches_of_ticket(self, ticket_id):
        matches = []
        for match in self.bookings:
            if ticket_id in self.bookings[match]:
                matches.append(match)
        return matches