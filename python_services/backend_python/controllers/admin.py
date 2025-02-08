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
from backend_python.services.admin_interface import AdminProxy

router = APIRouter()

user_role = "admin"  # pylint: disable=invalid-name
services = AdminProxy(user_role)


@router.get("/get_all_admins")
def get_all_admins():
    """This method is responsible for obtaining all admins."""
    admins = services.get_all_admins()
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
    admin = services.get_admin_by_id(admin_id)
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

    movie_created = services.add_movie(title, description, genre, release_date, length)

    return movie_created


@router.post("/update_movie")
async def update_movie(request: Request):
    """This method is responsible for updating a movie."""
    data = await request.json()
    movie_id = data.get("movie_id")
    title = data.get("title")
    description = data.get("description")
    genre = data.get("genre")
    release_date = data.get("release_date")
    length = data.get("length")

    movie_updated = services.update_movie(
        movie_id, title, description, genre, release_date, length
    )

    if movie_updated:
        return JSONResponse(
            content={"detail": "Movie updated successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=400, detail="Movie update failed")


@router.delete("/delete_movie/{movie_id}")
def delete_movie(movie_id: int):
    """This method is responsible for deleting a movie."""
    movie_deleted = services.delete_movie(movie_id)
    if movie_deleted:
        return JSONResponse(
            content={"detail": "Movie deleted successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=400, detail="Movie deletion failed")


@router.post("/create_showtime")
async def create_showtime(request: Request):
    """This method is responsible for creating a showtime."""
    data = await request.json()
    movie_id = data.get("movie_id")
    datetime = data.get("datetime")

    showtime_created = services.manage_showtime(movie_id, datetime)

    if showtime_created:
        return JSONResponse(
            content={
                "detail": "Showtime created successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Showtime creation failed")


@router.post("/update_showtime")
async def update_showtime(request: Request):
    """This method is responsible for updating a showtime."""
    data = await request.json()
    showtime_id = data.get("showtime_id")
    movie_id = data.get("movie_id")
    datetime = data.get("datetime")

    showtime_updated = services.update_showtime(showtime_id, movie_id, datetime)

    if showtime_updated:
        return JSONResponse(
            content={"detail": "Showtime updated successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=400, detail="Showtime update failed")
