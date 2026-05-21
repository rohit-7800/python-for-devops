# Library Charge Calculation

days = int(input("Enter the number of days the book was borrowed: "))

if days <= 5:
    charge = days * 2

elif days <= 10:
    charge = days * 3

elif days <= 15:
    charge = days * 4

else:
    charge = days * 5

print("Library Charge = Rs.", charge)