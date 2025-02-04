"""
This module contains the implementation of the web services of admin class.
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
from backend_python.repositories.admin_repository import AdminRepository
from backend_python.repositories.movie_repository import MovieRepository
from backend_python.repositories.showtime_repository import ShowtimeRepository

router = APIRouter()


@router.post("/create_admin")
async def create_admin(request: Request):
    """This method is responsible for creating an admin."""
    data = await request.json()
    email = data.get("email")

    admin_created = AdminRepository().create_admin(email)

    if admin_created:
        return JSONResponse(
            content={
                "data": admin_created,
                "detail": "Admin created successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Admin creation failed")


@router.get("/get_all_admins")
def get_all_admins():
    """This method is responsible for obtaining all admins."""
    admins = AdminRepository().get_all_admins()
    if admins:
        return JSONResponse(
            content={"data": admins, "detail": "Admins obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No admins found")


@router.get("/get_admin_by_id/{admin_id}")
def get_admin_by_id(admin_id: int):
    """This method is responsible for obtaining an admin by its id."""
    admin = AdminRepository().get_admin_by_id(admin_id)
    if admin:
        return JSONResponse(
            content={"data": admin, "detail": "Admin obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="Admin not found")


@router.post("/add_movie")
async def add_movie(request: Request):
    """This method is responsible for adding a movie."""
    data = await request.json()
    title = data.get("title")
    description = data.get("description")
    genre = data.get("genre")
    release_date = data.get("release_date")
    length = data.get("length")

    movie_created = MovieRepository().create_movie(
        title, description, genre, release_date, length
    )

    if movie_created:
        return JSONResponse(
            content={
                "data": movie_created,
                "detail": "Movie created successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Movie creation failed")


@router.post("/create_showtime")
async def create_showtime(request: Request):
    """This method is responsible for creating a showtime."""
    data = await request.json()
    movie_id = data.get("movie_id")
    datetime = data.get("datetime")
    available_seats = data.get("available_seats")

    showtime_created = ShowtimeRepository().create_showtime(
        movie_id, datetime, available_seats
    )

    if showtime_created:
        return JSONResponse(
            content={
                "detail": "Showtime created successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Showtime creation failed")
