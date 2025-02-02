"""
This class handle the use of the cart table in the database.
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

db = DBConnection(
    dbname="cinemacondo",
    user="postgres",
    password="Bullrock",
    host="localhost",
    port=5432,
)


class CartRepository:
    """This class handles interactions with the cart table in the database."""

    def get_cart_by_customer_id(self, customer_id):
        """Get the cart by its customer_id."""
        query = "SELECT * FROM cart WHERE customer_id = %s"
        return db.execute_query(query, (customer_id,), fetch_one=True)

    def create_cart(self, customer_id):
        """Create a new cart."""
        query = "INSERT INTO cart (customer_id) VALUES (%s) RETURNING *"
        return db.execute_query(query, (customer_id,), fetch_one=True)

    def update_cart(self, cart_id, customer_id):
        """Update the cart."""
        query = "UPDATE cart SET customer_id = %s WHERE cart_id = %s RETURNING *"
        return db.execute_query(query, (customer_id, cart_id), fetch_one=True)

    def delete_cart(self, cart_id):
        """Delete the cart."""
        query = "DELETE FROM cart WHERE cart_id = %s"
        return db.execute_query(query, (cart_id,))

    def get_all_carts(self):
        """Get all carts."""
        query = "SELECT * FROM cart"
        return db.execute_query(query, fetch_all=True)
