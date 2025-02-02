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

from .db_connection import DBConnection

db = DBConnection(
    dbname="cinemacondo",
    user="postgres",
    password="Bullrock",
    host="localhost",
    port=5432,
)


class ShowtimeRepository:
    """This class handles the use of the showtime table in the database."""

    def get_showtime_by_id(self, showtime_id):
        """Get a showtime by its id."""
        query = "SELECT * FROM showtimes WHERE showtime_id = %s"
        return db.execute_query(query, (showtime_id,), fetch_one=True)

    def create_showtime(self, movie_id, datetime, available_seats):
        """Create a new showtime."""
        query = "INSERT INTO showtimes (movie_id, datetime, available_seats) VALUES (%s, %s, %s) RETURNING *"
        return db.execute_query(
            query, (movie_id, datetime, available_seats), fetch_one=True
        )

    def update_showtime(self, showtime_id, movie_id, datetime, available_seats):
        """Update a showtime."""
        query = "UPDATE showtimes SET movie_id = %s, datetime = %s, available_seats = %s WHERE showtime_id = %s RETURNING *"
        return db.execute_query(
            query, (movie_id, datetime, available_seats, showtime_id), fetch_one=True
        )

    def delete_showtime(self, showtime_id):
        """Delete a showtime."""
        query = "DELETE FROM showtimes WHERE showtime_id = %s"
        return db.execute_query(query, (showtime_id,))

    def get_all_showtimes(self):
        """Get all showtimes."""
        query = "SELECT * FROM showtimes"
        return db.execute_query(query, fetch_all=True)
