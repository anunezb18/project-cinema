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
from backend_python.services.customer import Customer

router = APIRouter()
services = Customer()


@router.get("/customer/{customer_id}")
async def get_customer_by_id(customer_id: int):
    """This method is responsible for getting a customer by its id."""
    customer = services.get_customer_by_id(customer_id)
    if customer:
        return JSONResponse(status_code=200, content=customer.model_dump())
    raise HTTPException(status_code=404, detail="Customer not found.")


@router.get("/get_all_customers")
async def get_all_customers():
    """This method is responsible for getting all customers."""
    customers = services.get_all_customers()
    if customers:
        return JSONResponse(
            status_code=200, content=[customer.model_dump() for customer in customers]
        )
    raise HTTPException(status_code=404, detail="Customers not found.")


@router.post("/acquire_membership")
async def acquire_membership(request: Request):
    """This method is responsible for acquiring a membership."""
    data = await request.json()
    customer_id = data.get("customer_id")

    expiration_date = datetime.now().replace(year=datetime.now().year + 1)
    services.update_role(customer_id, "member")

    return services.acquire_membership(customer_id, expiration_date, True)
