from item import Item
from phone import Phone
from keyboard import Keyboard


def demo() -> None:
	# Create specialized items
	kbd = Keyboard("Vivo Keyboard", 100, 3)
	ph = Phone("JSC Phone v10", 500, 5, broken_phones=1)

	# Read properties
	print("Keyboard name:", kbd.name)
	print("Phone price before discount:", ph.price)

	# Apply class-wide discount
	Item.pay_rate = 0.9  # 10% discount for all items
	ph.apply_discount()
	print("Phone price after discount:", ph.price)

	# Calculate totals
	print("Keyboard total value:", kbd.calculate_total_price())
	print("Working phones in stock:", ph.working_inventory())

	# Instantiate from CSV
	created = Item.instantiate_from_csv()
	print("Created from CSV:", created)

	# Explore the class-level registry of all instances
	print("All items (including Keyboard/Phone):")
	for obj in Item.all:
		print(" -", obj)


if __name__ == "__main__":
	demo()





