#!/usr/bin/env python3
import json
import random
from pathlib import Path

def load_questions():
    data_path = Path(__file__).with_name("questions.json")
    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def ask_question(question_data, index, total):
    print(f"\nQuestion {index}/{total}")
    print(f"{question_data['question']}")
    for i, option in enumerate(question_data["options"], start=1):
        print(f"  {i}. {option}")

    while True:
        choice = input("Your answer (1-4 or 'q' to quit): ").strip().lower()
        if choice == "q":
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(question_data["options"]):
            return int(choice) - 1
        print("Please enter 1-4 or 'q'.")


def run_quiz():
    questions = load_questions()
    random.shuffle(questions)
    total_questions = min(10, len(questions))
    score = 0
    results = []

    print("=== Bible Quiz Classic ===")
    print("Answer the questions. Type 'q' anytime to quit.\n")

    for idx, question in enumerate(questions[:total_questions], start=1):
        user_answer = ask_question(question, idx, total_questions)
        if user_answer is None:
            break
        correct = user_answer == question["answer_index"]
        results.append((question, correct))
        if correct:
            print("Correct! ✅")
            score += 1
        else:
            correct_option = question["options"][question["answer_index"]]
            print(f"Not quite. The correct answer is: {correct_option}")

    print("\n=== Quiz Summary ===")
    print(f"Score: {score}/{len(results)}")
    for entry, correct in results:
        status = "✅" if correct else "❌"
        print(f"{status} {entry['reference']} - {entry['question']}")


if __name__ == "__main__":
    run_quiz()
