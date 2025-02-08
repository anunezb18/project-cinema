"""
This class is responsible for managing the cart logic.
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
from backend_python.repositories.cart_item_repository import CartItemRepository
from backend_python.repositories.cart_repository import CartRepository


class Cart:
    """This class contains the logic of the shopping cart and integrates it with the database."""

    def __init__(self):
        self.repository = CartRepository()
        self.item_repository = CartItemRepository()

    def add_to_cart(self, customer_id: int, ticket_id: int):
        """Add a ticket to the cart."""
        return self.item_repository.add_item(customer_id, ticket_id)

    def remove_from_cart(self, customer_id: int, ticket_id: int):
        """Remove a ticket from the cart."""
        return self.item_repository.remove_item(customer_id, ticket_id)

    def clear_cart(self, customer_id: int):
        """Clear the cart."""
        return self.item_repository.clear_items(customer_id)

    def get_items_by_customer_id(self, customer_id: int):
        """Get all items in the cart for a specific customer."""
        return self.item_repository.get_items_by_customer_id(customer_id)


class Command(ABC):
    """Interface base on commands"""

    @abstractmethod
    def execute(self):
        """Method to execute the command"""


class AddToCartCommand(Command):
    """Command to add a ticket to the cart."""

    def __init__(self, cart: Cart, customer_id: int, ticket_id: int):
        self.cart = cart
        self.customer_id = customer_id
        self.ticket_id = ticket_id

    def execute(self):
        return self.cart.add_to_cart(self.customer_id, self.ticket_id)


class RemoveFromCartCommand(Command):
    """Command to remove a ticket from the cart."""

    def __init__(self, cart: Cart, customer_id: int, ticket_id: int):
        self.cart = cart
        self.customer_id = customer_id
        self.ticket_id = ticket_id

    def execute(self):
        return self.cart.remove_from_cart(self.customer_id, self.ticket_id)


class ClearCartCommand(Command):
    """Command to clear the cart."""

    def __init__(self, cart: Cart, customer_id: int):
        self.cart = cart
        self.customer_id = customer_id

    def execute(self):
        return self.cart.clear_cart(self.customer_id)


class GetItemsByCustomerIdCommand(Command):
    """Command to get all items in the cart for a specific customer."""

    def __init__(self, cart: Cart, customer_id: int):
        self.cart = cart
        self.customer_id = customer_id

    def execute(self):
        return self.cart.get_items_by_customer_id(self.customer_id)


class CartInvoker:
    """Class to manage the commands."""

    def __init__(self):
        self.command_history = []

    def execute_command(self, command: Command):
        """Executes a command and stores it in history."""
        result = command.execute()
        self.command_history.append(command)
        return result

    def undo_last_command(self):
        """Undo the last executed command."""
        if self.command_history:
            last_command = self.command_history.pop()
            print(f"Undoing the command: {last_command.__class__.__name__}")
        else:
            print("No commands to undo.")
