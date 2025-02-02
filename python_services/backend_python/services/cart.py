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

    def __init__(self, customer_id: int):
        self.cart_repository = CartRepository()
        self.cart_item_repository = CartItemRepository()
        self.customer_id = customer_id
        self.cart = self.cart_repository.get_cart_by_customer_id(customer_id)

        if not self.cart:
            self.cart = self.cart_repository.create_cart(customer_id)

    def add_to_cart(self, ticket_id: int):
        """Adds a ticket to the cart (in the database)."""
        
        existing_item = self.cart_item_repository.get_cart_item_by_ticket_id_and_cart_id(
            self.cart["cart_id"], ticket_id
        )
        
        if not existing_item:

            self.cart_item_repository.create_cart_item(
                self.cart["cart_id"], ticket_id
            )
            return {"message": f"Ticket {ticket_id} added successfully."}
        
        return {"error": f"Ticket {ticket_id} is already in the cart."}


    def remove_from_cart(self, ticket_id: int):
        """Removes a ticket from the cart (in the database)."""
        item = self.cart_item_repository.get_cart_item_by_id(ticket_id)
        if item:
            self.cart_item_repository.delete_cart_item(item["cart_item_id"])
            return {"message": f"Ticket {ticket_id} removed successfully."}
        return {"error": f"Ticket {ticket_id} not found in the cart."}

    def clear_cart(self):
        """Clears all items from the cart (in the database)."""
        cart_items = self.cart_item_repository.get_all_cart_items()
        for item in cart_items:
            self.cart_item_repository.delete_cart_item(item["cart_item_id"])
        return {"message": "Cart cleared successfully."}

    def get_items(self):
        """Returns all items in the cart (retrieved from the database)."""
        cart_items = self.cart_item_repository.get_all_cart_items()
        return cart_items


class Command(ABC):
    """Interface base on commands"""

    @abstractmethod
    def execute(self):
        """Method to execute the command"""


class AddToCartCommand(Command):
    """Command to add a ticket to the cart."""

    def __init__(self, cart: Cart, ticket_id: int):
        self.cart = cart
        self.ticket_id = ticket_id

    def execute(self):
        return self.cart.add_to_cart(self.ticket_id)


class RemoveFromCartCommand(Command):
    """Command to remove a ticket from the cart."""

    def __init__(self, cart: Cart, ticket_id: int):
        self.cart = cart
        self.ticket_id = ticket_id

    def execute(self):
        return self.cart.remove_from_cart(self.ticket_id)


class ClearCartCommand(Command):
    """Command to clear the cart."""

    def __init__(self, cart: Cart):
        self.cart = cart

    def execute(self):
        return self.cart.clear_cart()


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
