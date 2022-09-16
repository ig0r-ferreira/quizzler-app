import html
from random import shuffle

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


def main() -> None:
    question_bank = [
        Question(
            html.unescape(question["question"]), question["correct_answer"]
        ) for question in question_data
    ]
    shuffle(question_bank)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)
    quiz_ui.mainloop()


if __name__ == "__main__":
    main()
