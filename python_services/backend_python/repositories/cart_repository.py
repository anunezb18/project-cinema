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

from pydantic import BaseModel
from .db_connection import DBConnection

db = DBConnection()

class CartDAO(BaseModel):
    """This class is used to define data structure for cart."""

    cart_id: int
    customer_id: int
class CartRepository:
    """This class handles interactions with the cart table in the database."""

    def get_cart_by_customer_id(self, customer_id):
        """Get the cart by its customer_id."""
        query = "SELECT * FROM cart WHERE customer_id = %s"
        return db.execute_query(query, (customer_id,), fetch_one=True)

    def create_cart(self, customer_id):
        """Create a new cart."""
        existing_cart = self.get_cart_by_customer_id(customer_id)
        if existing_cart:
            return {
                "cart_id": existing_cart[0],
                "customer_id": existing_cart[1]
            }

        query = "INSERT INTO cart (customer_id) VALUES (%s) RETURNING cart_id, customer_id"
        result = db.execute_query(query, (customer_id,), fetch_one=True)
        if result:
            return {
                "cart_id": result[0],
                "customer_id": result[1]
            }
        return None
