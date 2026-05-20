from product import Product
from product_manager import ProductManager

manager = ProductManager()

product1 = Product("Laptop", 1200, 5)
product2 = Product("Mouse", 25, 20)
product3 = Product("Keyboard", 75, 10)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("AVAILABLE PRODUCTS:")
manager.show_products()

print("\nTOTAL INVENTORY VALUE:")
print(manager.total_inventory_value(), "$")