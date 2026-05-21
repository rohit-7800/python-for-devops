# Authentication System

# Predefined credentials
correct_username = "user1"
correct_password = "pass@123"

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
if username == correct_username and password == correct_password:
    print("Authentication successful.")

else:
    print("Authentication failed.")