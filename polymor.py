"""Polymorphism examples.

1) Built-in polymorphism: the same function `len` works on many types.
2) Duck typing: a function works with any object that implements the needed methods.
"""

# Built-in polymorphism
name = "Jim"  # str
print(len(name))  # 3

some_list = ["Some", "Name"]  # list
print(len(some_list))  # 2


# Duck typing example
class PdfExporter:
	def export(self) -> str:
		return "Exporting as PDF"


class CsvExporter:
	def export(self) -> str:
		return "Exporting as CSV"


def run_export(exporter) -> None:
	"""Works with any object providing an `export()` method (duck typing)."""
	print(exporter.export())


run_export(PdfExporter())
run_export(CsvExporter())