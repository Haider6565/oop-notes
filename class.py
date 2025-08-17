class ItemBasic:
    """A minimal example showing how a class groups data and behavior."""

    # Methods always take `self` as the first parameter.
    def calculate_total_price(self, price: float, quantity: int) -> float:
        return price * quantity


# Create two objects (instances) of ItemBasic at runtime
item1 = ItemBasic()
item1.name = "phone"  # dynamic attribute assignment for simplicity
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = ItemBasic()
item2.name = "laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

