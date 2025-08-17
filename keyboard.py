from item import item

class keybord(item):
    
    def __init__(self, name: str, price: float, quantity = 0):
        # Call to cuper function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        