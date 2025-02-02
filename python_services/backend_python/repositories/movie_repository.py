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

from .db_connection import DBConnection

db = DBConnection(
    dbname="cinemacondo",
    user="postgres",
    password="Bullrock",
    host="localhost",
    port=5432,
)


class MovieRepository:
    """This class handles the use of the movie table in the database."""

    def get_movie_by_id(self, movie_id):
        """Get a movie by its id."""
        query = "SELECT * FROM movies WHERE movie_id = %s"
        return db.execute_query(query, (movie_id,), fetch_one=True)

    def create_movie(self, title, description, genre, release_date, length):
        """Create a new movie."""
        query = "INSERT INTO movies (title, description, genre, release_date, length) VALUES (%s, %s, %s, %s, %s) RETURNING *"
        return db.execute_query(
            query, (title, description, genre, release_date, length), fetch_one=True
        )

    def update_movie(self, movie_id, title, description, genre, release_date, length):
        """Update a movie."""
        query = "UPDATE movies SET title = %s, description = %s, genre = %s, release_date = %s, length = %s WHERE movie_id = %s RETURNING *"
        return db.execute_query(
            query,
            (title, description, genre, release_date, length, movie_id),
            fetch_one=True,
        )

    def delete_movie(self, movie_id):
        """Delete a movie."""
        query = "DELETE FROM movies WHERE movie_id = %s"
        return db.execute_query(query, (movie_id,))

    def get_all_movies(self):
        """Get all movies."""
        query = "SELECT * FROM movies"
        return db.execute_query(query, fetch_all=True)
