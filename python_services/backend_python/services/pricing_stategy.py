"""
This module contains the implementation of a pricing strategy for the ticket's price.
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

from abc import ABC, abstractmethod
from datetime import datetime


class PricingStrategy(ABC):
    """This class is responsible for managing the ticket pricing and implements a strategy pattern."""

    @abstractmethod
    def get_price(
        self, base_price: float, date: datetime = None, is_member: bool = False
    ):
        """This method is responsible for getting the price of a ticket."""


class RegularPricing(PricingStrategy):
    """This class represents the regular pricing strategy."""

    def get_price(
        self, base_price: float, date: datetime = None, is_member: bool = False
    ):
        """This method is responsible for getting the regular price of a ticket."""
        return base_price


class DayPricing(PricingStrategy):
    """This class represents the day-based pricing strategy."""

    def get_price(
        self, base_price: float, date: datetime = None, is_member: bool = False
    ) -> float:
        """This method is responsible for getting the day-based price of a ticket."""
        if date is None:
            return base_price

        weekday = date.weekday()
        if weekday in [1, 2]:
            return base_price * 0.8
        elif weekday == 6:
            return base_price * 1.2
        else:
            return base_price


class HourPricing(PricingStrategy):
    """This class represents the hour-based pricing strategy."""

    def get_price(
        self, base_price: float, date: datetime = None, is_member: bool = False
    ) -> float:
        """This method is responsible for getting the hour-based price of a ticket."""
        if date is None:
            return base_price

        hour = date.hour
        if hour >= 15:
            return base_price * 1.1
        else:
            return base_price


class MemberPricing(PricingStrategy):
    """This class represents the member-based pricing strategy."""

    def get_price(
        self, base_price: float, date: datetime = None, is_member: bool = False
    ) -> float:
        """This method is responsible for getting the member-based price of a ticket."""
        if is_member:
            return base_price * 0.5
        else:
            return base_price
