"""
This module contains the implementation of the Admin class into the database.
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


class AdminRepository:
    """This class handles the use of the admin table in the database."""

    def get_admin_by_id(self, admin_id):
        """Get an admin by its id."""
        query = "SELECT * FROM admins WHERE admin_id = %s"
        return db.execute_query(query, (admin_id,), fetch_one=True)

    def create_admin(self, email):
        """Create a new admin."""
        query = "INSERT INTO admins (email) VALUES (%s) RETURNING *"
        return db.execute_query(query, (email,), fetch_one=True)

    def get_all_admins(self):
        """Get all admins."""
        query = "SELECT * FROM admins"
        return db.execute_query(query, fetch_all=True)
