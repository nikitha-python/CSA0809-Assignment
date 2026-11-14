"""Run the executable demonstrations for CSA08 Assignment 1."""
from decimal import Decimal, ROUND_HALF_UP
from time import perf_counter
import milkrate as mr

def task2_types_and_decimal():
    print("\nTASK 2: TYPES, OPERATORS AND DECIMAL")
    values = [10, 10.0, "10", True, [10, 8.5]]
    for value in values:
        print(repr(value), "->", type(value).__name__)
    print("7 / 2 =", 7 / 2, "| 7 // 2 =", 7 // 2, "| 7 % 2 =", 7 % 2)
    print("-7 // 2 =", -7 // 2)
    print("float 0.1 + 0.2 =", 0.1 + 0.2)
    print("Decimal sum =", Decimal("0.1") + Decimal("0.2"))

def task3_variables():
    print("\nTASK 3: VARIABLES AND CONSTANTS")
    farmer_id = "F101"
    litres, fat, snf = Decimal("8.5"), Decimal("4.2"), Decimal("8.7")
    STANDARD_FAT = Decimal("3.5")
    print("Farmer:", farmer_id, "Litres:", litres, "Fat:", fat, "SNF:", snf)
    print("Standard fat:", STANDARD_FAT)
    a, b = 10, 20
    a, b = b, a
    print("Swapped values:", a, b)

def task4_expressions():
    print("\nTASK 4: RATE CALCULATION")
    for litres, fat, snf in [(10, "3.5", "8.5"), ("8.5", "4.2", "8.7"),
                             (12, "3.1", "8.3")]:
        rate = mr.rate_per_litre(fat, snf)
        print(f"{litres} L | fat={fat} | SNF={snf} | rate=Rs {rate}/L | "
              f"payment=Rs {mr.payout(litres, fat, snf)}")

def task5_input_validation():
    print("\nTASK 5: INPUT VALIDATION")
    examples = [
        ("F101", "8.5", "4.2", "8.7", "M"),
        ("F102", "ten", "4.2", "8.7", "E"),
        ("F103", "-2", "3.5", "8.5", "M"),
        ("F104", "10", "7.5", "8.5", "E"),
    ]
    for row in examples:
        try:
            print("Accepted:", mr.validate_entry(*row))
        except ValueError as error:
            print("Rejected:", row, "->", error)

def task6_functions():
    print("\nTASK 6: FUNCTIONS")
    print("Rate:", mr.rate_per_litre("4.2", "8.7"))
    print("Payout:", mr.payout("8.5", "4.2", "8.7"))

def task7_module_import():
    print("\nTASK 7: MODULE IMPORT")
    import decimal
    import math
    print("Imported standard modules:", decimal.__name__, math.__name__)
    print("Imported project module:", mr.__name__)
    print("Module payout:", mr.payout("8.5", "4.2", "8.7"))

def task8_algorithm_trace():
    print("\nTASK 8: ALGORITHM / HAND TRACE")
    readings = [(10, "3.5", "8.5"), ("8.5", "4.2", "8.7"), (12, "3.1", "8.3")]
    total = Decimal("0.00")
    for item in readings:
        amount = mr.payout(*item)
        total += amount
        print("Entry:", item, "Payment:", amount)
    print("Total payment:", total)

def task9_tests():
    print("\nTASK 9: AUTOMATED TESTS")
    mr._self_test()
    print("All built-in assertions passed.")

def task10_timing():
    print("\nTASK 10: FLOAT VS DECIMAL")
    amounts = ["33.40"] * 1000 + ["0.10"] * 3
    start = perf_counter()
    float_total = sum(float(x) for x in amounts)
    float_seconds = perf_counter() - start
    start = perf_counter()
    decimal_total = sum((Decimal(x) for x in amounts), Decimal("0.00"))
    decimal_seconds = perf_counter() - start
    print("Float total:", repr(float_total), f"({float_seconds:.6f} s)")
    print("Decimal total:", decimal_total, f"({decimal_seconds:.6f} s)")

def task11_recommended_design():
    print("\nTASK 11: RECOMMENDED DESIGN")
    sample_entries = [("10", "3.5", "8.5"), ("8.5", "4.2", "8.7")]
    total_litres, milk, bonus, final = mr.ten_day_total(sample_entries, month=1)
    print("Total litres:", total_litres, "Milk:", milk, "Bonus:", bonus, "Final:", final)

def task12_seasonal_bonus():
    print("\nTASK 12: SEASONAL RATE AND BONUS")
    for month in (2, 4):
        card = mr.get_rate_card(month)
        rate = mr.rate_per_litre("4.25", "8.63", card)
        print("Month", month, "| base", card.base, "| rate", rate)
    for quantity in ("500", "501"):
        entries = [(quantity, "3.5", "8.5")]
        print(quantity, "litres ->", mr.ten_day_total(entries, month=4))

if __name__ == "__main__":
    task2_types_and_decimal()
    task3_variables()
    task4_expressions()
    task5_input_validation()
    task6_functions()
    task7_module_import()
    task8_algorithm_trace()
    task9_tests()
    task10_timing()
    task11_recommended_design()
    task12_seasonal_bonus()
    print("\nAll task demonstrations completed.")
