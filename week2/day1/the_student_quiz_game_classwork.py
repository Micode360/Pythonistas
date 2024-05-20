# QUIZ GAME
questions = [
    {
        "question": "Who won the premier league 2023/24",
        "options": ["Chelsea", "Arsenal", "Liverpool", "Manchester City"],
        "answer": "d"
    },
    {
        "question": "What is the smallest state in Nigeria",
        "options": ["Cross River", "Lagos", "Delta", "Borno"],
        "answer": "b"
    },
    {
        "question": "The most popular programming language in the world",
        "options": ["Javascript", "Python", "C", "Java"],
        "answer": "a"
    }
]
score = 0
correct = 0


while score < len(questions):
    print(f"{questions[score]["question"]}?")
    print(f"a. {questions[score]["options"][0]}")
    print(f"b. {questions[score]["options"][1]}")
    print(f"c. {questions[score]["options"][2]}")
    print(f"d. {questions[score]["options"][3]}")
    answer = input("Choose the right option (a/b/c/d): ")
    print(answer == questions[score]["answer"], "ANSWER")
    if answer.lower() == questions[score]["answer"]:
        print("correct")
        correct = correct + 1
        score = score + 1
        continue
    else:
        print("Incorrect Answer")
        score = score + 1
        continue
else:
    print(f"Your score is {correct} out of {len(questions)}")

