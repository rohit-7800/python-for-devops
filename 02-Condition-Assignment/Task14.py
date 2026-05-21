# Arranging Three Numbers in Descending Order

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

numbers = [num1, num2, num3]

numbers.sort(reverse=True)

print("Numbers in Descending Order:", numbers[0], numbers[1], numbers[2])