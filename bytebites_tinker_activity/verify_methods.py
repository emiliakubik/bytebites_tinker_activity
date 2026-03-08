"""
Method Verification Script
Tests each key method individually to verify behavior
"""
from models import Food, Customer, Menu, Order

print("=" * 70)
print("METHOD VERIFICATION TEST")
print("=" * 70)

# Setup test data
burger = Food("Burger", 10.99, "Entrees", 4.5)
pizza = Food("Pizza", 12.99, "Entrees", 4.8)
soda = Food("Soda", 2.49, "Drinks", 4.0)
cake = Food("Cake", 5.99, "Desserts", 4.7)

menu = Menu()
menu.add_item(burger)
menu.add_item(pizza)
menu.add_item(soda)
menu.add_item(cake)

customer = Customer("Test User")

# ============================================================
# TEST 1: Menu.filter_by_category()
# ============================================================
print("\n[TEST 1] Menu.filter_by_category()")
print("-" * 70)

entrees = menu.filter_by_category("Entrees")
drinks = menu.filter_by_category("drinks")  # Test case-insensitive

print(f"✓ Filtered 'Entrees': Found {len(entrees)} items")
assert len(entrees) == 2, "Should find 2 entrees"
assert all(item.get_category() == "Entrees" for item in entrees), "All should be Entrees"

print(f"✓ Filtered 'drinks' (case-insensitive): Found {len(drinks)} items")
assert len(drinks) == 1, "Should find 1 drink"
assert drinks[0].get_name() == "Soda", "Should be Soda"

print("✅ PASS: filter_by_category() works correctly")

# ============================================================
# TEST 2: Menu.find_item_by_name()
# ============================================================
print("\n[TEST 2] Menu.find_item_by_name()")
print("-" * 70)

found_burger = menu.find_item_by_name("burger")  # Case-insensitive
found_pizza = menu.find_item_by_name("PIZZA")    # Case-insensitive
found_none = menu.find_item_by_name("Tacos")     # Not in menu

print(f"✓ Search 'burger': Found '{found_burger.get_name()}' at ${found_burger.get_price()}")
assert found_burger is not None, "Should find burger"
assert found_burger.get_name() == "Burger", "Should be Burger"

print(f"✓ Search 'PIZZA': Found '{found_pizza.get_name()}' at ${found_pizza.get_price()}")
assert found_pizza is not None, "Should find pizza"

print(f"✓ Search 'Tacos': Found {found_none}")
assert found_none is None, "Should return None for non-existent item"

print("✅ PASS: find_item_by_name() works correctly")

# ============================================================
# TEST 3: Order.compute_total()
# ============================================================
print("\n[TEST 3] Order.compute_total()")
print("-" * 70)

order = Order("TEST-001", customer)
order.add_item(burger)   # $10.99
order.add_item(soda)     # $2.49
order.add_item(pizza)    # $12.99

total = order.compute_total()
expected = 10.99 + 2.49 + 12.99

print(f"✓ Order items: {len(order.get_items())}")
print(f"✓ Computed total: ${total:.2f}")
print(f"✓ Expected total: ${expected:.2f}")

assert abs(total - expected) < 0.01, f"Total should be ${expected:.2f}"
print("✅ PASS: compute_total() calculates correctly")

# Test empty order
empty_order = Order("EMPTY-001", customer)
empty_total = empty_order.compute_total()
print(f"✓ Empty order total: ${empty_total:.2f}")
assert empty_total == 0.0, "Empty order should be $0.00"

# Test duplicate items
dup_order = Order("DUP-001", customer)
dup_order.add_item(soda)  # $2.49
dup_order.add_item(soda)  # $2.49
dup_order.add_item(soda)  # $2.49
dup_total = dup_order.compute_total()
print(f"✓ Order with 3 sodas: ${dup_total:.2f}")
assert abs(dup_total - (3 * 2.49)) < 0.01, "Should sum all duplicates"

print("✅ PASS: compute_total() handles edge cases")

# ============================================================
# TEST 4: Customer.get_purchase_history()
# ============================================================
print("\n[TEST 4] Customer.get_purchase_history()")
print("-" * 70)

# Add orders to customer
customer.add_purchase(order)
customer.add_purchase(empty_order)
customer.add_purchase(dup_order)

history = customer.get_purchase_history()
print(f"✓ Purchase history length: {len(history)}")
assert len(history) == 3, "Should have 3 orders"

# Verify it returns a copy (defensive programming)
history.append("FAKE")  # Try to modify the copy
actual_history = customer.get_purchase_history()
print(f"✓ Actual history length after external modification: {len(actual_history)}")
assert len(actual_history) == 3, "Internal history should be unchanged"

print("✅ PASS: get_purchase_history() returns defensive copy")

# ============================================================
# TEST 5: Customer.verify_real_user()
# ============================================================
print("\n[TEST 5] Customer.verify_real_user()")
print("-" * 70)

new_customer = Customer("New User")
is_real_before = new_customer.verify_real_user()
print(f"✓ New customer is real user? {is_real_before}")
assert is_real_before == False, "New customer should not be verified"

new_order = Order("NEW-001", new_customer)
new_order.add_item(burger)
new_customer.add_purchase(new_order)

is_real_after = new_customer.verify_real_user()
print(f"✓ After 1 order, is real user? {is_real_after}")
assert is_real_after == True, "Customer with order should be verified"

print("✅ PASS: verify_real_user() works correctly")

# ============================================================
# TEST 6: Input Validation
# ============================================================
print("\n[TEST 6] Input Validation")
print("-" * 70)

# Test filter_by_category with empty string
try:
    menu.filter_by_category("")
    assert False, "Should raise ValueError"
except ValueError as e:
    print(f"✓ Empty category raises ValueError: {e}")

# Test find_item_by_name with empty string
try:
    menu.find_item_by_name("   ")
    assert False, "Should raise ValueError"
except ValueError as e:
    print(f"✓ Whitespace-only name raises ValueError: {e}")

# Test add_purchase with None
try:
    customer.add_purchase(None)
    assert False, "Should raise ValueError"
except ValueError as e:
    print(f"✓ None order raises ValueError: {e}")

print("✅ PASS: All validation works correctly")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("✅ ALL METHOD VERIFICATION TESTS PASSED!")
print("=" * 70)
print("\nVerified Methods:")
print("  1. Menu.filter_by_category() - Case-insensitive filtering ✓")
print("  2. Menu.find_item_by_name() - Case-insensitive search ✓")
print("  3. Order.compute_total() - Correct sum calculation ✓")
print("  4. Customer.get_purchase_history() - Defensive copy ✓")
print("  5. Customer.verify_real_user() - Purchase verification ✓")
print("  6. Input validation - All edge cases handled ✓")
print("=" * 70)
