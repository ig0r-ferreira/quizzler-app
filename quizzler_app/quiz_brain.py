from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]) -> None:
        self.question_list = question_list
        self.question_number = 0
        self.hits = 0
        self.current_question: Question | None = None

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        return self.current_question.text

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str) -> bool:
        if self.current_question is not None and \
                self.current_question.answer.lower() == user_answer.lower():
            self.hits += 1
            return True

        return False
