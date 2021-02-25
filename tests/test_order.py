import pytest
from grocery_store.order import Order
from grocery_store.product import Product

def test_order_creation():
    # Arrange
    product_one = Product("Trombone", 478.95)
    product_two = Product("Guitar", 327.99)
    product_three = Product("Triangle", 2)
    products = [product_one, product_two, product_three]

    # Act
    sample_order = Order(products, "Shona Frederick")

    # Assert
    assert len(sample_order.products) == 3
    assert sample_order.customer_name == "Shona Frederick"
    for product in products:
        assert product in sample_order.products

def test_order_creation_with_no_products():
    # Arrange
    products = []

    # Act
    sample_order = Order(products, "Shona Frederick")

    # Assert
    assert len(sample_order.products) == 0
    assert sample_order.customer_name == "Shona Frederick"

def test_add_product():
    # Arrange
    product_one = Product("Trombone", 478.95)
    product_two = Product("Guitar", 327.99)
    product_three = Product("Triangle", 2)
    products = [product_one, product_two, product_three]
    sample_order = Order(products, "Shona Frederick")

    new_product = Product("Bass", 115)

    # Act
    sample_order.add_product(new_product)

    # Assert
    assert len(sample_order.products) == 4
    assert new_product in sample_order.products
    
def test_calculate_total_with_no_products():
    # Arrange
    order = Order([], "Shona Frederick")

    # Act
    total = order.calculate_total()

    # Assert
    assert total == 0

def test_calculate_total_with_multiple_products():
    # Arrange
    product_one = Product("Trombone", 478.95)
    product_two = Product("Guitar", 327.99)
    product_three = Product("Triangle", 2)
    products = [product_one, product_two, product_three]

    order = Order(products, "Shona Frederick")


    # Act
    total = order.calculate_total()

    # Assert
    assert total == pytest.approx(478.95 + 327.99 + 2) 