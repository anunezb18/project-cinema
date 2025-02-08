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
from backend_python.repositories.admin_repository import AdminRepository
from backend_python.repositories.movie_repository import MovieRepository
from backend_python.repositories.showtime_repository import (
    ShowtimeRepository,
    SeatRepository,
)
from backend_python.repositories.order_repository import OrderRepository


class AdminInterface(ABC):
    """This class is responsible for defining the admin's logic interface."""

    @abstractmethod
    def get_all_admins(self):
        """This method is responsible for get all admins"""

    @abstractmethod
    def get_admin_by_id(self, admin_id):
        """This method is responsible for get an admin by id"""

    @abstractmethod
    def add_movie(self, title, description, genre, release_date, length):
        """This method is responsible for adding a movie."""

    @abstractmethod
    def update_movie(self, movie_id, title, description, genre, release_date, length):
        """This method is responsible for updating a movie."""

    @abstractmethod
    def delete_movie(self, movie_id):
        """This method is responsible for deleting a movie."""

    @abstractmethod
    def update_showtime(self, showtime_id, movie_id, datetime):
        """This method is responsible for updating a showtime."""

    @abstractmethod
    def manage_showtime(self, movie_id, datetime):
        """This method is responsible for managing a showtime."""

    @abstractmethod
    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""


class AdminReal(AdminInterface):
    """This class is responsible for managing the admin's logic."""

    def get_all_admins(self):
        """This method is renposible for get all admins"""
        admin_repository = AdminRepository()
        admins = admin_repository.get_all_admins()
        return admins

    def get_admin_by_id(self, admin_id):
        admin_repository = AdminRepository()
        admin = admin_repository.get_admin_by_id(admin_id)
        return admin

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

    def delete_movie(self, movie_id):
        """This method is responsible for deleting a movie."""
        movie_repository = MovieRepository()
        movie_repository.delete_movie(movie_id)
        return {"message": "Movie deleted successfully."}

    def update_showtime(self, showtime_id, movie_id, datetime):
        """This method is responsible for updating a showtime."""
        showtime_repository = ShowtimeRepository()
        showtime_repository.update_showtime(showtime_id, movie_id, datetime)
        return {"message": "Showtime updated successfully."}

    def manage_showtime(self, movie_id, datetime):
        """This method is responsible for managing a showtime."""
        showtime_repository = ShowtimeRepository()
        showtime_id = showtime_repository.create_showtime(
            movie_id, datetime, available_seats=120
        )

        showtime_id = showtime_repository.get_last_inserted_id()

        seat_repository = SeatRepository()
        rows = ["A", "B", "C", "D", "E", "F"]
        seats_per_row = 20
        for row in rows:
            for seat_number in range(1, seats_per_row + 1):
                seat_repository.create_seat(
                    showtime_id, f"{row}{seat_number}", "available"
                )

        return {"message": "Showtime and seats created successfully."}

    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""
        order_repository = OrderRepository()
        return order_repository.get_all_orders()


class AdminProxy(AdminInterface):
    """This class is responsible for controlling access to the admin's logic."""

    def __init__(self, user_role):
        self.user_role = user_role
        self.admin_real = AdminReal()

    def get_all_admins(self):
        """This method is responsible for get all admins"""
        if self.user_role == "admin":
            return self.admin_real.get_all_admins()
        else:
            return {"error": "Access denied"}

    def get_admin_by_id(self, admin_id):
        if self.user_role == "admin":
            return self.admin_real.get_admin_by_id(admin_id)
        else:
            return {"error": "Access denied"}

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

    def delete_movie(self, movie_id):
        """This method is responsible for deleting a movie."""
        if self.user_role == "admin":
            return self.admin_real.delete_movie(movie_id)
        else:
            return {"error": "Access denied"}

    def update_showtime(self, showtime_id, movie_id, datetime):
        """This method is responsible for updating a showtime."""
        if self.user_role == "admin":
            return self.admin_real.update_showtime(showtime_id, movie_id, datetime)
        else:
            return {"error": "Access denied"}

    def manage_showtime(self, movie_id, datetime):
        """This method is responsible for managing a showtime."""
        if self.user_role == "admin":
            return self.admin_real.manage_showtime(movie_id, datetime)
        else:
            return {"error": "Access denied"}

    # TODO: Implement the view_all_purchases method
    def view_all_purchases(self):
        """This method is responsible for viewing all purchases."""
        if self.user_role == "admin":
            return self.admin_real.view_all_purchases()
        else:
            return {"error": "Access denied"}
