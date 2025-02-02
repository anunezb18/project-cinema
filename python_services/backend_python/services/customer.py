"""
This class is responsible for managing the customer's logic.
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

from pydantic import BaseModel
from backend_python.repositories.cart_item_repository import CartItemRepository
from backend_python.repositories.ticket_repository import TicketRepository
from backend_python.repositories.membership_repository import MembershipRepository
from .cart import Cart


class Customer(BaseModel):
    """This class is responsible for managing the customer's logic."""

    cart: Cart

    def add_to_cart(self, cart_id, ticket_id):
        """This method is responsible for adding a movie to the cart."""
        cart_repository = CartItemRepository()
        cart_repository.create_cart_item(cart_id, ticket_id)
        return {"message": "Ticket added to cart successfully."}

    def view_cart(self):
        """This method is responsible for viewing the cart."""
        cart_item_repository = CartItemRepository()
        return cart_item_repository.get_all_cart_items()

    def view_tickets(self, customer_id):
        """This method is responsible for viewing the tickets."""
        ticket_repository = TicketRepository()
        return ticket_repository.get_tickets_by_customer_id(customer_id)


class RegularCustomer(Customer):
    """This class is responsible for managing the regular customer's logic."""



class MemberCustomer(Customer):
    """This class is responsible for managing the member customer's logic."""

    membership: str

    def add_membership(self, customer_id, expiration_date, status):
        """This method is responsible for adding a membership."""
        membership_repository = MembershipRepository()
        membership_repository.create_membership(customer_id, expiration_date, status)
        return {"message": "Membership created successfully."}

    def view_membership(self, customer_id):
        """This method is responsible for viewing the membership."""
        membership_repository = MembershipRepository()
        return membership_repository.get_membership_by_customer_id(customer_id)
