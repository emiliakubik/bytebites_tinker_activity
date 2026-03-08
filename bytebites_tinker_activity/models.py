"""
ByteBites Backend Models
------------------------
Customer: Tracks user info and purchase history for verification
Food: Individual items with name, price, category, and popularity rating
Menu: Collection of all food items with category filtering
Order: Transaction grouping items and computing total cost
"""

from datetime import datetime
from typing import List, Optional


class Food:
    """Represents a food item with name, price, category, and popularity rating."""
    
    def __init__(self, name: str, price: float, category: str, popularity_rating: float = 0.0):
        """Initialize a Food item with name, price, category, and optional rating.
        
        Args:
            name: Name of the food item (must not be empty)
            price: Price in dollars (must be non-negative)
            category: Category like "Drinks", "Desserts", etc. (must not be empty)
            popularity_rating: Rating from 0.0 to 5.0 (defaults to 0.0 for new items)
            
        Raises:
            ValueError: If any validation fails
        """
        if not name or not name.strip():
            raise ValueError("Food name cannot be empty")
        if not category or not category.strip():
            raise ValueError("Category cannot be empty")
        if price < 0:
            raise ValueError("Price must be non-negative")
        if not (0.0 <= popularity_rating <= 5.0):
            raise ValueError("Popularity rating must be between 0.0 and 5.0")
            
        self._name = name.strip()
        self._price = price
        self._category = category.strip()
        self._popularity_rating = popularity_rating
    
    def get_name(self) -> str:
        """Return the name of the food item."""
        return self._name
    
    def get_price(self) -> float:
        """Return the price of the food item."""
        return self._price
    
    def get_category(self) -> str:
        """Return the category of the food item."""
        return self._category
    
    def get_popularity_rating(self) -> float:
        """Return the popularity rating of the food item."""
        return self._popularity_rating
    
    def set_price(self, price: float) -> None:
        """Update the price of the food item.
        
        Args:
            price: New price (must be non-negative)
            
        Raises:
            ValueError: If price is negative
        """
        if price < 0:
            raise ValueError("Price must be non-negative")
        self._price = price
    
    def update_rating(self, rating: float) -> None:
        """Update the popularity rating of the food item.
        
        Args:
            rating: New rating from 0.0 to 5.0
            
        Raises:
            ValueError: If rating is outside valid range
        """
        if not (0.0 <= rating <= 5.0):
            raise ValueError("Popularity rating must be between 0.0 and 5.0")
        self._popularity_rating = rating


class Customer:
    """Represents a customer with name and purchase history."""
    
    def __init__(self, name: str):
        """Initialize a Customer with a name.
        
        Args:
            name: Customer's name (must not be empty)
            
        Raises:
            ValueError: If name validation fails
        """
        if not name or not name.strip():
            raise ValueError("Customer name cannot be empty")
            
        self._name = name.strip()
        self._purchase_history = []
    
    def get_name(self) -> str:
        """Return the customer's name."""
        return self._name
    
    def get_purchase_history(self) -> List['Order']:
        """Return the list of past orders."""
        return self._purchase_history.copy()
    
    def add_purchase(self, order: 'Order') -> None:
        """Add an order to the customer's purchase history.
        
        Args:
            order: Order to add to history
            
        Raises:
            ValueError: If order is None
        """
        if order is None:
            raise ValueError("Order cannot be None")
        self._purchase_history.append(order)
    
    def verify_real_user(self) -> bool:
        """Verify if the customer is a real user based on purchase history.
        
        Returns:
            True if customer has made at least one purchase, False otherwise
        """
        return len(self._purchase_history) > 0
    
    def get_total_orders(self) -> int:
        """Return the total number of orders placed."""
        return len(self._purchase_history)


