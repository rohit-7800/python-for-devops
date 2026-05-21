# Bank Loan Approval System

age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
debts = int(input("Enter outstanding debts: "))

if (18 <= age <= 60) and (income >= 25000) and (credit_score >= 700) and (debts <= 10000):
    print("Loan Approved")
else:
    print("Loan Rejected")