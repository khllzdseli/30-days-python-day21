from statistics import Statistics
from person_account import PersonAccount

# Level 1 test
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
print(data.describe())

print("\n-----------------\n")

# Level 2 test
acc = PersonAccount("Ali", "Mammadov")

acc.add_income(1000, "Salary")
acc.add_income(200, "Freelance")

acc.add_expense(300, "Rent")
acc.add_expense(100, "Food")

print(acc.account_info())