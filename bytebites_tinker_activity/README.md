# Summary

Understanding the differences between chat, ask, plan, and agent modes is essential for students working on this project, along with knowing when and how to create custom agents. Students may encounter challenges during agent setup, particularly in older VS Code versions where agent selection requires verbal invocation rather than UI options. AI assistance proved most effective when given a clear starting point or initial direction, it excels at expanding and refining ideas rather than generating them from scratch. Initially, I leveraged AI for brainstorming different approaches to the project structure before providing more specific instructions. When guiding students through this assignment, I recommend helping them envision the final product first, as this visualization exercise clarifies which methods are essential for each class and which are unnecessary. This approach encourages critical thinking about object-oriented design without directly providing solutions. By focusing on the end goal, students can better reason about the relationships between their chosen classes.

# ByteBites Backend

A Python-based backend system for the ByteBites food ordering app. This project implements core business logic for managing customers, food items, menus, and orders.

## Overview

ByteBites is a food ordering system that tracks customers, manages a menu of food items, and processes orders. The backend provides classes to:
- Track customer information and purchase history
- Manage food items with pricing, categories, and ratings
- Organize menu items with category filtering
- Group selected items into orders with total cost calculation

## Project Structure

```
bytebites_tinker_activity/
├── models.py              # Core classes (Customer, Food, Menu, Order)
├── scenario_demo.py       # Demo script showcasing functionality
├── test_bytebites.py      # Integration tests
├── test_models.py         # Unit tests for models
├── verify_methods.py      # Method verification utilities
├── bytebites_spec.md      # Feature specifications
├── bytebites_design.md    # UML class diagrams
└── draft_from_copilot.md  # Development notes
```

## Core Classes

### Customer
Tracks user information and purchase history for verification.
- **Attributes**: name, purchase history
- **Key Methods**: `getName()`, `getPurchaseHistory()`, `addPurchase()`, `verifyRealUser()`, `getTotalOrders()`

### Food
Represents individual food items with details.
- **Attributes**: name, price, category, popularity rating (0.0-5.0)
- **Key Methods**: `getName()`, `getPrice()`, `getCategory()`, `getPopularityRating()`, `setPrice()`, `updateRating()`

### Menu
Manages the collection of all available food items.
- **Key Methods**: Add items, filter by category, find items

### Order
Represents a transaction grouping selected items.
- **Key Methods**: Add items, calculate total cost, get order details

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Running the Demo
```bash
python scenario_demo.py
```

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test files
python -m pytest test_models.py
python -m pytest test_bytebites.py
```

## Usage Example

```python
from models import Customer, Food, Menu, Order

# Create a customer
customer = Customer("John Doe")

# Create food items
burger = Food("Spicy Burger", 12.99, "Entrees", 4.5)
soda = Food("Large Soda", 2.99, "Drinks", 4.2)

# Create a menu and add items
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)

# Create an order
order = Order()
order.add_item(burger)
order.add_item(soda)

# Process the order
customer.addPurchase(order)
total = order.calculate_total()  # 15.98
```

## Development

The project follows object-oriented design principles with proper encapsulation, validation, and error handling. See [bytebites_design.md](bytebites_design.md) for UML diagrams and [bytebites_spec.md](bytebites_spec.md) for detailed feature requirements.

## License

This project is part of CodePath coursework.
