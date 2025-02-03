"""
This class is responsible for managing the user's web services.
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
from backend_python.repositories.user_repository import UserRepository

router = APIRouter()


@router.post("/signup")
async def sign_up(request: Request):
    """This method is responsible for registering a user."""
    data = await request.json()
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")

    if not email or not name or not password:
        raise HTTPException(status_code=400, detail="Invalid data")

    user_created = UserRepository().create_user(email, name, password)

    if user_created:
        return JSONResponse(
            content={"data": user_created, "detail": "User created successfully"},
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="User creation failed")


@router.post("/login")
async def log_in(request: Request):
    """This method is responsible for logging in a user."""
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        raise HTTPException(status_code=400, detail="Invalid data")

    user = UserRepository().get_user_by_email_and_password(email, password)
    if user:
        return JSONResponse(
            content={"data": user, "detail": "User logged in successfully"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"data": None, "detail": "User not found"}, status_code=404
        )


@router.post("/logout")
def log_out():
    """This method is responsible for logging out a user."""
    return JSONResponse(
        content={"data": None, "detail": "User logged out successfully"},
        status_code=200,
    )


@router.put("/update")
async def update_info(request: Request):
    """This method is responsible for updating a user's information."""
    data = await request.json()
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")

    if not email or not name or not password:
        raise HTTPException(status_code=400, detail="Invalid data")

    user = UserRepository().update_user(email, name, password)
    if user:
        return JSONResponse(
            content={"data": user, "detail": "User updated successfully"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"data": None, "detail": "User update failed"}, status_code=400
        )


@router.get("/get_all_users")
def get_all_users():
    """This method is responsible for obtaining all users."""
    users = UserRepository().get_all_users()
    if users:
        return JSONResponse(
            content={"data": users, "detail": "Users obtained successfully"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"data": None, "detail": "Users not found"}, status_code=404
        )
