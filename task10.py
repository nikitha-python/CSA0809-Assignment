"""Task 10: Compare float and Decimal totals and measure execution time."""
from decimal import Decimal
from statistics import median
from time import perf_counter

amounts = ["33.40"] * 1000 + ["0.10"] * 3
float_times, decimal_times = [], []
for _ in range(5):
    start = perf_counter(); float_total = sum(float(x) for x in amounts); float_times.append(perf_counter() - start)
    start = perf_counter(); decimal_total = sum((Decimal(x) for x in amounts), Decimal("0.00")); decimal_times.append(perf_counter() - start)
print("TASK 10 - FLOAT VS DECIMAL")
print("Float total:", repr(float_total), "median seconds:", f"{median(float_times):.8f}")
print("Decimal total:", decimal_total, "median seconds:", f"{median(decimal_times):.8f}")
