from datetime import datetime
from backend_python.services.ticket import Ticket
from backend_python.services.ticket_state import TicketState, CancelledState, PaidState, UsedState
from backend_python.services.pricing_stategy import RegularPricing, DayPricing, HourPricing, MemberPricing

# Regular pricing
ticket = Ticket(strategy=RegularPricing(), ticket_id=1, movie_id=1, showtime_id=1, seat_number=1, status=PaidState())
print(ticket.get_final_price())  # Should print 5.0

# Day pricing (Tuesday)
ticket = Ticket(strategy=DayPricing(), ticket_id=1, movie_id=1, showtime_id=1, seat_number=1, status=PaidState())
print(ticket.get_final_price(date=datetime(2023, 10, 17)))  # Should print 4.0 (Tuesday)

# Hour pricing (After 3 PM)
ticket = Ticket(strategy=HourPricing(), ticket_id=1, movie_id=1, showtime_id=1, seat_number=1, status=PaidState())
print(ticket.get_final_price(date=datetime(2023, 10, 17, 16, 0)))  # Should print 5.5 (After 3 PM)

# Member pricing
ticket = Ticket(strategy=MemberPricing(), ticket_id=1, movie_id=1, showtime_id=1, seat_number=1, status=PaidState())
print(ticket.get_final_price(is_member=True))  # Should print 4.5 (Member)