# Library Charge Calculation

# Input
days = int(input("Enter number of days book was borrowed: "))

# Calculate charges
if days <= 5:
    charge = days * 2

elif days <= 10:
    charge = days * 3

elif days <= 15:
    charge = days * 4

else:
    charge = days * 5

# Output
print("Total library charge = ₹", charge)