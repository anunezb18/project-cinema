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

from .db_connection import DBConnection

db = DBConnection()

class CustomerRepository:
    """This class handles the use of the customer table in the database."""

    def get_customer_by_email(self, email):
        """Get a customer by its email."""
        query = "SELECT * FROM customers WHERE email = %s"
        return db.execute_query(query, (email,), fetch_one=True)

    def create_customer(self, email):
        """Create a new customer."""
        query = "INSERT INTO customers (email) VALUES (%s) RETURNING *"
        return db.execute_query(query, (email,), fetch_one=True)

    def update_customer(self, customer_id, email):
        """Update a customer."""
        query = "UPDATE customers SET email = %s WHERE customer_id = %s RETURNING *"
        return db.execute_query(query, (email, customer_id), fetch_one=True)

    def delete_customer(self, customer_id):
        """Delete a customer."""
        query = "DELETE FROM customers WHERE customer_id = %s"
        return db.execute_query(query, (customer_id,))

    def get_all_customers(self):
        """Get all customers."""
        query = "SELECT * FROM customers"
        return db.execute_query(query, fetch_all=True)
