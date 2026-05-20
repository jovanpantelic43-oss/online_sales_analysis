
from product import Product
from product_manager import ProductManager
from cart import Cart

# Kreiranje ProductManager instance
manager = ProductManager()

# Kreiranje proizvoda
product1 = Product("Gaming Laptop", 1500, 3)
product2 = Product("Wireless Mouse", 40, 15)
product3 = Product("Mechanical Keyboard", 120, 8)
product4 = Product("Monitor", 300, 5)

# Dodavanje proizvoda u manager
manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)
manager.add_product(product4)

# Kreiranje korpe
cart = Cart()

# Dodavanje proizvoda u korpu
cart.add_to_cart(product1)
cart.add_to_cart(product2)
cart.add_to_cart(product3)

# Prikaz sadržaja korpe
print("\nCART CONTENT:")
cart.show_cart()

# Ukupna vrednost korpe
print("\nTOTAL FOR PAYMENT:")
print(cart.calculate_total(), "$")