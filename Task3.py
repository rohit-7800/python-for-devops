# Retirement Age Calculator

age = int(input("Enter your age: "))

retirement_age = 65

if age < retirement_age:
    years_left = retirement_age - age
    print("You have", years_left, "years left until retirement.")
else:
    print("You have already reached retirement age.")