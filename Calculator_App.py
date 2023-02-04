from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=50,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_add():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "+"
    Gnum1 = float(num1)
    e.delete(0, END)

def button_subtract():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "-"
    Gnum1 = float(num1)
    e.delete(0, END)


def button_multiply():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "*"
    Gnum1 = float(num1)
    e.delete(0, END)

def button_divide():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "/"
    Gnum1 = float(num1)
    e.delete(0, END)

def button_Modulo():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "%"
    Gnum1 = float(num1)
    e.delete(0, END)
def button_power2():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "^2"
    Gnum1 = float(num1)
    e.insert(END, "²")
    # e.delete(0, END)
def button_powerX():
    num1 = e.get()
    global Gnum1
    global operator
    operator = "^n"
    Gnum1 = float(num1)
    e.insert(END, "^")
    # e.delete(0, END)

def button_equal():
    current = e.get()
    e.delete(0, END)
    if operator == "+":
        ans = Gnum1 + int(current)
        e.insert(0, str(ans))
    elif operator == "-":
        ans = Gnum1 - int(current)
        e.insert(0, str(ans))
    elif operator == "*":
        ans = Gnum1 * int(current)
        e.insert(0, str(ans))
    elif operator == "/":
        ans = Gnum1 / int(current)
        e.insert(0, str(ans))
    elif operator == "%":
        ans = Gnum1 % int(current)
        e.insert(0, str(ans))
    elif operator == "^2":
        ans = Gnum1 ** 2
        e.insert(0, str(ans))
    elif operator == "^n":
        currentStr = current
        split = currentStr.rsplit('^', 1)
        num2 = float(split[-1])
        ans = pow(Gnum1, int(num2))
        e.insert(0, str(ans))

#Define the buttons

button_1 = Button(root, text="1", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", bg="#dbfffc", padx=40,pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", bg="#dbfffc", padx=39,pady=20, command=button_add)
button_equal = Button(root, text="=", bg="#dbfffc", padx=94,pady=20, command=button_equal)
button_clear = Button(root, text="clear", bg="#ff544d", padx=86,pady=20, command=button_clear)

button_subtract = Button(root, text="-", bg="#dbfffc", padx=40,pady=20, command=button_subtract)
button_multiply = Button(root, text="*", bg="#dbfffc", padx=41,pady=20, command=button_multiply)
button_divide = Button(root, text="/", bg="#dbfffc", padx=41,pady=20, command=button_divide)
button_modulo = Button(root, text="Modulo", bg="#dbfffc", padx=22,pady=20, command=button_Modulo)
button_power2 = Button(root, text="x²", bg="#dbfffc", padx=38,pady=20, command=button_power2)
button_powerX = Button(root, text="xⁿ", bg="#dbfffc", padx=38,pady=20, command=button_powerX)


#Put buttons on screen
button_clear.grid(row=1, column=0, columnspan=2)
button_modulo.grid(row=1, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)


button_add.grid(row=6, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_subtract.grid(row=7, column=0)
button_power2.grid(row=6, column=1)
button_powerX.grid(row=6, column=2)

button_equal.grid(row=7, column=1, columnspan=2)



root.mainloop()