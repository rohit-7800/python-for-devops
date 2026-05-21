# Salary Calculation Program

base_salary = 50000
bonus = 5000
tax_rate = 10
other_charges = 2000

# Calculate gross salary
gross_salary = base_salary + bonus

# Calculate tax
tax = (gross_salary * tax_rate) / 100

# Calculate net salary
net_salary = gross_salary - tax - other_charges

print("Gross Salary =", gross_salary)
print("Tax Amount =", tax)
print("Net Salary =", net_salary)