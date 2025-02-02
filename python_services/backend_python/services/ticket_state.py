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
    """Clase base para el estado del ticket usando el patrón State."""

    @abstractmethod
    def cancel_ticket(self, ticket):
        """Cambia el estado del ticket a cancelado."""

    @abstractmethod
    def use_ticket(self, ticket):
        """Cambia el estado del ticket a usado."""

    @abstractmethod
    def get_status(self):
        """Devuelve el estado actual del ticket."""


class PaidState(TicketState):
    """Estado 'pagado' de un ticket."""

    def cancel_ticket(self, ticket):
        ticket.status = CancelledState()
        return "Ticket cancelled"

    def use_ticket(self, ticket):
        ticket.status = UsedState()
        return "Ticket used"

    def get_status(self):
        return "paid"


class UsedState(TicketState):
    """Estado 'usado' de un ticket."""

    def cancel_ticket(self, ticket):
        return "Cannot cancel a used ticket"

    def use_ticket(self, ticket):
        return "Ticket already used"

    def get_status(self):
        return "used"


class CancelledState(TicketState):
    """Estado 'cancelado' de un ticket."""

    def cancel_ticket(self, ticket):
        return "Ticket already cancelled"

    def use_ticket(self, ticket):
        return "Cannot use a cancelled ticket"

    def get_status(self):
        return "cancelled"
