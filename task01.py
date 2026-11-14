"""Task 01: Problem understanding and data design for the milk payment calculator."""
from decimal import Decimal

# One delivery is represented as a record-like tuple, not separate variables per farmer.
example_entry = ("F101", Decimal("10.0"), Decimal("3.5"), Decimal("8.5"), "M", 4)

print("TASK 01 - INPUT / OUTPUT / DATA DESIGN")
print("Input fields: farmer ID, litres, fat %, SNF %, shift, month")
print("Output fields: rate per litre, delivery payment, ten-day total and bonus")
print("Example record:", example_entry)
print("Use a list of records for many deliveries: O(n) storage and O(n) processing.")
