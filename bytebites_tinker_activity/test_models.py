"""
Temporary test script to verify ByteBites models implementation
"""
from models import Food, Customer, Menu, Order

print("=" * 60)
print("TESTING BYTEBITES MODELS")
print("=" * 60)

# Test Food class
print("\n1. Creating Food items...")
burger = Food("Spicy Burger", 12.99, "Entrees", 4.5)
soda = Food("Large Soda", 2.99, "Drinks", 4.0)
fries = Food("French Fries", 4.99, "Sides")  # Default rating
dessert = Food("Ice Cream", 5.99, "Desserts", 4.8)

print(f"✓ {burger.get_name()}: ${burger.get_price()} - {burger.get_category()} (Rating: {burger.get_popularity_rating()})")
print(f"✓ {soda.get_name()}: ${soda.get_price()} - {soda.get_category()} (Rating: {soda.get_popularity_rating()})")
print(f"✓ {fries.get_name()}: ${fries.get_price()} - {fries.get_category()} (Rating: {fries.get_popularity_rating()})")
print(f"✓ {dessert.get_name()}: ${dessert.get_price()} - {dessert.get_category()} (Rating: {dessert.get_popularity_rating()})")

# Test Customer class
print("\n2. Creating Customer...")
customer = Customer("Alice Smith")
print(f"✓ Customer: {customer.get_name()}")
print(f"✓ Is real user? {customer.verify_real_user()} (no orders yet)")
print(f"✓ Total orders: {customer.get_total_orders()}")

# Test Menu class
print("\n3. Creating Menu and adding items...")
menu = Menu()
menu.add_item(burger)
menu.add_item(soda)
menu.add_item(fries)
menu.add_item(dessert)
print(f"✓ Menu has {menu.get_item_count()} items")

print("\n4. Filtering menu by category...")
drinks = menu.filter_by_category("Drinks")
print(f"✓ Drinks category has {len(drinks)} item(s):")
for item in drinks:
    print(f"  - {item.get_name()}: ${item.get_price()}")

desserts = menu.filter_by_category("desserts")  # Test case-insensitive
print(f"✓ Desserts category has {len(desserts)} item(s):")
for item in desserts:
    print(f"  - {item.get_name()}: ${item.get_price()}")

print("\n5. Finding item by name...")
found = menu.find_item_by_name("spicy burger")  # Test case-insensitive
if found:
    print(f"✓ Found: {found.get_name()} - ${found.get_price()}")

# Test Order class
print("\n6. Creating Order...")
order = Order("ORD-001", customer)
print(f"✓ Order ID: {order.get_order_id()}")
print(f"✓ Customer: {order.get_customer().get_name()}")
print(f"✓ Order date: {order.get_order_date()}")

print("\n7. Adding items to order...")
order.add_item(burger)
order.add_item(soda)
order.add_item(fries)
order.add_item(soda)  # Test duplicate - ordering 2 sodas
print(f"✓ Order has {len(order.get_items())} items")

print("\n8. Computing order total...")
total = order.compute_total()
print(f"✓ Total cost: ${total:.2f}")

print("\n9. Order details:")
for i, item in enumerate(order.get_items(), 1):
    print(f"  {i}. {item.get_name()} - ${item.get_price()}")

# Test Customer purchase history
print("\n10. Adding order to customer history...")
customer.add_purchase(order)
print(f"✓ Customer now has {customer.get_total_orders()} order(s)")
print(f"✓ Is real user? {customer.verify_real_user()}")

# Create second order
print("\n11. Creating second order...")
order2 = Order("ORD-002", customer)
order2.add_item(dessert)
order2.add_item(soda)
customer.add_purchase(order2)
print(f"✓ Customer now has {customer.get_total_orders()} order(s)")
print(f"✓ Second order total: ${order2.compute_total():.2f}")

# Test order history
print("\n12. Customer purchase history:")
for i, past_order in enumerate(customer.get_purchase_history(), 1):
    print(f"  Order {i} ({past_order.get_order_id()}): ${past_order.compute_total():.2f}")

print("\n" + "=" * 60)
print("ALL TESTS COMPLETED SUCCESSFULLY!")
print("=" * 60)
