import art
from random import shuffle
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main() -> None:
    question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]
    shuffle(question_bank)

    quiz = QuizBrain(question_bank)

    print(art.LOGO)
    while quiz.still_has_questions():
        try:
            quiz.next_question()
        except KeyboardInterrupt:
            quiz.question_number -= 1
            print(f"\n\nYou left the quiz with {len(question_bank) - quiz.question_number} questions missing.")
            break
    else:
        print(f"You complete the quiz.")

    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
