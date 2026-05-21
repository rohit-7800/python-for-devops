# Students Interview Eligibility Checker

academic_score = float(input("Enter academic score (%): "))
attendance = float(input("Enter attendance percentage (%): "))
extra = input("Extracurricular participation (yes/no): ").strip().lower()

if academic_score >= 75 and attendance >= 80 and extra == "yes":
    print("Eligible for Interview")
else:
    print("Not Eligible for Interview")