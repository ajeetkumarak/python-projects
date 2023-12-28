from tkinter import *

THEME_COLOR = "#375362"


class UI:
    def __init__(self):
        window = Tk()
        window.config(bg=THEME_COLOR, padx=50, pady=1)
        window.title(string="Quizzer App")

        canvas = Canvas(width=400, height=400, bg="white")
        canvas.config(highlightthickness=0)
        canvas.create_text(200, 200, text="The vapour produced by e-cigarettes is actually water.")
        canvas.grid(row=1, column=1, columnspan=2)

        score_label = Label(text=f"Score: 1", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"), pady=40)
        score_label.grid(row=0, column=2)

        right = PhotoImage(file="images/true.png")
        wrong = PhotoImage(file="images/false.png")

        right_button = Button(image=right, bg=THEME_COLOR, highlightthickness=0)
        wrong_button = Button(image=wrong, bg=THEME_COLOR, highlightthickness=0)
        right_button.grid(row=4, column=1)
        wrong_button.grid(row=4, column=2)
        window.mainloop()


