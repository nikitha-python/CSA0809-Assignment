"""Task 08: Algorithm and hand-trace of sample payments."""
from decimal import Decimal
import milkrate as mr

print("TASK 08 - ALGORITHM / HAND TRACE")
readings = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3")]
total = Decimal("0.00")
for item in readings:
    amount = mr.payout(*item)
    total += amount
    print("Entry:", item, "Payment:", amount)
print("Total payment:", total)
