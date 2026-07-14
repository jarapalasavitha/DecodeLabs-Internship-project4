print("===== GENERAL KNOWLEDGE QUIZ =====")

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "2. Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"],
        "answer": "A"
    },
    {
        "question": "3. Which planet is called the Red Planet?",
        "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "4. Which is the largest ocean in the world?",
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
        "answer": "D"
    },
    {
        "question": "5. Which programming language are you learning?",
        "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
        "answer": "B"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good Job!")
elif percentage >= 40:
    print("Keep Practicing!")
else:
    print("Better Luck Next Time!")