from tkinter import *

def button_press(button):
    global equation_text
    equation_text = equation_text + str(button)
    equation_label.set(equation_text)

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        print("Wrong syntax!")
        equation_label.set("Error")
        equation_text = ""
    except ZeroDivisionError:
        print("Division by zero!!")
        equation_label.set("Error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set(equation_text)

window = Tk()
window.geometry("300x400")
window.config(bg="#e7cfbc")

equation_text = ""
equation_label = StringVar()

label1 = Label(window, bg="#e7cfbc")
label1.pack()

label = Label(window, textvariable=equation_label, width=25, height=2, bg="#fff4ec")
label.pack()

label2 = Label(window, bg="#e7cfbc")
label2.pack()

frame = Frame(window)
frame.pack()

button_1 = Button(frame, text="1", height=2, width=4, font=25, command=lambda: button_press(1), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_1.grid(row=0, column=0, padx=1, pady=1)

button_2 = Button(frame, text="2", height=2, width=4, font=25, command=lambda: button_press(2), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_2.grid(row=0, column=1, padx=1, pady=1)

button_3 = Button(frame, text="3", height=2, width=4, font=25, command=lambda: button_press(3), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_3.grid(row=0, column=2, padx=1, pady=1)

button_plus = Button(frame, text="+", height=2, width=4, font=25, command=lambda: button_press("+"), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_plus.grid(row=0, column=3, padx=1, pady=1)

button_4 = Button(frame, text="4", height=2, width=4, font=25, command=lambda: button_press(4), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_4.grid(row=1, column=0, padx=1, pady=1)

button_5 = Button(frame, text="5", height=2, width=4, font=25, command=lambda: button_press(5), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_5.grid(row=1, column=1, padx=1, pady=1)

button_6 = Button(frame, text="6", height=2, width=4, font=25, command=lambda: button_press(6), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_6.grid(row=1, column=2, padx=1, pady=1)

button_minus = Button(frame, text="-", height=2, width=4, font=25, command=lambda: button_press("-"), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_minus.grid(row=1, column=3, padx=1, pady=1)

button_7 = Button(frame, text="7", height=2, width=4, font=25, command=lambda: button_press(7), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_7.grid(row=2, column=0, padx=1, pady=1)

button_8 = Button(frame, text="8", height=2, width=4, font=25, command=lambda: button_press(8), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_8.grid(row=2, column=1, padx=1, pady=1)

button_9 = Button(frame, text="9", height=2, width=4, font=25, command=lambda: button_press(9), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_9.grid(row=2, column=2, padx=1, pady=1)

button_mul = Button(frame, text="*", height=2, width=4, font=25, command=lambda: button_press("*"), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_mul.grid(row=2, column=3, padx=1, pady=1)

button_0 = Button(frame, text="0", height=2, width=4, font=25, command=lambda: button_press(0), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_0.grid(row=3, column=0, padx=1, pady=1)

button_dot = Button(frame, text=".", height=2, width=4, font=25, command=lambda: button_press("."), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_dot.grid(row=3, column=1, padx=1, pady=1)

button_equal = Button(frame, text="=", height=2, width=4, font=25, command=equals, bg="#c98686", fg="#fff4ec", relief=FLAT)
button_equal.grid(row=3, column=2, padx=1, pady=1)

button_div = Button(frame, text="/", height=2, width=4, font=25, command=lambda: button_press("/"), bg="#c98686", fg="#fff4ec", relief=FLAT)
button_div.grid(row=3, column=3, padx=1, pady=1)

button_clear = Button(window, text="Clear", height=2, width=8, font=25, command=clear, bg="#966b9d", fg="#fff4ec", relief=FLAT)
button_clear.pack()
window.mainloop()