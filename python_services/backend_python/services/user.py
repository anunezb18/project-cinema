"""
This class is responsible for managing the user's logic.
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
from abc import ABC
from pydantic import BaseModel
from backend_python.repositories.user_repository import UserRepository


class User(BaseModel, ABC):
    """This class has the services for user management."""

    name: str
    email: str
    password: str

    def signup(self, name: str, email: str, password: str):
        """This method is responsible for registering a user."""
        user_repository = UserRepository()
        user_repository.create_user(email, name, password)
        return {"message": "User created successfully."}

    def login(self, email: str, password: str):
        """This method is responsible for logging in a user."""
        user_repository = UserRepository()
        user = user_repository.get_user_by_email_and_password(email, password)
        if user:
            return {"message": "User logged in successfully."}
        return {"message": "User not found."}

    def log_out(self):
        """This method is responsible for logging out a user."""
        return {"message": "User logged out successfully."}

    def update_info(self, name: str, email: str, password: str):
        """This method is responsible for updating a user's information."""
        user_repository = UserRepository()
        user_repository.update_user(email, name, password)
        return {"message": "User updated successfully."}
