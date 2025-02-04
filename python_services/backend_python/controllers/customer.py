"""
This class is responsible for managing the customer's web services.
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

from datetime import datetime
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from backend_python.repositories.customer_repository import CustomerRepository
from backend_python.repositories.membership_repository import MembershipRepository

router = APIRouter()


@router.post("/create_customer")
async def create_customer(request: Request):
    """This method is responsible for creating a customer."""
    data = await request.json()
    email = data.get("email")

    if not email:
        raise HTTPException(status_code=400, detail="Invalid data")

    customer_created = CustomerRepository().create_customer(email)

    if customer_created:
        return JSONResponse(
            content={
                "data": customer_created,
                "detail": "Customer created successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Customer creation failed")


@router.get("/get_all_customers")
def get_all_customers():
    """This method is responsible for obtaining all customers."""
    customers = CustomerRepository().get_all_customers()
    if customers:
        return JSONResponse(
            content={"data": customers, "detail": "Customers obtained successfully"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"data": None, "detail": "Customers not found"}, status_code=404
        )


@router.get("/get_customer_by_id/{customer_id}")
def get_customer_by_id(customer_id: int):
    """This method is responsible for obtaining a customer by its id."""
    customer = CustomerRepository().get_customer_by_id(customer_id)
    if customer:
        return JSONResponse(
            content={"data": customer, "detail": "Customer obtained successfully"},
            status_code=200,
        )
    else:
        return JSONResponse(
            content={"data": None, "detail": "Customer not found"}, status_code=404
        )


@router.post("/customer/acquire_membership")
async def acquire_membership(request: Request):
    """This method is responsible for acquiring a membership."""
    data = await request.json()
    customer_id = data.get("customer_id")

    if not customer_id:
        raise HTTPException(status_code=400, detail="customer_id is required")

    expiration_date = datetime.now().replace(year=datetime.now().year + 1)

    membership_acquired = MembershipRepository().create_membership(
        customer_id, expiration_date, True
    )

    if membership_acquired:
        return JSONResponse(
            content={
                "detail": "Membership acquired successfully",
            },
            status_code=201,
        )
    else:
        raise HTTPException(status_code=400, detail="Membership acquisition failed")
