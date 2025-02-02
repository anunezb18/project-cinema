"""
This module contains the implementation of the Admin functionality using the Proxy pattern.
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

from abc import ABC, abstractmethod
from backend_python.repositories.movie_repository import MovieRepository
from backend_python.repositories.showtime_repository import ShowtimeRepository
from backend_python.repositories.order_repository import OrderRepository


class AdminInterface(ABC):
    """This class is responsible for defining the admin's logic interface."""

    @abstractmethod
    def add_movie(self, title, description, genre, release_date, length):
        """This method is responsible for adding a movie."""

    @abstractmethod
    def update_movie(self, movie_id, title, description, genre, release_date, length):
        """This method is responsible for updating a movie."""

    @abstractmethod
    def manage_showtime(self, movie_id, datetime, available_seats):
        """This method is responsible for managing a showtime."""

    @abstractmethod
    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""


class AdminReal(AdminInterface):
    """This class is responsible for managing the admin's logic."""

    def add_movie(self, title, description, genre, release_date, length):
        """This method is responsible for adding a movie."""
        movie_repository = MovieRepository()
        movie_repository.create_movie(title, description, genre, release_date, length)
        return {"message": "Movie created successfully."}

    def update_movie(self, movie_id, title, description, genre, release_date, length):
        """This method is responsible for updating a movie."""
        movie_repository = MovieRepository()
        movie_repository.update_movie(
            movie_id, title, description, genre, release_date, length
        )
        return {"message": "Movie updated successfully."}

    def manage_showtime(self, movie_id, datetime, available_seats):
        """This method is responsible for managing a showtime."""
        showtime_repository = ShowtimeRepository()
        showtime_repository.create_showtime(movie_id, datetime, available_seats)
        return {"message": "Showtime created successfully."}

    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""
        order_repository = OrderRepository()
        return order_repository.get_all_orders()


class AdminProxy(AdminInterface):
    """This class is responsible for controlling access to the admin's logic."""

    def __init__(self, user_role):
        self.user_role = user_role
        self.admin_real = AdminReal()

    def add_movie(self, title, description, genre, release_date, length):
        """This method is responsible for adding a movie."""
        if self.user_role == "admin":
            return self.admin_real.add_movie(
                title, description, genre, release_date, length
            )
        else:
            return {"error": "Access denied"}

    def update_movie(self, movie_id, title, description, genre, release_date, length):
        """This method is responsible for updating a movie."""
        if self.user_role == "admin":
            return self.admin_real.update_movie(
                movie_id, title, description, genre, release_date, length
            )
        else:
            return {"error": "Access denied"}

    def manage_showtime(self, movie_id, datetime, available_seats):
        """This method is responsible for managing a showtime."""
        if self.user_role == "admin":
            return self.admin_real.manage_showtime(movie_id, datetime, available_seats)
        else:
            return {"error": "Access denied"}

    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""
        if self.user_role == "admin":
            return self.admin_real.view_all_purchases()
        else:
            return {"error": "Access denied"}
