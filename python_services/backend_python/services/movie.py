"""
This class is responsible for managing the movie logic.
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

from backend_python.repositories.movie_repository import MovieRepository


class Movie():
    """This class is responsible for managing the movie logic."""

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_all_movies(self):
        """This method is responsible for getting all movies."""
        return self.movie_repository.get_all_movies()

    def get_movie_by_id(self, movie_id: int):
        """This method is responsible for getting a movie by id."""
        return self.movie_repository.get_movie_by_id(movie_id)

    def get_movies_by_genre(self, genre: str):
        """This method is responsible for getting all movies by genre."""
        return self.movie_repository.get_movies_by_genre(genre)
