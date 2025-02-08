"""
This class handle the use of the movie table in the database.
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


class UserDAO(BaseModel):
    """This class is used to define data structure for user."""

    email: str
    name: str
    password: str
    role: str


class UserRepository:
    """This class handle the use of the user table in the database."""

    def create_user(self, email, name, password, role) -> UserDAO:
        """Create a new user."""
        query = "INSERT INTO users (email, name, password, role) VALUES (%s, %s, %s, %s) RETURNING email, name, password, role"
        result = db.execute_query(query, (email, name, password, role), fetch_one=True)
        if result:
            return UserDAO(
                email=result[0], name=result[1], password=result[2], role=result[3]
            )
        return None

    def update_user(self, email, name, password) -> UserDAO:
        """Update a user."""
        query = "UPDATE users SET name = %s, password = %s WHERE email = %s RETURNING email, name, password, role"
        result = db.execute_query(query, (name, password, email), fetch_one=True)
        if result:
            return UserDAO(
                email=result[0], name=result[1], password=result[2], role=result[3]
            )
        return None

    def delete_user(self, email) -> bool:
        """Delete a user."""
        user = self.get_user_by_email(email)
        if not user:
            return False

        query = "DELETE FROM users WHERE email = %s"
        db.execute_query(query, (email,))
        return True

    def get_all_users(self) -> list[UserDAO]:
        """Get all users."""
        query = "SELECT email, name, password, role FROM users"
        results = db.execute_query(query, fetch_all=True)
        return [
            UserDAO(email=row[0], name=row[1], password=row[2], role=row[3])
            for row in results
        ]

    def get_user_by_email(self, email) -> UserDAO:
        """Get a user by its email."""
        query = "SELECT email, name, password, role FROM users WHERE email = %s"
        result = db.execute_query(query, (email,), fetch_one=True)
        if result:
            return UserDAO(
                email=result[0], name=result[1], password=result[2], role=result[3]
            )
        return None
    
    def get_user_by_email_and_password(self, email, password) -> UserDAO:
        """Get a user by its email and password."""
        query = "SELECT email, name, password, role FROM users WHERE email = %s AND password = %s"
        result = db.execute_query(query, (email, password), fetch_one=True)
        if result:
            return UserDAO(
                email=result[0], name=result[1], password=result[2], role=result[3]
            )
        return None
    
    def login(self, email, password) -> bool:
        """Login a user."""
        query = "SELECT email, password FROM users WHERE email = %s AND password = %s"
        result = db.execute_query(query, (email, password), fetch_one=True)
        return result is not None