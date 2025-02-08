"""
This class is responsible for managing the ticket's services web.
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
from backend_python.services.ticket import Ticket

router = APIRouter()

services = Ticket()


@router.post("/create_ticket")
async def create_ticket(request: Request):
    """This method is responsible for creating a ticket."""
    data = await request.json()
    showtime_id = data.get("showtime_id")
    customer_id = data.get("customer_id")
    seat = data.get("seat")

    try:
        ticket = services.create_ticket(customer_id, showtime_id, seat)

        if ticket:
            ticket_data = {
                "ticket_id": ticket[0],
                "customer_id": ticket[1],
                "showtime_id": ticket[2],
                "seat_number": ticket[3],
                "price": float(ticket[4]),
                "status": ticket[5],
            }
            return JSONResponse(
                content={"data": ticket_data, "detail": "Ticket created successfully"},
                status_code=201,
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to create ticket.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


@router.get("/get_all_tickets")
async def get_all_tickets():
    """This method is responsible for getting all tickets."""
    tickets = services.get_all_tickets()
    tickets_data = []
    for ticket in tickets:
        ticket_data = {
            "ticket_id": ticket[0],
            "customer_id": ticket[1],
            "showtime_id": ticket[2],
            "seat_number": ticket[3],
            "price": float(ticket[4]),
            "status": ticket[5],
        }
        tickets_data.append(ticket_data)
    return JSONResponse(
        content={"data": tickets_data, "detail": "Tickets retrieved successfully"},
        status_code=200,
    )


@router.get("/get_ticket_by_id/{ticket_id}")
async def get_ticket_by_id(ticket_id: int):
    """This method is responsible for getting a ticket by its id."""
    ticket = services.get_ticket_by_id(ticket_id)
    if ticket:
        ticket_data = {
            "ticket_id": ticket[0],
            "customer_id": ticket[1],
            "showtime_id": ticket[2],
            "seat_number": ticket[3],
            "price": float(ticket[4]),
            "status": ticket[5],
        }
        return JSONResponse(
            content={"data": ticket_data, "detail": "Ticket retrieved successfully"},
            status_code=200,
        )
    else:
        raise HTTPException(status_code=404, detail="Ticket not found.")


@router.get("/get_tickets_by_customer_id/{customer_id}")
async def get_tickets_by_customer_id(customer_id: int):
    """This method is responsible for getting all tickets for a customer by customer_id."""
    tickets = services.get_tickets_by_customer_id(customer_id)
    tickets_data = []
    for ticket in tickets:
        ticket_data = {
            "ticket_id": ticket[0],
            "customer_id": ticket[1],
            "showtime_id": ticket[2],
            "seat_number": ticket[3],
            "price": float(ticket[4]),
            "status": ticket[5],
        }
        tickets_data.append(ticket_data)
    return JSONResponse(
        content={"data": tickets_data, "detail": "Tickets retrieved successfully"},
        status_code=200,
    )


@router.post("/cancel_ticket")
async def cancel_ticket(request: Request):
    """This method is responsible for canceling a ticket."""
    data = await request.json()
    ticket_id = data.get("ticket_id")

    try:
        ticket = services.cancel_ticket(ticket_id)
        if ticket:
            ticket_data = {
                "ticket_id": ticket[0],
                "customer_id": ticket[1],
                "showtime_id": ticket[2],
                "seat_number": ticket[3],
                "price": float(ticket[4]),
                "status": ticket[5],
            }
            return JSONResponse(
                content={"data": ticket_data, "detail": "Ticket canceled successfully"},
                status_code=200,
            )
        else:
            raise HTTPException(status_code=500, detail="Failed to cancel ticket.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
