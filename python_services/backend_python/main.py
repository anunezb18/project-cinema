"""
This class is responsible for handling the web services created with Fastapi.
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
from fastapi import FastAPI
from backend_python.controllers.user import router as user_router

app = FastAPI(
    title="CineMacondo",
    description="This is a backend service for the CineMacondo project, a systen cinema managment.",
    version="0.0.1",
)

app.include_router(user_router)
