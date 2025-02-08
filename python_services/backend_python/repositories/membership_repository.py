"""
This class handle the use of the membership table in the database.
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

from pydantic import BaseModel
from .db_connection import DBConnection

db = DBConnection()


class MembershipDAO(BaseModel):
    """Membership data access object."""

    membership_id: int
    customer_id: int
    expiration_date: str
    status: bool


class MembershipRepository:
    """This class handles the use of the membership table in the database."""

    def get_all_memberships(self) -> MembershipDAO:
        """Get all memberships."""
        query = "SELECT * FROM membership"
        return db.execute_query(query, fetch_all=True)

    def get_membership_by_customer_id(self, customer_id) -> MembershipDAO:
        """Get a membership by its customer_id."""
        query = "SELECT * FROM membership WHERE customer_id = %s"
        return db.execute_query(query, (customer_id,), fetch_one=True)

    def create_membership(self, customer_id, expiration_date, status):
        """Create a new membership."""
        query = "INSERT INTO membership (customer_id, expiration_date, status) VALUES (%s, %s, %s) RETURNING *"
        result = db.execute_query(
            query, (customer_id, expiration_date, status), fetch_one=True
        )
        return result

    def update_membership(self, membership_id, expiration_date, status):
        """Update a membership."""
        query = "UPDATE membership SET expiration_date = %s, status = %s WHERE membership_id = %s RETURNING *"
        result = db.execute_query(
            query, (expiration_date, status, membership_id), fetch_one=True
        )
        return result
