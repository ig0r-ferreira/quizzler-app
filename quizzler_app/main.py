import html
from random import shuffle

import art
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


def main() -> None:
    question_bank = [
        Question(
            html.unescape(question["question"]), question["correct_answer"]
        )
        for question in question_data
    ]
    shuffle(question_bank)

    quiz = QuizBrain(question_bank)

    print(art.LOGO)
    while quiz.still_has_questions():
        try:
            quiz.next_question()
        except KeyboardInterrupt:
            quiz.question_number -= 1
            print(f"\n\nYou left the quiz with "
                  f"{len(question_bank) - quiz.question_number} "
                  f"questions missing.")
            break
    else:
        print("You complete the quiz.")

    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
