"""Task 03: Variables, naming conventions and constants."""
from decimal import Decimal

STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
BASE_RATE = Decimal("30.00")
farmer_id = "F101"
litres, fat, snf = Decimal("8.5"), Decimal("4.2"), Decimal("8.7")
a, b = 10, 20
a, b = b, a
print("TASK 03 - VARIABLES AND CONSTANTS")
print(farmer_id, litres, fat, snf)
print("Constants:", STANDARD_FAT, STANDARD_SNF, BASE_RATE)
print("Swapped values:", a, b)
