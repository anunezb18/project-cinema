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

from .db_connection import DBConnection

db = DBConnection()


class CartItemRepository:
    """This class handles interactions with the cart_item table in the database."""

    def get_cart_item_by_id(self, cart_item_id):
        """Get a cart item by its ID."""
        query = "SELECT * FROM cart_items WHERE cart_item_id = %s"
        return db.execute_query(query, (cart_item_id,), fetch_one=True)

    def create_cart_item(self, cart_id, ticket_id):
        """Create a new cart item."""
        query = (
            "INSERT INTO cart_items (cart_id, ticket_id) VALUES (%s, %s) RETURNING *"
        )
        return db.execute_query(query, (cart_id, ticket_id), fetch_one=True)

    def update_cart_item(self, cart_item_id, cart_id, ticket_id):
        """Update a cart item."""
        query = "UPDATE cart_items SET cart_id = %s, ticket_id = %s WHERE cart_item_id = %s RETURNING *"
        return db.execute_query(
            query, (cart_id, ticket_id, cart_item_id), fetch_one=True
        )

    def delete_cart_item(self, cart_item_id):
        """Delete a cart item."""
        query = "DELETE FROM cart_items WHERE cart_item_id = %s"
        return db.execute_query(query, (cart_item_id,))

    def get_all_cart_items(self):
        """Get all cart items."""
        query = "SELECT * FROM cart_items"
        return db.execute_query(query, fetch_all=True)

    def get_cart_item_by_ticket_id_and_cart_id(self, cart_id, ticket_id):
        """Get a cart item by its cart_id and ticket_id."""
        query = "SELECT * FROM cart_items WHERE cart_id = %s AND ticket_id = %s"
        return db.execute_query(query, (cart_id, ticket_id), fetch_one=True)