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

db = DBConnection()
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

    def get_tickets_by_customer_id(self, customer_id):
        """Get all tickets for a customer by customer_id."""
        query = "SELECT * FROM tickets WHERE customer_id = %s"
        return db.execute_query(query, (customer_id,), fetch_all=True)

    def get_tickets_details_by_id(self, ticket_id):
        """Get the tickets details by its id"""
        query = """
        SELECT 
            tickets.ticket_id,
            tickets.customer_id,
            tickets.movie_id,
            tickets.showtime_id,
            tickets.seat_number,
            movies.title AS movie_title,
            movies.description AS movie_description,
            movies.genre AS movie_genre,
            movies.release_date AS movie_release_date,
            movies.length AS movie_length,
            showtimes.datetime AS showtime_datetime,
            showtimes.available_seats AS showtime_available_seats
        FROM tickets
        JOIN movies ON tickets.movie_id = movies.movie_id
        JOIN showtimes ON tickets.showtime_id = showtimes.showtime_id
        WHERE tickets.ticket_id = %s
        """
        return db.execute_query(query, (ticket_id,), fetch_one=True)
