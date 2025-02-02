from abc import ABC, abstractmethod
from datetime import datetime

class PricingStrategy(ABC):
    """This class is responsible for managing the ticket pricing and implements a strategy pattern."""

    @abstractmethod
    def get_price(self, base_price: float, date: datetime = None, is_member: bool = False) -> float:
        """This method is responsible for getting the price of a ticket."""
        pass

class RegularPricing(PricingStrategy):
    """This class represents the regular pricing strategy."""

    def get_price(self, base_price: float, date: datetime = None, is_member: bool = False) -> float:
        """This method is responsible for getting the regular price of a ticket."""
        return base_price
    
class DayPricing(PricingStrategy):
    """This class represents the day-based pricing strategy."""

    def get_price(self, base_price: float, date: datetime = None, is_member: bool = False) -> float:
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

    def get_price(self, base_price: float, date: datetime = None, is_member: bool = False) -> float:
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

    def get_price(self, base_price: float, date: datetime = None, is_member: bool = False) -> float:
        """This method is responsible for getting the member-based price of a ticket."""
        if is_member:
            return base_price * 0.9
        else:
            return base_price