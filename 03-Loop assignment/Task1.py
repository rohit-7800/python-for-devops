# Print even and odd numbers from 1 to 20

print("Even numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("\nOdd numbers:")
for i in range(1, 21):
    if i % 2 != 0:
        print(i)