class Menu:
    """Manages a collection of food items with filtering capabilities."""
    
    def __init__(self):
        """Initialize an empty Menu."""
        self._items = []
    
    def add_item(self, food: Food) -> None:
        """Add a food item to the menu.
        
        Args:
            food: Food item to add to the menu
            
        Raises:
            ValueError: If food is None or already exists in menu
        """
        if food is None:
            raise ValueError("Food item cannot be None")
        
        # Check for duplicates by name (case-insensitive)
        if any(item.get_name().lower() == food.get_name().lower() for item in self._items):
            raise ValueError(f"Food item '{food.get_name()}' already exists in menu")
        
        self._items.append(food)
    
    def remove_item(self, food: Food) -> None:
        """Remove a food item from the menu.
        
        Args:
            food: Food item to remove from the menu
            
        Raises:
            ValueError: If food is None or not found in menu
        """
        if food is None:
            raise ValueError("Food item cannot be None")
        
        if food not in self._items:
            raise ValueError(f"Food item '{food.get_name()}' not found in menu")
        
        self._items.remove(food)
    
    def get_all_items(self) -> List[Food]:
        """Return all food items in the menu.
        
        Returns:
            A copy of the items list to prevent external modification
        """
        return self._items.copy()
    
    def filter_by_category(self, category: str) -> List[Food]:
        """Return all food items matching the specified category.
        
        Args:
            category: Category to filter by (case-insensitive)
            
        Returns:
            List of Food items in the specified category
            
        Raises:
            ValueError: If category is None or empty
        """
        if not category or not category.strip():
            raise ValueError("Category cannot be empty")
        
        category_lower = category.strip().lower()
        return [item for item in self._items 
                if item.get_category().lower() == category_lower]
    
    def find_item_by_name(self, name: str) -> Optional[Food]:
        """Find and return a food item by name, or None if not found.
        
        Args:
            name: Name of the food item to search for (case-insensitive)
            
        Returns:
            Food item if found, None otherwise
            
        Raises:
            ValueError: If name is None or empty
        """
        if not name or not name.strip():
            raise ValueError("Name cannot be empty")
        
        name_lower = name.strip().lower()
        for item in self._items:
            if item.get_name().lower() == name_lower:
                return item
        return None
    
    def get_item_count(self) -> int:
        """Return the total number of items in the menu.
        
        Returns:
            Number of items in the menu
        """
        return len(self._items)


class Order:
    """Represents a transaction grouping food items and computing total cost."""
    
    def __init__(self, order_id: str, customer: Customer):
        """Initialize an Order with an order ID and customer.
        
        Args:
            order_id: Unique identifier for the order (must not be empty)
            customer: Customer who placed the order (must not be None)
            
        Raises:
            ValueError: If validation fails
        """
        if not order_id or not order_id.strip():
            raise ValueError("Order ID cannot be empty")
        if customer is None:
            raise ValueError("Customer cannot be None")
            
        self._order_id = order_id.strip()
        self._customer = customer
        self._items = []
        self._order_date = datetime.now()
    
    def add_item(self, food: Food) -> None:
        """Add a food item to the order.
        
        Allows duplicate items (e.g., ordering 2 burgers).
        
        Args:
            food: Food item to add to the order
            
        Raises:
            ValueError: If food is None
        """
        if food is None:
            raise ValueError("Food item cannot be None")
        self._items.append(food)
    
    def remove_item(self, food: Food) -> None:
        """Remove a food item from the order.
        
        Removes the first occurrence of the food item.
        
        Args:
            food: Food item to remove from the order
            
        Raises:
            ValueError: If food is None or not found in order
        """
        if food is None:
            raise ValueError("Food item cannot be None")
        
        if food not in self._items:
            raise ValueError(f"Food item '{food.get_name()}' not found in order")
        
        self._items.remove(food)
    
    def compute_total(self) -> float:
        """Calculate and return the total cost of all items in the order.
        
        Returns:
            Total cost of all items in the order
        """
        return sum(item.get_price() for item in self._items)
    
    def get_items(self) -> List[Food]:
        """Return the list of food items in the order.
        
        Returns:
            A copy of the items list to prevent external modification
        """
        return self._items.copy()
    
    def get_customer(self) -> Customer:
        """Return the customer who placed the order.
        
        Returns:
            Customer who placed this order
        """
        return self._customer
    
    def get_order_id(self) -> str:
        """Return the order ID.
        
        Returns:
            Unique order identifier
        """
        return self._order_id
    
    def get_order_date(self) -> datetime:
        """Return the date and time the order was placed.
        
        Returns:
            Datetime when order was created
        """
        return self._order_date

