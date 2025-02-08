"""
This class is responsible for managing the ticket's status and implements the state pattern.
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

from abc import ABC, abstractmethod

class TicketState(ABC):
    """Base class for the ticket state using the State pattern."""

    @abstractmethod
    def cancel_ticket(self, ticket):
        """Attempts to cancel the ticket. Changes the state if allowed."""
        pass

    @abstractmethod
    def use_ticket(self, ticket):
        """Attempts to use the ticket. Changes the state if allowed."""
        pass

    @abstractmethod
    def get_status(self):
        """Returns the current state name."""
        pass


class AddedCartState(TicketState):
    """State: The ticket has been added to the cart but not yet paid."""

    def cancel_ticket(self, ticket):
        ticket.set_state(CancelledState())
        return "Ticket cancelled."

    def use_ticket(self, ticket):
        ticket.set_state(PaidState())
        return "Ticket paid."

    def get_status(self):
        return "added_to_cart"


class PaidState(TicketState):
    """State: The ticket has been paid and can be used."""

    def cancel_ticket(self, ticket):
        ticket.set_state(CancelledState())
        return "Ticket cancelled."

    def use_ticket(self, ticket):
        ticket.set_state(UsedState())
        return "Ticket used."

    def get_status(self):
        return "paid"


class UsedState(TicketState):
    """State: The ticket has been used and cannot be reused or cancelled."""

    def cancel_ticket(self, ticket):
        return "Cannot cancel a used ticket."

    def use_ticket(self, ticket):
        return "Ticket already used."

    def get_status(self):
        return "used"


class CancelledState(TicketState):
    """State: The ticket has been cancelled and cannot be used."""

    def cancel_ticket(self, ticket):
        return "Ticket already cancelled."

    def use_ticket(self, ticket):
        return "Cannot use a cancelled ticket."

    def get_status(self):
        return "cancelled"


class Ticket:
    """The Context class that maintains a reference to a TicketState instance."""

    def __init__(self):
        self._state = AddedCartState()  # Default state

    def set_state(self, state: TicketState):
        """Changes the ticket's state."""
        self._state = state

    def cancel(self):
        """Requests the ticket to be cancelled."""
        return self._state.cancel_ticket(self)

    def use(self):
        """Requests the ticket to be used."""
        return self._state.use_ticket(self)

    def get_status(self):
        """Returns the current ticket status."""
        return self._state.get_status()