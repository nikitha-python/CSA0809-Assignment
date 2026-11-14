"""Task 04: Calculate milk rate and payout using the shared module."""
import milkrate as mr

print("TASK 04 - EXPRESSIONS AND RATE CALCULATION")
examples = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7"), ("12", "3.1", "8.3")]
for litres, fat, snf in examples:
    rate = mr.rate_per_litre(fat, snf)
    print(f"{litres} L | fat={fat} | SNF={snf} | rate=Rs {rate}/L | payment=Rs {mr.payout(litres, fat, snf)}")
