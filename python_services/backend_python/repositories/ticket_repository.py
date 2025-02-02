"""
This class handle the use of the ticket table in the database.
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

from .db_connection import DBConnection

db = DBConnection(
    dbname="cinemacondo",
    user="postgres",
    password="Bullrock",
    host="localhost",
    port=5432,
)


class TicketRepository:
    """This class handles the use of the ticket table in the database."""

    def get_ticket_by_id(self, ticket_id):
        """Get a ticket by its id."""
        query = "SELECT * FROM tickets WHERE ticket_id = %s"
        return db.execute_query(query, (ticket_id,), fetch_one=True)

    def create_ticket(self, customer_id, showtime_id, seat_number, price, status):
        """Create a new ticket."""
        query = "INSERT INTO tickets (customer_id, showtime_id, seat_number, price, status) VALUES (%s, %s, %s, %s, %s) RETURNING *"
        return db.execute_query(
            query,
            (customer_id, showtime_id, seat_number, price, status),
            fetch_one=True,
        )

    def update_ticket(
        self, ticket_id, customer_id, showtime_id, seat_number, price, status
    ):
        """Update a ticket."""
        query = "UPDATE tickets SET customer_id = %s, showtime_id = %s, seat_number = %s, price = %s, status = %s WHERE ticket_id = %s RETURNING *"
        return db.execute_query(
            query,
            (customer_id, showtime_id, seat_number, price, status, ticket_id),
            fetch_one=True,
        )

    def delete_ticket(self, ticket_id):
        """Delete a ticket."""
        query = "DELETE FROM tickets WHERE ticket_id = %s"
        return db.execute_query(query, (ticket_id,))

    def get_all_tickets(self):
        """Get all tickets."""
        query = "SELECT * FROM tickets"
        return db.execute_query(query, fetch_all=True)
