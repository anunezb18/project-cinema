"""
This class is responsible for managing the ticket logic.
@Author: <anunezb@udistrital.edu.co>, <masanabriap@udistrital.edu.co>

CineMacondo is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

CineMacondo is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with CineMacondo. If not, see <https://www.gnu.org/licenses/>.
"""

from datetime import datetime
from backend_python.repositories.ticket_repository import TicketRepository
from backend_python.repositories.customer_repository import CustomerRepository
from backend_python.repositories.showtime_repository import ShowtimeRepository
from backend_python.repositories.showtime_repository import SeatRepository
from .ticket_state import AddedCartState, CancelledState
from .pricing_stategy import MemberPricing, DayPricing, HourPricing, RegularPricing


class Ticket:
    """This class is responsible for managing the ticket's logic."""

    def __init__(self):
        self.repository = TicketRepository()

    def get_all_tickets(self):
        """This method is responsible for getting all tickets."""
        tickets = self.repository.get_all_tickets()
        return tickets

    def get_ticket_by_id(self, ticket_id: int):
        """This method is responsible for getting a ticket by its id."""
        ticket = self.repository.get_ticket_by_id(ticket_id)
        return ticket

    def get_tickets_by_customer_id(self, customer_id: int):
        """This method is responsible for getting all tickets for a customer by customer_id."""
        tickets = self.repository.get_tickets_by_customer_id(customer_id)
        return tickets

    def create_ticket(self, customer_id: int, showtime_id: int, seat_number: str):
        """This method is responsible for creating a new ticket."""
        base_price = 10
        state = AddedCartState()
        status = state.get_status()

        date = datetime.now()
        customer = CustomerRepository().get_customer_by_id(customer_id)

        is_member = False
        if customer.type_customer == "member":
            is_member = True
            pricing_strategy = MemberPricing().get_price(base_price, date, is_member)
        else:
            if datetime.now().hour >= 15:
                pricing_strategy = HourPricing().get_price(base_price, date, is_member)
            elif datetime.now().weekday() in [1, 2, 6]:
                pricing_strategy = DayPricing().get_price(base_price, date, is_member)
            else:
                pricing_strategy = RegularPricing().get_price(
                    base_price, date, is_member
                )

        seat_repository = SeatRepository()
        seat_repository.update_seat_status(showtime_id, seat_number, "reserved")

        showtime_repository = ShowtimeRepository()
        showtime_repository.rest_available_seats(showtime_id)   

        ticket = self.repository.create_ticket(
            customer_id, showtime_id, seat_number, pricing_strategy, status
        )
        return ticket

    def get_price(self, ticket_id: int):
        """This method is used for obtain the price of a ticket"""
        ticket_repository = TicketRepository()
        ticket = ticket_repository.get_ticket_by_id(ticket_id)
        if not ticket:
            return {"error": "Ticket not found"}
        return {"price": ticket.price}

    def cancel_ticket(self, ticket_id: int):
        """This method is responsible for canceling a ticket."""
        ticket_repository = TicketRepository()
        ticket_data = ticket_repository.get_ticket_by_id(ticket_id)
        if not ticket_data:
            return {"error": "Ticket not found"}

        state = CancelledState()
        status = state.get_status()

        updated_ticket = ticket_repository.update_ticket_status(ticket_id, status)
        return {"message": "Ticket cancelled", "ticket": updated_ticket}
