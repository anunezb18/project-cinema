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

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from backend_python.services.showtime import Showtime

router = APIRouter()

services = Showtime()


@router.get("/get_all_showtimes")
def get_all_showtimes():
    """This method is responsible for obtaining all showtimes."""
    showtimes = services.get_all_showtimes()
    if showtimes:
        showtimes_list = [
            {
                "showtime_id": showtime[0],
                "movie_id": showtime[1],
                "datetime": showtime[2].strftime("%Y-%m-%d %H:%M:%S"),
                "available_seats": showtime[3],
            }
            for showtime in showtimes
        ]
        return JSONResponse(
            content={
                "data": showtimes_list,
                "detail": "Showtimes obtained successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No showtimes found")


@router.get("/get_showtime_by_id/{showtime_id}")
def get_showtime_by_id(showtime_id: int):
    """This method is responsible for obtaining a showtime by its id."""
    showtime = services.get_showtime_by_id(showtime_id)
    if showtime:
        showtime_dict = {
            "showtime_id": showtime[0],
            "movie_id": showtime[1],
            "datetime": showtime[2].strftime("%Y-%m-%d %H:%M:%S"),
            "available_seats": showtime[3],
        }
        return JSONResponse(
            content={"data": showtime_dict, "detail": "Showtime obtained successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No showtime found")


@router.get("/get_seat_availability/{showtime_id}")
def get_seat_availability(showtime_id: int):
    """This method is responsible for obtaining the seat availability of a showtime."""
    seats = services.get_seat_availability(showtime_id)
    if seats:
        return JSONResponse(
            content={
                "data": seats,
                "detail": "Seat availability obtained successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No seat availability found")
