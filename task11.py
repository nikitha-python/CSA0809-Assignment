"""Task 11: Demonstrate the recommended Decimal/module-based design."""
import milkrate as mr

print("TASK 11 - RECOMMENDED DESIGN")
entries = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7")]
total_litres, milk, bonus, final = mr.ten_day_total(entries, month=1)
print("Total litres:", total_litres)
print("Milk payment:", milk)
print("Bonus:", bonus)
print("Final amount:", final)
print("Recommendation: Decimal, centralized RateCard, validation and automated tests.")
