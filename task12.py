"""Task 12: Day-4 seasonal rate and ten-day bonus challenge."""
import milkrate as mr

print("TASK 12 - SEASONAL RATE AND BONUS")
for month in (2, 4):
    card = mr.get_rate_card(month)
    rate = mr.rate_per_litre("4.25", "8.63", card)
    print("Month", month, "base", card.base, "rate", rate)
for quantity in ("500", "501"):
    result = mr.ten_day_total([(quantity, "3.5", "8.5")], month=4)
    print(quantity, "litres ->", result)
