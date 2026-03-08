from models import Food, Customer, Menu, Order


def test_order_total():
    """Test that compute_total() correctly sums item prices."""
    print("Running test_order_total...")
    
    # Create food items
    burger = Food("Burger", 8.99, "Entrees")
    fries = Food("Fries", 3.49, "Sides")
    soda = Food("Soda", 1.99, "Drinks")
    salad = Food("Salad", 5.99, "Sides")
    
    # Create customer and order
    customer = Customer("Alice")
    order = Order("ORD-001", customer)
    
    # Add items to order
    order.add_item(burger)
    order.add_item(fries)
    order.add_item(soda)
    order.add_item(salad)
    
    # Verify total
    expected_total = 8.99 + 3.49 + 1.99 + 5.99  # 20.46
    actual_total = order.compute_total()
    
    assert abs(actual_total - expected_total) < 0.01, \
        f"Expected total {expected_total}, but got {actual_total}"
    
    print(f"✓ Order total correctly computed: ${actual_total:.2f}")


def test_empty_order_total():
    """Test that compute_total() returns 0.0 for an empty order."""
    print("Running test_empty_order_total...")
    
    # Create customer and empty order
    customer = Customer("Bob")
    order = Order("ORD-002", customer)
    
    # Verify empty order has zero total
    total = order.compute_total()
    
    assert total == 0.0, \
        f"Expected empty order total to be 0.0, but got {total}"
    
    print(f"✓ Empty order total correctly returns: ${total:.2f}")


def test_filter_menu_by_category():
    """Test that filter_by_category() returns correct items (case-insensitive)."""
    print("Running test_filter_menu_by_category...")
    
    # Create menu with items in different categories
    burger = Food("Burger", 8.99, "Entrees")
    pizza = Food("Pizza", 10.99, "Entrees")
    fries = Food("Fries", 3.49, "Sides")
    salad = Food("Salad", 5.99, "Sides")
    soda = Food("Soda", 1.99, "Drinks")
    juice = Food("Juice", 2.49, "Drinks")
    
    menu = Menu()
    menu.add_item(burger)
    menu.add_item(pizza)
    menu.add_item(fries)
    menu.add_item(salad)
    menu.add_item(soda)
    menu.add_item(juice)
    
    # Test filtering by "Entrees"
    entrees = menu.filter_by_category("Entrees")
    assert len(entrees) == 2, \
        f"Expected 2 entrees, but got {len(entrees)}"
    assert burger in entrees and pizza in entrees, \
        "Expected burger and pizza in entrees"
    
    # Test filtering by "drinks" (case-insensitive)
    drinks = menu.filter_by_category("drinks")
    assert len(drinks) == 2, \
        f"Expected 2 drinks, but got {len(drinks)}"
    assert soda in drinks and juice in drinks, \
        "Expected soda and juice in drinks"
    
    # Test filtering by "SIDES" (uppercase)
    sides = menu.filter_by_category("SIDES")
    assert len(sides) == 2, \
        f"Expected 2 sides, but got {len(sides)}"
    assert fries in sides and salad in sides, \
        "Expected fries and salad in sides"
    
    # Test filtering by non-existent category
    desserts = menu.filter_by_category("Desserts")
    assert len(desserts) == 0, \
        f"Expected 0 desserts, but got {len(desserts)}"
    
    print(f"✓ Category filtering works correctly (case-insensitive)")
    print(f"  - Found {len(entrees)} Entrees")
    print(f"  - Found {len(drinks)} Drinks")
    print(f"  - Found {len(sides)} Sides")
    print(f"  - Found {len(desserts)} Desserts (none)")


def test_order_with_duplicates():
    """Test that orders can contain duplicate items and total is correct."""
    print("Running test_order_with_duplicates...")
    
    # Create food items
    burger = Food("Burger", 8.99, "Entrees")
    soda = Food("Soda", 1.99, "Drinks")
    
    # Create customer and order
    customer = Customer("Charlie")
    order = Order("ORD-003", customer)
    
    # Add duplicate items
    order.add_item(burger)
    order.add_item(burger)  # Second burger
    order.add_item(soda)
    order.add_item(soda)    # Second soda
    
    # Verify total includes both duplicates
    expected_total = (8.99 * 2) + (1.99 * 2)  # 21.96
    actual_total = order.compute_total()
    
    assert abs(actual_total - expected_total) < 0.01, \
        f"Expected total {expected_total}, but got {actual_total}"
    
    # Verify all 4 items are in order
    items = order.get_items()
    assert len(items) == 4, \
        f"Expected 4 items in order, but got {len(items)}"
    
    print(f"✓ Order with duplicates correctly computed: ${actual_total:.2f} (4 items)")


if __name__ == "__main__":
    print("=" * 60)
    print("Running ByteBites Test Suite")
    print("=" * 60)
    print()
    
    try:
        test_order_total()
        print()
        test_empty_order_total()
        print()
        test_filter_menu_by_category()
        print()
        test_order_with_duplicates()
        print()
        print("=" * 60)
        print("✓ All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print()
        print("=" * 60)
        print(f"✗ Test failed: {e}")
        print("=" * 60)
    except Exception as e:
        print()
        print("=" * 60)
        print(f"✗ Unexpected error: {e}")
        print("=" * 60)
