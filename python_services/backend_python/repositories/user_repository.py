"""
This class handle the use of the user table in the database.
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


class UserRepository:
    """This class handle the use of the user table in the database."""

    def get_user_by_email(self, email):
        """Get a user by its email."""
        query = "SELECT * FROM users WHERE email = %s"
        return db.execute_query(query, (email,), fetch_one=True)

    def create_user(self, email, name, password):
        """Create a new user."""
        query = (
            "INSERT INTO users (email, name, password) VALUES (%s, %s, %s) RETURNING *"
        )
        return db.execute_query(query, (email, name, password), fetch_one=True)

    def update_user(self, email, name, password):
        """Update a user."""
        query = "UPDATE users SET name = %s, password = %s WHERE email = %s RETURNING *"
        return db.execute_query(query, (name, password, email), fetch_one=True)

    def delete_user(self, email):
        """Delete a user."""
        query = "DELETE FROM users WHERE email = %s"
        return db.execute_query(query, (email,))

    def get_all_users(self):
        """Get all users."""
        query = "SELECT * FROM users"
        return db.execute_query(query, fetch_all=True)

    def get_user_by_email_and_password(self, email, password):
        """Get a user by its email and password."""
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        return db.execute_query(query, (email, password), fetch_one=True)
