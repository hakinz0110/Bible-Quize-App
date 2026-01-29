#!/usr/bin/env python3
import json
import random
import time
from pathlib import Path

TIME_LIMIT_SECONDS = 60


def load_questions():
    data_path = Path(__file__).with_name("questions.json")
    with data_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def run_challenge():
    questions = load_questions()
    random.shuffle(questions)
    start_time = time.time()
    score = 0
    streak = 0
    best_streak = 0

    print("=== Bible Quiz Challenge ===")
    print(f"Answer as many as you can in {TIME_LIMIT_SECONDS} seconds.")
    print("Type 'q' to quit early.\n")

    for question in questions:
        elapsed = time.time() - start_time
        remaining = max(0, TIME_LIMIT_SECONDS - int(elapsed))
        if remaining <= 0:
            break

        print(f"Time left: {remaining}s")
        print(question["question"])
        for idx, option in enumerate(question["options"], start=1):
            print(f"  {idx}. {option}")

        response = input("Your answer (1-4 or 'q'): ").strip().lower()
        if response == "q":
            break
        if response.isdigit() and 1 <= int(response) <= len(question["options"]):
            selected = int(response) - 1
            if selected == question["answer_index"]:
                score += 1
                streak += 1
                best_streak = max(best_streak, streak)
                print("Correct! ✅\n")
            else:
                streak = 0
                correct_option = question["options"][question["answer_index"]]
                print(f"Wrong. Correct answer: {correct_option}\n")
        else:
            streak = 0
            print("Invalid response. No points awarded.\n")

    print("=== Challenge Over ===")
    print(f"Score: {score}")
    print(f"Best streak: {best_streak}")


if __name__ == "__main__":
    run_challenge()
