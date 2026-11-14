"""Task 05: Validate text input and report invalid values."""
import milkrate as mr

print("TASK 05 - INPUT VALIDATION")
examples = [("F101", "8.5", "4.2", "8.7", "M"), ("F102", "ten", "4.2", "8.7", "E"),
            ("F103", "-2", "3.5", "8.5", "M"), ("F104", "10", "7.5", "8.5", "E")]
for row in examples:
    try:
        print("Accepted:", mr.validate_entry(*row))
    except ValueError as error:
        print("Rejected:", row, "->", error)
