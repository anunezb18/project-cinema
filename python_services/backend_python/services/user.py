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
from backend_python.repositories.user_repository import UserRepository
from .user_factory import UserFactory


class User(ABC):
    """This class has the services for user management."""

    def __init__(self):
        self.repository = UserRepository()

    def signup(self, name: str, email: str, password: str, role: str):
        """This method is responsible for registering a user.
        
        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.
            role (str): The role of the user.
            
        Returns:
            dict: A dictionary with the message of the operation.
        """
        user_factory = UserFactory()
        user = user_factory.create_user(name, email, password, role)
        if user:
            return {"detail": "User created successfully."}
        return {"detail": "User creation failed."}

    def update(self, name: str, email: str, password: str):
        """This method is responsible for updating a user.
        
        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            dict: A dictionary with the message of the operation
        """
        user = self.repository.update_user(email, name, password)
        if user:
            return {"detail": "User updated successfully."}
        return {"detail": "User not found."}
    
    def delete_user(self, email: str):
        """This method is responsible for deleting a user.
        
        Args:
            email (str): The email of the user.

        Returns:
            dict: A dictionary with the message of the operation
        """
        user_deleted = self.repository.delete_user(email)
        if user_deleted:
            return {"detail": "User deleted successfully."}
        return {"detail": "User not found."}

    def get_all__users(self):
        """This method is responsible for getting all users.
        
        Returns:
            list: A list with all users.
        """
        return self.repository.get_all_users()
    
    def get_user_by_email(self, email: str):
        """This method is responsible for getting a user by its email.
        
        Args:
            email (str): The email of the user.
            
        Returns:
            dict: A dictionary with the user.
        """
        return self.repository.get_user_by_email(email)
    
    def login(self, email: str, password: str):
        """This method is responsible for logging in a user.
        
        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            
        Returns:
            dict: A dictionary with the message of the operation.
        """
        user = self.repository.get_user_by_email_and_password(email, password)
        if user:
            return {"detail": "User logged in successfully."}
        return {"detail": "User not found."}
