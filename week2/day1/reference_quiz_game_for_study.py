# Function to display quiz questions
def display_question(question, options):
    print(question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    return int(input("Enter your answer (1/2/3/4): "))

# Function to check answer
def check_answer(answer, user_answer):
    return answer == user_answer

# Main program
if __name__ == "__main__":
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Rome"],
            "answer": 2
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Mars", "Saturn"],
            "answer": 2
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Emily Brontë"],
            "answer": 1
        }
    ]

    score = 0
    for idx, question in enumerate(questions):
        print(f"\nQuestion {idx + 1}:")
        user_answer = display_question(question["question"], question["options"])
        if check_answer(question["answer"], user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nQuiz complete!")
    print(f"Your score: {score} out of {len(questions)}")
