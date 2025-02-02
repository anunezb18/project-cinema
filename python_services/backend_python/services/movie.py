"""
This class is responsible for managing the cart logic.
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
from backend_python.repositories.movie_repository import MovieRepository


class Movie(BaseModel):
    """This class is responsible for managing the movie logic."""

    movieId: int
    title: str
    description: str
    genre: str
    releaseDate: str
    length: str

    def get_movie_details(self, movie_id):
        """This method is responsible for getting the details of a movie."""
        movie_repository = MovieRepository()
        movie = movie_repository.get_movie_by_id(movie_id)
        return movie
