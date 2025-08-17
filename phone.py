from item import Item


class Phone(Item):
    """Specialized Item representing a phone, with broken units tracked."""

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int = 0,
        broken_phones: int = 0,
    ) -> None:
        # Call to super to inherit Item's attributes/validation
        super().__init__(name, price, quantity)

        if not isinstance(broken_phones, int):
            raise TypeError("broken_phones must be an integer")
        if broken_phones < 0:
            raise ValueError(
                f"broken_phones {broken_phones} must be >= 0"
            )

        self.broken_phones: int = broken_phones

    def working_inventory(self) -> int:
        """Return count of working (non-broken) phones."""
        return max(self.quantity - self.broken_phones, 0)
