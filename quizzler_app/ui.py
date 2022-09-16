import tkinter as tk

from quiz_brain import QuizBrain

WIN_BG_COLOR: str = "#1E5A83"
CANVAS_BG_COLOR: str = "#202020"
CORRECT_COLOR: str = "#013B11"
WRONG_COLOR: str = "#871010"
QUESTION_FONT: tuple[str, int, str] = ("Trebuchet MS", 20, "italic")
INFO_FONT: tuple[str, int, str] = ("Trebuchet MS", 14, "bold")


class QuizInterface(tk.Tk):
    def __init__(self, quiz: QuizBrain) -> None:
        super().__init__()
        self.quiz = quiz
        self.title("Quizzler")
        self.config(padx=20, pady=40, bg=WIN_BG_COLOR)
        self.resizable(False, False)

        canvas_width, canvas_height = 500, 300
        self.canvas = tk.Canvas(
            width=canvas_width, height=canvas_height,
            highlightthickness=0, bg=CANVAS_BG_COLOR
        )

        self.question_identifier_text_id = self.canvas.create_text(
            65, 20,
            text="Question 0", font=INFO_FONT, fill="white"
        )

        self.question_text_id = self.canvas.create_text(
            canvas_width / 2, canvas_height / 2, width=470,
            text="Some question", font=QUESTION_FONT, fill="white"
        )
        self.hits_text_id = self.canvas.create_text(
            canvas_width - 70, 20,
            text="Hits: 00/00", font=INFO_FONT, fill="white"
        )

        self.true_img = tk.PhotoImage(file=r"img/true.png")
        self.true_button = tk.Button(
            image=self.true_img,
            highlightthickness=0, bd=0, activebackground=WIN_BG_COLOR,
            command=self.true_pressed
        )
        self.false_img = tk.PhotoImage(file="img/false.png")
        self.false_button = tk.Button(
            image=self.false_img,
            highlightthickness=0, bd=0, activebackground=WIN_BG_COLOR,
            command=self.false_pressed
        )

        self.canvas.grid(row=0, column=0, columnspan=2, padx=20, pady=(0, 40))
        self.true_button.grid(row=1, column=0)
        self.false_button.grid(row=1, column=1)

        self.eval('tk::PlaceWindow . center')
        self.get_question_text()

    def get_question_text(self) -> None:
        self.enable_buttons()

        self.canvas.config(bg=CANVAS_BG_COLOR)

        self.canvas.itemconfig(
            self.question_text_id,
            text=self.quiz.next_question()
        )

        self.canvas.itemconfig(
            self.question_identifier_text_id,
            text=f"Question {self.quiz.question_number}"
        )

    def true_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self) -> None:
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        self.disable_buttons()
        feedback_color = CORRECT_COLOR if is_right else WRONG_COLOR
        self.canvas.config(bg=feedback_color)
        self.update_hits()
        
        next_function = self.get_question_text \
            if self.quiz.still_has_questions() \
            else self.finish_game

        self.after(1500, next_function)

    def update_hits(self) -> None:
        self.canvas.itemconfig(
            self.hits_text_id,
            text=f"Hits: "
                 f"{self.quiz.hits:02}/{self.quiz.question_number:02}"
        )

    def finish_game(self) -> None:
        self.canvas.config(bg=CANVAS_BG_COLOR)
        self.canvas.itemconfig(
            self.question_text_id,
            text="Congratulations! You have completed the quiz."
        )
        self.disable_buttons()

    def disable_buttons(self) -> None:
        self.true_button.config(state=tk.DISABLED)
        self.false_button.config(state=tk.DISABLED)

    def enable_buttons(self) -> None:
        self.true_button.config(state=tk.NORMAL)
        self.false_button.config(state=tk.NORMAL)
