#!/usr/bin/env python3
import json
from pathlib import Path


def load_questions():
    data_path = Path(__file__).with_name("questions.json")
    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def choose_book(questions):
    books = sorted({q["book"] for q in questions})
    print("\nAvailable books:")
    for idx, book in enumerate(books, start=1):
        print(f"  {idx}. {book}")
    print("  0. All books")

    while True:
        choice = input("Choose a book (number): ").strip()
        if choice.isdigit():
            choice_num = int(choice)
            if choice_num == 0:
                return None
            if 1 <= choice_num <= len(books):
                return books[choice_num - 1]
        print("Please enter a valid number.")


def practice_loop(questions):
    print("\n=== Bible Quiz Practice ===")
    print("Type 'hint' to see the verse reference.")
    print("Type 'answer' to reveal the answer.")
    print("Type 'next' to skip or 'q' to quit.\n")

    question_index = 0
    while question_index < len(questions):
        question = questions[question_index]
        print(f"\n{question['question']}")
        for idx, option in enumerate(question["options"], start=1):
            print(f"  {idx}. {option}")

        while True:
            response = input("Your response: ").strip().lower()
            if response == "q":
                return
            if response == "hint":
                print(f"Hint: {question['reference']}")
                continue
            if response == "answer":
                correct_option = question["options"][question["answer_index"]]
                print(f"Answer: {correct_option}")
                break
            if response == "next":
                break
            if response.isdigit() and 1 <= int(response) <= len(question["options"]):
                selected = int(response) - 1
                if selected == question["answer_index"]:
                    print("Correct! ✅")
                else:
                    correct_option = question["options"][question["answer_index"]]
                    print(f"Not quite. Correct answer: {correct_option}")
                break
            print("Try 1-4, 'hint', 'answer', 'next', or 'q'.")

        question_index += 1


if __name__ == "__main__":
    all_questions = load_questions()
    chosen_book = choose_book(all_questions)
    if chosen_book:
        filtered = [q for q in all_questions if q["book"] == chosen_book]
    else:
        filtered = all_questions

    if not filtered:
        print("No questions found for that selection.")
    else:
        practice_loop(filtered)
