"""Task 07: Import and use the project module and standard modules."""
import decimal
import math
import milkrate as mr

print("TASK 07 - MODULE IMPORT")
print("Standard modules:", decimal.__name__, math.__name__)
print("Project module:", mr.__name__)
print("Imported payout function result:", mr.payout("8.5", "4.2", "8.7"))
