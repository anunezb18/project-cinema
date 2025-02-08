"""
This class handle the use of the cart item table in the database.
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
from .db_connection import DBConnection

db = DBConnection()


class CartItemDAO(BaseModel):
    """This class is used to define data structure for cart item."""

    cart_id: int
    ticket_id: int


class CartItemRepository:
    """This class handles interactions with the cart_item table in the database."""

    def get_cart_item_by_id(self, cart_item_id):
        """Get a cart item by its ID."""
        query = "SELECT * FROM cart_item WHERE cart_item_id = %s"
        return db.execute_query(query, (cart_item_id,), fetch_one=True)

    def create_cart_item(self, cart_id, ticket_id):
        """Create a new cart item."""
        query = "INSERT INTO cart_item (cart_id, ticket_id) VALUES (%s, %s) RETURNING *"
        return db.execute_query(query, (cart_id, ticket_id), fetch_one=True)

    def update_cart_item(self, cart_item_id, cart_id, ticket_id):
        """Update a cart item."""
        query = "UPDATE cart_item SET cart_id = %s, ticket_id = %s WHERE cart_item_id = %s RETURNING *"
        return db.execute_query(
            query, (cart_id, ticket_id, cart_item_id), fetch_one=True
        )

    def delete_cart_item(self, cart_item_id):
        """Delete a cart item."""
        query = "DELETE FROM cart_item WHERE cart_item_id = %s"
        return db.execute_query(query, (cart_item_id,))

    def get_all_cart_items(self):
        """Get all cart items."""
        query = "SELECT * FROM cart_item"
        return db.execute_query(query, fetch_all=True)

    def get_cart_item_by_ticket_id_and_cart_id(self, cart_id, ticket_id):
        """Get a cart item by its cart_id and ticket_id."""
        query = "SELECT * FROM cart_item WHERE cart_id = %s AND ticket_id = %s"
        return db.execute_query(query, (cart_id, ticket_id), fetch_one=True)

    def get_items_by_customer_id(self, customer_id):
        """Get all cart items by customer_id."""
        query = "SELECT * FROM cart_item WHERE cart_id IN (SELECT cart_id FROM cart WHERE customer_id = %s)"
        return db.execute_query(query, (customer_id,), fetch_all=True)

    def add_item(self, customer_id, ticket_id):
        """Add a ticket to the cart."""
        cart = db.execute_query(
            "SELECT * FROM cart WHERE customer_id = %s", (customer_id,), fetch_one=True
        )
        if not cart:
            return None
        cart_id = cart[0]
        cart_item = self.get_cart_item_by_ticket_id_and_cart_id(cart_id, ticket_id)
        if cart_item:
            return cart_item
        return self.create_cart_item(cart_id, ticket_id)

    def remove_item(self, customer_id, ticket_id):
        """Remove a ticket from the cart."""
        cart = db.execute_query(
            "SELECT * FROM cart WHERE customer_id = %s", (customer_id,), fetch_one=True
        )
        if not cart:
            return None
        cart_id = cart[0]
        cart_item = self.get_cart_item_by_ticket_id_and_cart_id(cart_id, ticket_id)
        if not cart_item:
            return None
        return self.delete_cart_item(cart_item[0])

    def clear_items(self, customer_id):
        """Clear all items from the cart."""
        cart = db.execute_query(
            "SELECT * FROM cart WHERE customer_id = %s", (customer_id,), fetch_one=True
        )
        if not cart:
            return None
        cart_items = self.get_items_by_customer_id(customer_id)
        for cart_item in cart_items:
            self.delete_cart_item(cart_item[0])
        return True
