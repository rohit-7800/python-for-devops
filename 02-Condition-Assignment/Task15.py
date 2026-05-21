# Tax Calculation for Car Purchase

brand = input("Enter car brand: ")
price = float(input("Enter car price in lakh: "))

tax = 0

if brand == "Mahindra" and 7 <= price <= 10:
    tax = price * 0.05

elif brand == "Audi" and 10 <= price <= 15:
    tax = price * 0.10

elif brand == "Jaguar" and 15 <= price <= 20:
    tax = price * 0.25

elif brand == "Mercedes" and 20 <= price <= 25:
    tax = price * 0.30

else:
    print("No tax rule available for this car.")

print("Calculated Tax =", tax, "lakh")