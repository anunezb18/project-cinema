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

from datetime import datetime
from backend_python.repositories.cart_repository import CartRepository
from backend_python.repositories.customer_repository import CustomerRepository
from backend_python.repositories.user_repository import UserRepository
from backend_python.repositories.admin_repository import AdminRepository
from backend_python.repositories.membership_repository import MembershipRepository

class UserFactory:
    """This class is responsible for managing the user's logic."""

    @staticmethod
    def create_user(name: str, email: str, password: str, role: str):
        """This method is responsible for creating a user based on the role."""
        user_repository = UserRepository()

        if role == "admin":
            user_created = user_repository.create_user(email, name, password, role)
            if user_created:
                admin_repository = AdminRepository()
                admin_repository.create_admin(email)
        elif role == "regular":
            user_created = user_repository.create_user(email, name, password, role)
            if user_created:
                customer_repository = CustomerRepository()
                customer_created = customer_repository.create_customer(email, "regular")
                if customer_created:
                    cart_repository = CartRepository()
                    cart = cart_repository.create_cart(customer_created.customer_id)
                    if cart:
                        customer_repository.asign_cart(
                            customer_created.customer_id, cart["cart_id"]
                        )
                        customer_created.cart_id = cart["cart_id"]
        elif role == "member":
            user_created = user_repository.create_user(email, name, password, role)
            if user_created:
                customer_repository = CustomerRepository()
                customer_created = customer_repository.create_customer(email, "member")
                membership_customer = MembershipRepository()
                expiration_date = datetime.now().replace(year=datetime.now().year + 1)
                membership_customer.create_membership(customer_created.customer_id, expiration_date, True)
                if customer_created:
                    cart_repository = CartRepository()
                    cart = cart_repository.create_cart(customer_created.customer_id)
                    if cart:
                        customer_repository.asign_cart(
                            customer_created.customer_id, cart["cart_id"]
                        )
                        customer_created.cart_id = cart["cart_id"]
        else:
            raise ValueError(f"Unknown role: {role}")

        return user_created
