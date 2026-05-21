# KBC Game (Quiz Game)

print("Welcome to KBC Game!")

start = input("Do you want to start the game? (yes/no): ")

if start.lower() != "yes":
    print("Game exited. Have a nice day!")
    exit()

# Questions (question, options, correct answer)
questions = [
    ("What is the capital of India?",
     ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
     "B"),

    ("Which language is used for AI?",
     ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
     "A"),

    ("2 + 2 * 2 = ?",
     ["A. 6", "B. 8", "C. 4", "D. 10"],
     "A"),

    ("Who developed Python?",
     ["A. Elon Musk", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Bill Gates"],
     "C"),

    ("Which planet is known as Red Planet?",
     ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
     "B")
]

scores = [1000, 2000, 3000, 5000, 10000]

total_score = 0
correct = 0
wrong = 0
skipped = 0

# Game loop
for i in range(len(questions)):
    q, options, answer = questions[i]

    print("\nQuestion", i + 1)
    print(q)

    for opt in options:
        print(opt)

    user = input("Enter your answer (A/B/C/D or S to skip): ").upper()

    if user == "S":
        skipped += 1
        print("Question skipped.")

    elif user == answer:
        total_score += scores[i]
        correct += 1
        print("Correct answer! +", scores[i])

    else:
        wrong += 1
        print("Wrong answer!")

# Final Result
print("\n===== GAME OVER =====")
print("Total Score:", total_score)
print("Correct Answers:", correct)
print("Wrong Answers:", wrong)
print("Skipped Questions:", skipped)