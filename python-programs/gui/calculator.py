from tkinter import END, Button, Entry, Tk

root = Tk()
root.title("Calculator")

e = Entry(root, width=45, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def btn_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def btn_add():
    global operator
    operator = "plus"

    global num1
    num1 = e.get()
    e.delete(0, END)


def btn_subtract():
    global operator
    operator = "minus"

    global num1
    num1 = e.get()
    e.delete(0, END)


def btn_multiply():
    global operator
    operator = "times"

    global num1
    num1 = e.get()
    e.delete(0, END)


def btn_divide():
    global operator
    operator = "divide"

    global num1
    num1 = e.get()
    e.delete(0, END)


def btn_equal():
    num2 = e.get()
    e.delete(0, END)

    if operator == "plus":
        e.insert(0, eval(f"{num1} + {num2}"))
    elif operator == "minus":
        e.insert(0, eval(f"{num1} - {num2}"))
    elif operator == "times":
        e.insert(0, eval(f"{num1} * {num2}"))
    else:
        try:
            e.insert(0, eval(f"{num1} / {num2}"))
        except ZeroDivisionError:
            e.insert(0, "Infinity")


def btn_clear():
    e.delete(0, END)


btn1 = Button(
    root,
    text="1",
    padx=40,
    pady=20,
    command=lambda: btn_click(1),
)
btn2 = Button(
    root,
    text="2",
    padx=40,
    pady=20,
    command=lambda: btn_click(2),
)
btn3 = Button(
    root,
    text="3",
    padx=40,
    pady=20,
    command=lambda: btn_click(3),
)
btn4 = Button(
    root,
    text="4",
    padx=40,
    pady=20,
    command=lambda: btn_click(4),
)
btn5 = Button(
    root,
    text="5",
    padx=40,
    pady=20,
    command=lambda: btn_click(5),
)
btn6 = Button(
    root,
    text="6",
    padx=40,
    pady=20,
    command=lambda: btn_click(6),
)
btn7 = Button(
    root,
    text="7",
    padx=40,
    pady=20,
    command=lambda: btn_click(7),
)
btn8 = Button(
    root,
    text="8",
    padx=40,
    pady=20,
    command=lambda: btn_click(8),
)
btn9 = Button(
    root,
    text="9",
    padx=40,
    pady=20,
    command=lambda: btn_click(9),
)
btn0 = Button(
    root,
    text="0",
    padx=40,
    pady=20,
    command=lambda: btn_click(0),
)
btnp = Button(
    root,
    text=".",
    padx=40,
    pady=20,
    command=lambda: btn_click("."),
)

add_btn = Button(
    root,
    text="+",
    padx=40,
    pady=20,
    command=btn_add,
    bg="#87CEEB",
)
subtract_btn = Button(
    root,
    text="−",
    padx=40,
    pady=20,
    command=btn_subtract,
    bg="#87CEEB",
)
multiply_btn = Button(
    root,
    text="×",
    padx=40,
    pady=20,
    command=btn_multiply,
    bg="#87CEEB",
)
divide_btn = Button(
    root,
    text="÷",
    padx=40,
    pady=20,
    command=btn_divide,
    bg="#87CEEB",
)

equal_btn = Button(
    root,
    text="=",
    padx=40,
    pady=20,
    command=btn_equal,
    bg="#87CEEB",
)
clear_btn = Button(
    root,
    text="C",
    padx=180,
    pady=20,
    command=btn_clear,
    bg="#87CEEB",
)

btn1.grid(row=4, column=0)
btn2.grid(row=4, column=1)
btn3.grid(row=4, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)
btn0.grid(row=5, column=0)
btnp.grid(row=5, column=1)

add_btn.grid(row=5, column=3)
subtract_btn.grid(row=4, column=3)
multiply_btn.grid(row=3, column=3)
divide_btn.grid(row=2, column=3)

equal_btn.grid(row=5, column=2)
clear_btn.grid(row=1, column=0, columnspan=4)

root.mainloop()
