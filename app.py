from utils import calculate_total
from analytics import get_average
expenses = [100, 250, 50, 300]
total = calculate_total(expenses)
average = get_average(expenses)


print("My Expense Tracker")
print("-------------------")
print("Expenses:", expenses)
print("Total:", total)
print("Average:", average)

