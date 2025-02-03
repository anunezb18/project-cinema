"""
This class handle the use of the cart table in the database.
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

import logging
import os
import psycopg2


class DBConnection:
    """This class handles the connection to the database."""

    def __init__(self):
        """Initialize the database connection."""
        self.name = os.getenv("DATABASE_NAME", "cinemacondo")
        self.user = os.getenv("DATABASE_USER", "postgres")
        self.password = os.getenv("DATABASE_PASSWORD", "181018")
        self.host = os.getenv("DATABASE_HOST", "localhost")
        self.port = int(os.getenv("DATABASE_PORT", "5432"))
        self.conn = None

    def connect(self):
        """Establish the connection to the database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    dbname=self.name,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port,
                )
                logging.info("Database connection established.")
            except psycopg2.DatabaseError as e:
                logging.error("Database connection failed: %s", e)
                raise

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        """Execute a query to the database."""
        self.connect()
        try:
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
        except psycopg2.DatabaseError as e:
            logging.error("Query execution failed: %s", e)
            self.conn.rollback()
            raise

    def close(self):
        """Close the connection to the database."""
        if self.conn:
            self.conn.close()
            self.conn = None
            logging.info("Database connection closed.")
