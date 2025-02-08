"""
This class is responsible for managing the showtime logic.
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

from backend_python.repositories.showtime_repository import ShowtimeRepository

class Showtime():
    """This class is responsible for managing the showtime's logic."""

    def __init__(self):
        self.showtime_repository = ShowtimeRepository()

    def get_all_showtimes(self):
        """This method is responsible for getting all the showtimes."""
        return ShowtimeRepository().get_all_showtimes()
    
    def get_showtime_by_id(self, showtime_id: int):
        """This method is responsible for getting a showtime by its id."""
        return ShowtimeRepository().get_showtime_by_id(showtime_id)

    def get_seat_availability(self, showtime_id: int) -> int:
        """This method is responsible for getting the seat availability of a showtime."""
        return ShowtimeRepository().get_seat_availability(showtime_id)
