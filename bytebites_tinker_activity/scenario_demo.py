"""
ByteBites Scenario Demo
Exercises filtering, searching, and total computation methods
"""
from models import Food, Customer, Menu, Order

print("=" * 70)
print("BYTEBITES SCENARIO: RESTAURANT ORDERING SYSTEM")
print("=" * 70)

# ==================== CREATE MENU ====================
print("\n📋 STEP 1: Building the Menu")
print("-" * 70)

menu = Menu()

# Add various food items
menu.add_item(Food("Classic Burger", 10.99, "Entrees", 4.5))
menu.add_item(Food("Spicy Burger", 12.99, "Entrees", 4.8))
menu.add_item(Food("Veggie Burger", 11.99, "Entrees", 4.2))
menu.add_item(Food("Coca Cola", 2.49, "Drinks", 4.0))
menu.add_item(Food("Lemonade", 2.99, "Drinks", 3.8))
menu.add_item(Food("Iced Tea", 2.49, "Drinks", 4.1))
menu.add_item(Food("French Fries", 4.99, "Sides", 4.6))
menu.add_item(Food("Onion Rings", 5.49, "Sides", 4.3))
menu.add_item(Food("Ice Cream Sundae", 5.99, "Desserts", 4.7))
menu.add_item(Food("Chocolate Cake", 6.99, "Desserts", 4.9))

print(f"✓ Menu created with {menu.get_item_count()} items")

# ==================== FILTER BY CATEGORY ====================
print("\n🔍 STEP 2: Filtering Menu by Category")
print("-" * 70)

print("\nAvailable Entrees:")
entrees = menu.filter_by_category("Entrees")
for item in entrees:
    print(f"  • {item.get_name()}: ${item.get_price():.2f} (⭐ {item.get_popularity_rating()})")

print("\nAvailable Drinks:")
drinks = menu.filter_by_category("drinks")  # Test case-insensitive
for item in drinks:
    print(f"  • {item.get_name()}: ${item.get_price():.2f} (⭐ {item.get_popularity_rating()})")

print("\nAvailable Desserts:")
desserts = menu.filter_by_category("DESSERTS")  # Test case-insensitive
for item in desserts:
    print(f"  • {item.get_name()}: ${item.get_price():.2f} (⭐ {item.get_popularity_rating()})")

# ==================== SEARCH FOR ITEMS ====================
print("\n🔎 STEP 3: Searching for Specific Items")
print("-" * 70)

search_terms = ["spicy burger", "Lemonade", "chocolate cake"]
for term in search_terms:
    found = menu.find_item_by_name(term)
    if found:
        print(f"✓ Found '{term}': {found.get_name()} - ${found.get_price():.2f}")

# ==================== CREATE CUSTOMER ====================
print("\n👤 STEP 4: Creating Customer")
print("-" * 70)

customer = Customer("John Smith")
print(f"✓ Customer created: {customer.get_name()}")
print(f"  Is verified user? {customer.verify_real_user()} (no orders yet)")

# ==================== PLACE FIRST ORDER ====================
print("\n🛒 STEP 5: Placing First Order")
print("-" * 70)

order1 = Order("ORD-2024-001", customer)
print(f"✓ Order created: {order1.get_order_id()}")

# Customer orders a burger combo
burger = menu.find_item_by_name("Spicy Burger")
fries = menu.find_item_by_name("French Fries")
drink = menu.find_item_by_name("Coca Cola")

order1.add_item(burger)
order1.add_item(fries)
order1.add_item(drink)

print(f"\nOrder Items:")
for i, item in enumerate(order1.get_items(), 1):
    print(f"  {i}. {item.get_name()} - ${item.get_price():.2f}")

# Compute total
total1 = order1.compute_total()
print(f"\n💰 Order Total: ${total1:.2f}")

# Add to customer history
customer.add_purchase(order1)
print(f"✓ Order added to {customer.get_name()}'s purchase history")
print(f"  Is verified user now? {customer.verify_real_user()}")

# ==================== PLACE SECOND ORDER ====================
print("\n🛒 STEP 6: Placing Second Order (Dessert Run)")
print("-" * 70)

order2 = Order("ORD-2024-002", customer)
print(f"✓ Order created: {order2.get_order_id()}")

# Customer orders desserts
cake = menu.find_item_by_name("chocolate cake")
sundae = menu.find_item_by_name("ice cream sundae")
tea = menu.find_item_by_name("iced tea")

order2.add_item(cake)
order2.add_item(sundae)
order2.add_item(tea)

print(f"\nOrder Items:")
for i, item in enumerate(order2.get_items(), 1):
    print(f"  {i}. {item.get_name()} - ${item.get_price():.2f}")

total2 = order2.compute_total()
print(f"\n💰 Order Total: ${total2:.2f}")

customer.add_purchase(order2)

# ==================== PLACE THIRD ORDER (PARTY) ====================
print("\n🛒 STEP 7: Placing Third Order (Party - Multiple Items)")
print("-" * 70)

order3 = Order("ORD-2024-003", customer)
print(f"✓ Order created: {order3.get_order_id()}")

# Customer orders multiple items (duplicates allowed)
classic = menu.find_item_by_name("Classic Burger")
veggie = menu.find_item_by_name("Veggie Burger")
lemonade = menu.find_item_by_name("Lemonade")
onion_rings = menu.find_item_by_name("Onion Rings")

# Add multiple burgers and drinks
order3.add_item(classic)
order3.add_item(classic)  # 2 classic burgers
order3.add_item(veggie)
order3.add_item(fries)
order3.add_item(onion_rings)
order3.add_item(lemonade)
order3.add_item(lemonade)  # 2 lemonades
order3.add_item(drink)    # 1 coca cola

print(f"\nOrder Items ({len(order3.get_items())} items):")
for i, item in enumerate(order3.get_items(), 1):
    print(f"  {i}. {item.get_name()} - ${item.get_price():.2f}")

total3 = order3.compute_total()
print(f"\n💰 Order Total: ${total3:.2f}")

customer.add_purchase(order3)

# ==================== CUSTOMER SUMMARY ====================
print("\n📊 STEP 8: Customer Summary")
print("-" * 70)

print(f"\n👤 Customer: {customer.get_name()}")
print(f"   Verified User: {customer.verify_real_user()}")
print(f"   Total Orders: {customer.get_total_orders()}")

print(f"\n📝 Purchase History:")
purchase_history = customer.get_purchase_history()
grand_total = 0
for i, order in enumerate(purchase_history, 1):
    order_total = order.compute_total()
    grand_total += order_total
    print(f"   {i}. {order.get_order_id()} - ${order_total:.2f} ({len(order.get_items())} items)")

print(f"\n💵 Grand Total Across All Orders: ${grand_total:.2f}")

# ==================== CATEGORY ANALYSIS ====================
print("\n📈 STEP 9: Menu Category Analysis")
print("-" * 70)

categories = ["Entrees", "Drinks", "Sides", "Desserts"]
for category in categories:
    items = menu.filter_by_category(category)
    if items:
        avg_price = sum(item.get_price() for item in items) / len(items)
        avg_rating = sum(item.get_popularity_rating() for item in items) / len(items)
        print(f"\n{category}:")
        print(f"  Items: {len(items)}")
        print(f"  Avg Price: ${avg_price:.2f}")
        print(f"  Avg Rating: {avg_rating:.1f} ⭐")

print("\n" + "=" * 70)
print("SCENARIO COMPLETE! All methods tested successfully.")
print("=" * 70)
