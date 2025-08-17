# Python OOP Notes (Practical Guide)

This repo is a compact, hands-on set of notes and examples to learn and practice Object-Oriented Programming (OOP) in Python.

What you'll find:
- Encapsulation with properties and private attributes
- Class vs instance attributes
- Inheritance and specialization
- Classmethods and staticmethods
- Dunder methods like `__repr__`
- Polymorphism and duck typing

Files overview:
- `class.py` – the simplest starting point (`ItemBasic`) showing methods and attributes
- `item.py` – a robust `Item` class with properties, class attributes, alt constructors, and utilities
- `phone.py` – `Phone` subclass with extra state and behavior
- `keyboard.py` – `Keyboard` subclass (simple inheritance)
- `polymor.py` – built-in polymorphism and duck typing examples
- `main.py` – demo script tying things together
- `items.csv` – sample data for the CSV constructor

Quick try:
1) Run `main.py` to see the demo in action and items loaded from CSV.
2) Open each file to read the docstrings and comments.

Key concepts explained
1) Encapsulation (hide internal details)
- We store `name` and `price` as private (`__name`, `__price`) and expose them via properties.
- Validation happens in setters/constructor so your objects stay correct.

2) Class vs instance attributes
- `Item.pay_rate` is shared by all items and used by `apply_discount()`.
- `quantity` is per-instance, unique to each object.

3) Inheritance
- `Keyboard(Item)` reuses all Item logic but doesn't add new fields.
- `Phone(Item)` adds `broken_phones` and a method `working_inventory()`.

4) Classmethods and staticmethods
- `Item.instantiate_from_csv()` is an alternative constructor reading `items.csv`.
- `Item.is_integer()` is a utility that doesn't depend on a specific instance.

5) Dunder methods
- `__repr__` provides a helpful text representation for debugging and lists.

6) Polymorphism
- Built-in: `len()` works on strings, lists, etc.
- Duck typing: any object with an `export()` method can be passed to `run_export()`.

Tips
- Prefer clear names (`Item`, `Phone`, `Keyboard`) and type hints.
- Keep side-effects out of import-time code (no top-level test executions in modules).
- Use docstrings/comments to capture the “why”, not just the “what”.