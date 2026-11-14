"""Task 02: Explore Python data types, operators and Decimal arithmetic."""
from decimal import Decimal

values = [10, 10.0, "10", True, [10, 8.5]]
print("TASK 02 - TYPES AND OPERATORS")
for value in values:
    print(repr(value), "->", type(value).__name__)
print("7 / 2 =", 7 / 2, "7 // 2 =", 7 // 2, "7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)
print("Float 0.1 + 0.2 =", 0.1 + 0.2)
print("Decimal 0.1 + 0.2 =", Decimal("0.1") + Decimal("0.2"))
