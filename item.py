from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Any


class Item:
    """Represents a generic store item.

    Concepts demonstrated:
    - Class vs instance attributes (pay_rate, all)
    - Encapsulation via private attributes (__name, __price)
    - Properties with validation (name, price)
    - Classmethod for alternative constructors (instantiate_from_csv)
    - Staticmethod for utility logic (is_integer)
    - Dunder methods (__repr__)
    """

    # Class attributes (shared by all instances)
    pay_rate: float = 0.8  # 20% discount
    all: List["Item"] = []

    def __init__(self, name: str, price: float, quantity: int = 0) -> None:
        """Create a new item.

        Args:
            name: Item name (max 30 chars).
            price: Unit price (>= 0).
            quantity: Units in stock (>= 0).

        Raises:
            ValueError: If price or quantity are negative, or name too long.
            TypeError: If provided types are incorrect.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an integer")

        if price < 0:
            raise ValueError(f"price {price} must be >= 0")
        if quantity < 0:
            raise ValueError(f"quantity {quantity} must be >= 0")
        if len(name) > 30:
            raise ValueError("name is too long (max 30 chars)")

        # Private attributes (encapsulation)
        self.__name: str = name
        self.__price: float = float(price)

        # Public attribute (by convention)
        self.quantity: int = quantity

        # Keep track of all instances
        Item.all.append(self)

    # -------------------- Properties (encapsulation) --------------------
    @property
    def name(self) -> str:
        """Read/write name with validation."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if len(value) == 0:
            raise ValueError("name cannot be empty")
        if len(value) > 30:
            raise ValueError("name is too long (max 30 chars)")
        self.__name = value

    @property
    def price(self) -> float:
        """Read-only price; modify via helpers (apply_discount/increment)."""
        return self.__price

    # -------------------- Business logic methods --------------------
    def calculate_total_price(self) -> float:
        """Total inventory value for this item (price * quantity)."""
        return self.__price * self.quantity

    def apply_discount(self) -> None:
        """Apply class-level discount (pay_rate) to price."""
        self.__price = self.__price * Item.pay_rate

    def apply_increment(self, increment_value: float) -> None:
        """Increase price by a percentage (e.g., 0.2 = +20%)."""
        if increment_value < 0:
            raise ValueError("increment_value must be >= 0")
        self.__price = self.__price * (1 + increment_value)

    # -------------------- Alt constructors / utilities --------------------
    @classmethod
    def instantiate_from_csv(cls) -> List["Item"]:
        """Create items from items.csv located next to this file.

        Returns the list of created Item instances.
        """
        csv_path = Path(__file__).with_name("items.csv")
        created: List[Item] = []
        with csv_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                created.append(
                    cls(
                        name=str(row.get("name", "")).strip().strip("\"") or "Unnamed",
                        price=float(row.get("price", 0) or 0),
                        quantity=int(row.get("quantity", 0) or 0),
                    )
                )
        return created

    @staticmethod
    def is_integer(num: Any) -> bool:
        """Return True if num is an int or a float with no fractional part."""
        if isinstance(num, bool):  # bool is a subclass of int, exclude it
            return False
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)

    # -------------------- Dunder methods --------------------
    def __repr__(self) -> str:  # Helpful for debugging/printing lists
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    # -------------------- Example of (fake) private helpers --------------------
    def __connect(self, smtp_server: str) -> None:
        # Imagine real email setup here
        _ = smtp_server

    def __prepare_body(self) -> str:
        return (
            "Hello,\n"
            f"We have {self.name} available {self.quantity} times.\n"
            "Regards, Store Bot\n"
        )

    def __send(self) -> None:
        # Imagine sending the email here
        return None

    def send_email(self) -> None:
        """Public API that composes the private helpers (abstraction)."""
        self.__connect("smtp.example.com")
        body = self.__prepare_body()
        self.__send()
        # Not returning the body to keep the API minimal; this is illustrative only.


