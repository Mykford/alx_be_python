monthly_income = input("Enter your monthly income: ")
monthly_income = int(monthly_income)
monthly_expenses = input("Enter your total monthly expenses: " )
monthly_expenses = int(monthly_expenses)
savings = monthly_income - monthly_expenses
projected_savings = savings * 12+ (savings * 0.05 * 12)
print("Your monthly savings are ", savings)
print("Projected savings after one year, with interest, is: ", projected_savings)