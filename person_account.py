class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()    # (amount, description)
        self.expenses = set()   # (amount, description)

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"""Account Owner: {self.firstname} {self.lastname}
Total Income: {self.total_income()}
Total Expense: {self.total_expense()}
Account Balance: {self.account_balance()}"""