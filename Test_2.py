class RestaurantItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discounted_price(self, discount):
        original_price = self.price
        discount_price = original_price - (original_price * discount / 100)

        print("Original Price is:", original_price)
        print("After apply discount the price is:", discount_price)


class Pizza(RestaurantItem):
    def __init__(self, name, price, discount, size, toppings):
        super().__init__(name, price)
        self.discount = discount
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        if self.size == "Large":
            self.price += 100
        elif self.size == "Medium":
            self.price += 50
        else:
            self.price = self.price
        return self.price


    def show_items(self):
        print("Name:", self.name)
        print("Size of Pizza:", self.size)
        print("Toppings:", self.toppings)

        print("The price of the Pizza is:")
        self.calculate_price()
        super().discounted_price(self.discount)

r = Pizza("FarmHouse", 300, 10, "Large", "Cheese")
r.show_items()