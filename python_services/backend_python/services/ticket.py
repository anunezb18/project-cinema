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
from pydantic import BaseModel
from backend_python.repositories.ticket_repository import TicketRepository
from .ticket_state import TicketState
from .pricing_stategy import PricingStrategy


class Ticket(BaseModel):
    """This class is responsible for managing the ticket's logic."""

    strategy: PricingStrategy
    base_price: float = 5.0
    ticket_id: int
    movie_id: int
    showtime_id: int
    seat_number: int
    status: TicketState

    class Config:
        """This class is for pydantic configuration."""

        arbitrary_types_allowed = True

    def select_movie(
        self,
        customer_id: int,
        showtime_id: int,
        status: str,
        seat_number: str,
        price: float,
    ):
        """This method is responsible for selecting a movie."""
        ticket_repository = TicketRepository()
        ticket = ticket_repository.create_ticket(
            customer_id, showtime_id, seat_number, price, status
        )
        return {"message": "Ticket purchased successfully", "ticket": ticket}

    def get_ticket_details(self, ticket_id: int):
        """This method is responsible for getting the ticket details."""
        ticket_repository = TicketRepository()
        ticket_details = ticket_repository.get_tickets_details_by_id(ticket_id)
        if not ticket_details:
            return {"error": "Ticket not found"}
        return {"ticket_details": ticket_details}

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
        ticket = ticket_repository.get_ticket_by_id(ticket_id)
        if not ticket:
            return {"error": "Ticket not found"}
        ticket.status = "cancelled"
        ticket_repository.update_ticket(
            ticket.ticket_id,
            ticket.customer_id,
            ticket.showtime_id,
            ticket.seat_number,
            ticket.price,
            ticket.status,
        )
        return {"message": "Ticket canceled successfully"}

    def get_final_price(self, date: datetime = None, is_member: bool = False) -> float:
        """This method is responsible for getting the final price of a ticket."""
        return self.strategy.get_price(self.base_price, date, is_member)
