class Product:
    def __init__(self, name, quantity, description, price):
        self.name = name
        self.quantity = quantity
        self.description = description
        self.price = price

    def check_quantity(self, count) -> bool:
        return self.quantity >= count

    def buy(self, count):
        if count > self.quantity:
            raise ValueError("Not enough products in stock")
        self.quantity -= count

    def __hash__(self):
        return hash((self.name, self.description))


class Cart:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            return
        if remove_count is None or remove_count >= self.products[product]:
            self.products.pop(product)
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return sum(p.price * c for p, c in self.products.items())

    def buy(self):
        for p, c in self.products.items():
            if not p.check_quantity(c):
                raise ValueError("Not enough products in stock")
        for p, c in list(self.products.items()):
            p.buy(c)
        self.clear()