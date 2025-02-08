"""
This class is responsible for managing the cart's web services.
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
from backend_python.services.cart import (
    Cart,
    CartInvoker,
    AddToCartCommand,
    RemoveFromCartCommand,
    ClearCartCommand,
    GetItemsByCustomerIdCommand,
)

router = APIRouter()
cart = Cart()
invoker = CartInvoker()


@router.post("/add_to_cart")
async def add_to_cart(request: Request):
    """Add a ticket to the cart."""
    try:
        data = await request.json()
        customer_id = data.get("customer_id")
        ticket_id = data.get("ticket_id")
        command = AddToCartCommand(cart, customer_id, ticket_id)
        result = invoker.execute_command(command)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/remove_from_cart")
async def remove_from_cart(request: Request):
    """Remove a ticket from the cart."""
    try:
        data = await request.json()
        customer_id = data.get("customer_id")
        ticket_id = data.get("ticket_id")
        command = RemoveFromCartCommand(cart, customer_id, ticket_id)
        result = invoker.execute_command(command)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.post("/clear_cart")
async def clear_cart(request: Request):
    """Clear the cart."""
    try:
        data = await request.json()
        customer_id = data.get("customer_id")
        command = ClearCartCommand(cart, customer_id)
        result = invoker.execute_command(command)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get("/get_items_by_customer_id/{customer_id}")
async def get_items_by_customer_id(customer_id: int):
    """Get all items in the cart for a specific customer."""
    try:
        command = GetItemsByCustomerIdCommand(cart, customer_id)
        result = invoker.execute_command(command)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
