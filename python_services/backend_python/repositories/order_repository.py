"""
This class handle the use of the order table in the database.
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
class OrderRepository:
    """This class handles the use of the order table in the database."""

    def create_order(self, customer_id, total_price):
        """Create a new order."""
        query = (
            "INSERT INTO orders (customer_id, total_price) VALUES (%s, %s) RETURNING *"
        )
        return db.execute_query(query, (customer_id, total_price), fetch_one=True)

    def get_order_by_id(self, order_id):
        """Get an order by its ID."""
        query = "SELECT * FROM orders WHERE order_id = %s"
        return db.execute_query(query, (order_id,), fetch_one=True)

    def update_order(self, order_id, customer_id, total_price):
        """Update an order."""
        query = "UPDATE orders SET customer_id = %s, total_price = %s WHERE order_id = %s RETURNING *"
        return db.execute_query(
            query, (customer_id, total_price, order_id), fetch_one=True
        )

    def delete_order(self, order_id):
        """Delete an order."""
        query = "DELETE FROM orders WHERE order_id = %s"
        return db.execute_query(query, (order_id,))

    def get_all_orders(self):
        """Get all orders."""
        query = "SELECT * FROM orders"
        return db.execute_query(query, fetch_all=True)
