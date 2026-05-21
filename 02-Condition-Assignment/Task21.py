# UPSC Selection Process

# Eligibility Check
age = int(input("Enter your age: "))
graduate = input("Are you a graduate? (yes/no): ")
nationality = input("Enter your nationality: ")

if age >= 21 and age <= 32:

    if graduate.lower() == "yes":

        if nationality.lower() == "indian":

            print("Eligible for UPSC.")
            print("Proceed to Prelims Exam")

            # Prelims Exam
            prelims_score = int(input("Enter Prelims score: "))
            prelims_cutoff = 80

            if prelims_score >= prelims_cutoff:

                print("You passed the Prelims.")
                print("Proceed to Mains Exam")

                # Mains Exam
                mains_score = int(input("Enter Mains score: "))
                mains_cutoff = 100

                if mains_score >= mains_cutoff:

                    print("You passed the Mains.")
                    print("Proceed to Interview")

                    # Interview
                    interview_score = int(input("Enter Interview score: "))
                    interview_cutoff = 60

                    if interview_score >= interview_cutoff:
                        print("Congratulations! You have cleared the UPSC.")

                    else:
                        print("You failed the Interview.")

                else:
                    print("You failed the Mains.")

            else:
                print("You failed the Prelims.")

        else:
            print("Ineligible: Nationality must be Indian.")

    else:
        print("Ineligible: Candidate must be a graduate.")

else:
    print("Ineligible: Age must be between 21 and 32.")