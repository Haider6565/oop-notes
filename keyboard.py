from item import Item


class Keyboard(Item):
    """Specialized Item representing a keyboard.

    Demonstrates simple inheritance with no new attributes.
    """

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        # Call to super to reuse Item's initialization
        super().__init__(name, price, quantity)
