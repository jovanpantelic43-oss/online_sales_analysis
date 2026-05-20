class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)

    def show_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
            return

        for product in self.cart_items:
            product.display_info()

    def calculate_total(self):
        total = 0

        for product in self.cart_items:
            total += product.price

        return total