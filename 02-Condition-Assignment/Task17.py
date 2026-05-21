# Find the Greatest Number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Check greatest number
if num1 >= num2 and num1 >= num3:
    greatest = num1

elif num2 >= num1 and num2 >= num3:
    greatest = num2

else:
    greatest = num3

print("Greatest number is:", greatest)