"""
This class handle the use of the customer table in the database.
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
from .cart_repository import CartRepository

db = DBConnection()


class CustomerDAO(BaseModel):
    """This class is used to define data structure for customer."""

    customer_id: int
    email: str
    type_customer: str
    cart_id: int | None = None


class CustomerRepository:
    """This class handles the use of the customer table in the database."""

    def create_customer(self, email, type_customer) -> CustomerDAO:
        """Create a new customer."""
        query = "INSERT INTO customers (email, type_customer) VALUES (%s, %s) RETURNING customer_id, email, type_customer"
        result = db.execute_query(query, (email, type_customer), fetch_one=True)
        if result:
            customer = CustomerDAO(
                customer_id=result[0],
                email=result[1],
                type_customer=result[2],
                cart_id=None,
            )
            cart_repository = CartRepository()
            cart = cart_repository.create_cart(customer.customer_id)
            if cart:
                self.asign_cart(customer.customer_id, cart["cart_id"])
                customer.cart_id = cart["cart_id"]
            return customer
        return None

    def asign_cart(self, customer_id, cart_id) -> bool:
        """Assign a cart to a customer."""
        query = "UPDATE customers SET cart_id = %s WHERE customer_id = %s"
        result = db.execute_query(query, (cart_id, customer_id))
        return result is not None

    def get_customer_by_id(self, customer_id) -> CustomerDAO:
        """Get a customer by its id."""
        query = "SELECT customer_id, email, type_customer, cart_id FROM customers WHERE customer_id = %s"
        result = db.execute_query(query, (customer_id,), fetch_one=True)
        if result:
            return CustomerDAO(
                customer_id=result[0],
                email=result[1],
                type_customer=result[2],
                cart_id=result[3],
            )
        return None

    def get_all_customers(self) -> list[CustomerDAO]:
        """Get all customers."""
        query = "SELECT customer_id, email, type_customer, cart_id FROM customers"
        results = db.execute_query(query, fetch_all=True)
        return [
            CustomerDAO(
                customer_id=row[0],
                email=row[1],
                type_customer=row[2],
                cart_id=row[3],
            )
            for row in results
        ]

    def acquire_membership(self, customer_id, expiration_date, status) -> bool:
        """Acquire a membership."""
        query = "INSERT INTO memberships (customer_id, expiration_date, status) VALUES (%s, %s, %s)"
        result = db.execute_query(query, (customer_id, expiration_date, status))
        return result is not None

    def update_role(self, customer_id, role) -> bool:
        """Update the role of a customer."""
        query = "UPDATE customers SET type_customer = %s WHERE customer_id = %s"
        result = db.execute_query(query, (role, customer_id))
        email = self.get_customer_by_id(customer_id).email
        query2 = "UPDATE users SET role = %s WHERE email = %s"
        result2 = db.execute_query(query2, (role, email))
        return result is not None and result2 is not None
