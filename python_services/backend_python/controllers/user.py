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
from backend_python.services.user import User

router = APIRouter()

services = User()


@router.post("/signup")
async def sign_up(request: Request):
    """This method is responsible for registering a user."""
    data = await request.json()
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")
    role = data.get("role")

    return services.signup(name, email, password, role)


@router.put("/update")
async def update_user(request: Request):
    """This method is responsible for updating a user."""
    data = await request.json()
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")

    return services.update(name, email, password)

@router.delete("/delete")
async def delete_user(request: Request):
    """This method is responsible for deleting a user."""
    data = await request.json()
    email = data.get("email")

    return services.delete_user(email)

@router.get("/get_all_users")
async def get_all_users():
    """This method is responsible for getting all users."""
    users = services.get_all__users()

    if users:
        return JSONResponse(
            content={
                "data": [user.model_dump() for user in users],
                "detail": "Users retrieved successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=400, detail="Users retrieval failed")


@router.get("/get_user_by_email")
async def get_user_by_email(request: Request):
    """This method is responsible for getting a user by its email."""
    data = await request.json()
    email = data.get("email")

    user = services.get_user_by_email(email)

    if user:
        return JSONResponse(
            content={
                "data": user.model_dump(),
                "detail": "User retrieved successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=400, detail="User retrieval failed")


@router.post("/login")
async def login(request: Request):
    """This method is responsible for logging in a user."""
    data = await request.json()
    email = data.get("email")
    password = data.get("password")

    return services.login(email, password)
