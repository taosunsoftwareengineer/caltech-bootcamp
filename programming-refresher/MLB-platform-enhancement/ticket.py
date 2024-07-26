class Ticket:
    def __init__(self, ticket_id, match_id, seat_number, price):
        self.ticket_id = ticket_id
        self.match_id = match_id,
        self.seat_number = seat_number
        self.price = price
        self.buyer_id = None
        
    def book(self, buyer_id):
        self.buyer_id = buyer_id
        
    def cancel(self):
        self.buyer_id = None
        
    def get_ticket_info(self):
        return {
            "ticket_id": self.ticket_id,
            "match_id": self.match_id,
            "seat_number": self.seat_number,
            "price": self.price,
            "buyer_id": self.buyer_id
        }
    
        