from grocery_store.product import Product

class Order:
    def __init__(self, products, customer_name):
        self.products = products
        self.customer_name = customer_name
        
    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for i in range(1, len(self.products)):
            total += self.products[i].price
        
        return total





        