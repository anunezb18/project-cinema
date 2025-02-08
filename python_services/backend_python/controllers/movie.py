"""
This class is responsible for managing movie's web services.
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

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from backend_python.services.movie import Movie

router = APIRouter()

services = Movie()


@router.get("/get_all_movies")
def get_all_movies():
    """This method is responsible for obtaining all movies."""
    movies = services.get_all_movies()
    if movies:
        return JSONResponse(
            content={"data": movies, "detail": "Movies obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No movies found")


@router.get("/get_movie_by_id/{movie_id}")
def get_movie_by_id(movie_id: int):
    """This method is responsible for obtaining a movie by its id."""
    movie = services.get_movie_by_id(movie_id)
    if movie:
        return JSONResponse(
            content={"data": movie, "detail": "Movie obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No movie found")


@router.post("/get_movies_by_genre")
async def get_movies_by_genre(request: Request):
    """This method is responsible for obtaining all movies by genre."""
    data = await request.json()
    genre = data.get("genre")
    movies = services.get_movies_by_genre(genre)
    if movies:
        return JSONResponse(
            content={"data": movies, "detail": "Movies obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No movies found")
