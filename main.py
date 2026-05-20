from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 1200, 5)
product2 = Product("Mouse", 25, 20)
product3 = Product("Keyboard", 75, 10)
product4 = Product("Monitor", 300, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

print("AVAILABLE PRODUCTS:")
manager.show_products()

print("\nTOTAL INVENTORY VALUE:")
print(manager.total_inventory_value(), "$")

cart = Cart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

print("\nCART CONTENT:")
cart.show_cart()

print("\nTOTAL FOR PAYMENT:")
print(cart.calculate_total(), "$")