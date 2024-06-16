# quiz.py

# Define the questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Berlin", "C. Paris", "D. Madrid"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Oxygen", "C. Osmium", "D. Silver"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Jane Austen"],
        "answer": "A"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0

    for i, question in enumerate(quiz_questions):
        print(f"Question {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        
        answer = input("Enter the letter of your answer: ").strip().upper()
        
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}\n")

    print(f"Your final score is {score} out of {len(quiz_questions)}")

if __name__ == "__main__":
    run_quiz()
