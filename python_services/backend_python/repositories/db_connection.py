"""
This class contains the connection to the database.

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

import psycopg2


class DBConnection:
    """This class handle the connection to the database."""

    def __init__(self, dbname, user, password, host, port=5432):
        """Initialize the database connection."""
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        """Stablish the connection to the database."""
        if self.conn is None:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        """Execute a query to the database."""
        self.connect()
        with self.conn.cursor() as cursor:
            cursor.execute(query, params or ())

            if fetch_one:
                result = cursor.fetchone()
            elif fetch_all:
                result = cursor.fetchall()
            else:
                result = None

            self.conn.commit()
            return result

    def close(self):
        """Close the connection to the database."""
        if self.conn:
            self.conn.close()
            self.conn = None
