# Employee Salary Based on Experience

experience = int(input("Enter years of experience: "))

if experience >= 10:
    salary = 80000
    print("Senior employee")

    if experience > 15:
        salary += 5000
        print("Experience exceeds 15 years. Bonus added.")

elif experience >= 5:
    salary = 50000
    print("Mid-level employee")

else:
    salary = 30000
    print("Junior employee")

print("Salary:", salary)