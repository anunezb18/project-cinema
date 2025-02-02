"""
This class is responsible for managing the membership logic.
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

from datetime import datetime, timedelta
from pydantic import BaseModel
from backend_python.repositories.membership_repository import MembershipRepository


class Membership(BaseModel):
    """This class is responsible for managing the membership's logic."""

    membership_id: int
    expiration_date: str
    status: bool

    def renew_membership(self, membership_id: int):
        """This method is responsible for renewing a membership."""

        membership = self.membership_repository.get_membership_by_customer_id(
            membership_id
        )
        if not membership:
            return {"error": "Membership not found"}

        new_expiration_date = datetime.strptime(
            membership["expiration_date"], "%Y-%m-%d"
        ) + timedelta(days=365)

        updated_membership = MembershipRepository().update_membership(
            membership_id, new_expiration_date, status=True
        )

        return {
            "message": "Membership renewed successfully",
            "membership": updated_membership,
        }

    def deactivate_membership(self, membership_id: int):
        """This method is responsible for deactivating a membership."""

        membership = self.membership_repository.get_membership_by_customer_id(
            membership_id
        )
        if not membership:
            return {"error": "Membership not found"}

        updated_membership = MembershipRepository().update_membership(
            membership_id, membership["expiration_date"], status=False
        )

        return {
            "message": "Membership deactivated successfully",
            "membership": updated_membership,
        }

    def activate_membership(self, membership_id: int):
        """This method is responsible for activating a membership."""

        membership = self.membership_repository.get_membership_by_customer_id(
            membership_id
        )
        if not membership:
            return {"error": "Membership not found"}

        updated_membership = MembershipRepository().update_membership(
            membership_id, membership["expiration_date"], status=True
        )

        return {
            "message": "Membership activated successfully",
            "membership": updated_membership,
        }
