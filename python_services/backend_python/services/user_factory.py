"""
This class is the factory for the user's logic.
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

from .admin_interface import AdminReal
from .customer import RegularCustomer, MemberCustomer


class UserFactory:
    """This class is responsible for managing the user's logic."""

    @staticmethod
    def create_user(
        name: str, email: str, password: str, role: str, membership_id: str = None
    ):
        """This method is responsible for creating a user based on the role."""
        if role == "admin":
            return AdminReal(name=name, email=email, password=password)
        elif role == "regular_customer":
            return RegularCustomer(name=name, email=email, password=password)
        elif role == "member_customer":
            if membership_id is None:
                raise ValueError("Membership ID is required for member customers.")
            return MemberCustomer(
                name=name, email=email, password=password, membership_id=membership_id
            )
        else:
            raise ValueError(f"Unknown role: {role}")
