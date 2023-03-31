from random import randint
import customtkinter as ctk


class NumberGuessingGame:
    def __init__(self, master: ctk.CTk) -> None:

        # GUI
        self.master = master
        self.master.geometry("300x200")
        self.master.resizable(False, False)
        self.master.wm_title("Spammer")

        # Guess number and guess
        self.number: int = randint(0, 9)
        self.guess_num: int = 0

        # Label
        self.label = ctk.CTkLabel(
            self.master,
            text="Guess a number between 0 - 9",
            font=("Jetbrains Mono", 14),
        )
        self.label.place(relx=0.5, rely=0.1, anchor="center")

        # Guess entry
        self.guess = ctk.CTkEntry(
            self.master,
            placeholder_text="0",
            width=30,
            height=30,
            border_width=2,
            corner_radius=10,
            font=("Jetbrains Mono", 14),
        )
        self.guess.place(relx=0.5, rely=0.3, anchor="center")

        # Guess checker button
        self.check = ctk.CTkButton(
            self.master,
            text="Guess",
            width=100,
            height=30,
            border_width=0,
            corner_radius=8,
            command=self.check_guess,
            hover_color="red",
        )
        self.check.place(relx=0.5, rely=0.5, anchor="center")

        # Result label
        self.result_label = ctk.CTkLabel(
            self.master,
            text="Goodluck!",
            font=("Jetbrains Mono", 14),
        )
        self.result_label.place(relx=0.5, rely=0.7, anchor="center")

        # Dark mode
        self.switch = ctk.CTkSwitch(
            self.master,
            text="Dark Mode",
            command=self.theme,
        )
        self.switch.place(relx=0.5, rely=0.9, anchor="center")

    def check_guess(self):
        guess = self.guess.get()
        self.guess.delete(0, ctk.END)

        try:
            guess = int(guess)
        except ValueError:
            self.result_label.configure(text="Invalid guess.")
            return

        if guess == self.number:
            self.result_label.configure(text=f"You're right! It's {self.number}.")
            self.guess.configure(state=ctk.DISABLED)
            self.check.configure(state=ctk.DISABLED)
        elif guess < self.number:
            self.result_label.configure(text="Too low!")
        else:
            self.result_label.configure(text="Too high!")

    def theme(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")


if __name__ == "__main__":
    app = ctk.CTk()
    gui = NumberGuessingGame(master=app)
    app.mainloop()
