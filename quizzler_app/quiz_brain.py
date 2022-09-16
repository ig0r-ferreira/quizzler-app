from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        while True:
            user_answer = input(
                f"Question {self.question_number}: {current_question.text}\n"
                "True or False? "
            ).lower()
            if user_answer in ("true", "false"):
                break
            print("\033[1;31mType only true or false.\033[m")

        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str) -> None:
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!", end=" ")
        else:
            print("Wrong!", end=" ")

        print(f"Current score: {self.score}/{self.question_number}.\n")
