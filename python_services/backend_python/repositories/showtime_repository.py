"""
This class handle the use of the showtime table in the database.
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


class ShowtimeDAO(BaseModel):
    """Showtime data access object."""

    showtime_id: int
    movie_id: int
    datetime: str
    available_seats: int


class ShowtimeRepository:
    """This class handles the use of the showtime table in the database."""

    def get_all_showtimes(self) -> ShowtimeDAO:
        """Get all showtimes."""
        query = "SELECT * FROM showtimes"
        return db.execute_query(query, fetch_all=True)

    def get_showtime_by_id(self, showtime_id) -> ShowtimeDAO:
        """Get a showtime by its id."""
        query = "SELECT * FROM showtimes WHERE showtime_id = %s"
        return db.execute_query(query, (showtime_id,), fetch_one=True)

    def get_seat_availability(self, showtime_id):
        """Get the seat availability of a showtime."""
        query = "SELECT seat_number, status FROM seats WHERE showtime_id = %s"
        return db.execute_query(query, (showtime_id,), fetch_all=True)

    def create_showtime(self, movie_id, datetime, available_seats):
        """Create a new showtime."""
        query = "INSERT INTO showtimes (movie_id, datetime, available_seats) VALUES (%s, %s, %s) RETURNING *"
        return db.execute_query(
            query, (movie_id, datetime, available_seats), fetch_one=True
        )

    def update_showtime(self, showtime_id, movie_id, datetime):
        """Update a showtime."""
        query = "UPDATE showtimes SET movie_id = %s, datetime = %s WHERE showtime_id = %s RETURNING *"
        return db.execute_query(
            query, (movie_id, datetime, showtime_id), fetch_one=True
        )

    def delete_showtime(self, showtime_id):
        """Delete a showtime."""
        query = "DELETE FROM showtimes WHERE showtime_id = %s"
        return db.execute_query(query, (showtime_id,))

    def get_last_inserted_id(self):
        """Get the last inserted showtime_id."""
        query = "SELECT lastval()"
        result = db.execute_query(query, fetch_one=True)
        return result[0] if result else None

    def rest_available_seats(self, showtime_id):
        """Rest available seats of a showtime."""
        query = "UPDATE showtimes SET available_seats = available_seats - 1 WHERE showtime_id = %s RETURNING *"
        return db.execute_query(query, (showtime_id,), fetch_one=True)

class SeatRepository:
    """This class handles the use of the seat table in the database."""

    def create_seat(self, showtime_id, seat_number, status):
        """Create a seat for a showtime."""
        query = (
            "INSERT INTO seats (showtime_id, seat_number, status) VALUES (%s, %s, %s)"
        )
        db.execute_query(query, (showtime_id, seat_number, status))

    def update_seat_status(self, showtime_id, seat_number, status):
        """Update the status of a seat."""
        query = (
            "UPDATE seats SET status = %s WHERE showtime_id = %s AND seat_number = %s"
        )
        db.execute_query(query, (status, showtime_id, seat_number))
