from grocery_store.product import Product
from grocery_store.order import Order


kamala_order = Order([], "Kamala")

product_1 = Product("Apples", 3.47)
product_2 = Product("Oranges", 4.89)
product_3 = Product("Macbook", 1379.99)

kamala_order.add_product(product_1)
kamala_order.add_product(product_2)
kamala_order.add_product(product_3)

print(f"The order total for {kamala_order.customer_name} is " +
    f"{kamala_order.calculate_total()}")

