"""
This module contains the implementation of the web services of membership class.
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
from backend_python.services.membership import Membership

router = APIRouter()

services = Membership()


@router.get("/get_all_memberships")
def get_all_memberships():
    """This method is responsible for obtaining all memberships."""
    memberships = services.get_all_memberships()
    if memberships:
        memberships_list = [
            {
                "membership_id": membership[0],
                "customer_id": membership[1],
                "expiration_date": membership[2].strftime("%Y-%m-%d"),
                "status": membership[3],
            }
            for membership in memberships
        ]
        return JSONResponse(
            content={
                "data": memberships_list,
                "detail": "Memberships obtained successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="No memberships found")


@router.get("/get_membership_by_id/{membership_id}")
def get_membership_by_id(membership_id: int):
    """This method is responsible for obtaining a membership by its id."""
    membership = services.get_membership_by_id(membership_id)
    if membership:
        membership_dict = {
            "membership_id": membership[0],
            "customer_id": membership[1],
            "expiration_date": membership[2].strftime("%Y-%m-%d"),
            "status": membership[3],
        }
        return JSONResponse(
            content={
                "data": membership_dict,
                "detail": "Membership obtained successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="Membership not found")


@router.get("/get_membership_by_customer_id/{customer_id}")
def get_membership_by_customer_id(customer_id: int):
    """This method is responsible for obtaining a membership by customer id."""
    membership = services.get_membership_by_customer_id(customer_id)
    if membership:
        membership_dict = {
            "membership_id": membership[0],
            "customer_id": membership[1],
            "expiration_date": membership[2].strftime("%Y-%m-%d"),
            "status": membership[3],
        }
        return JSONResponse(
            content={
                "data": membership_dict,
                "detail": "Membership obtained successfully",
            },
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="Membership not found")


@router.post("/renew_membership")
async def renew_membership(request: Request):
    """This method is responsible for renewing a membership."""
    data = await request.json()
    membership_id = data.get("membership_id")
    return services.renew_membership(membership_id)


@router.post("/deactivate_membership")
async def deactivate_membership(request: Request):
    """This method is responsible for deactivating a membership."""
    data = await request.json()
    membership_id = data.get("membership_id")
    return services.deactivate_membership(membership_id)
