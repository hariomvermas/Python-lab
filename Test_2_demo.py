class RestaurantItem:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def show_price(self):
        original_price = self.price
        discount_price = original_price - (original_price * self.discount / 100)
        print("Original Price:", original_price)
        print("After discount price:", discount_price)


class Pizza(RestaurantItem):
    def __init__(self, name, price, discount, size, toppings):
        super().__init__(name, price, discount)
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        self.price = self.price + 20

    def show_items(self):
        print("Name:", self.name)
        print("Size:", self.size)
        print("Toppings:", self.toppings)

        self.calculate_price()   # add toppings price
        super().show_price()


p = Pizza("FarmHouse", 300, 10, "Large", "Cheese")
p.show_items()