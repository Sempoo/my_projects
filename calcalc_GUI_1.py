import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg_box

main_window = tk.Tk()
main_window.title('Calcalc')

menu_bar = Menu(main_window)
main_window.config(menu=menu_bar)

tabs = ttk.Notebook(main_window)

tab_1 = ttk.Frame(tabs)
tabs.add(tab_1, text='Main Panel')
tabs.pack(expand=1, fill='both')


def info_box():
    msg_box.showinfo('Information', 'I learn programming')

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=info_box)
menu_bar.add_cascade(label='Help', menu=help_menu)


display_frame = ttk.LabelFrame(tab_1, text='Display')
display_frame.grid(column=0, row=0, columnspan=4, sticky='WE')


display_text = tk.StringVar()
display = ttk.Entry(display_frame, textvariable=display_text)
display.grid(column=0, row=0, columnspan=4, sticky='WE')
display.focus()

data = display.get()
print(data)


def clear():
    pass
button_clear = ttk.Button(tab_1, text='C', command=clear, width=6)
button_clear.grid(column=0, row=1)


def result():
    pass
button_result = ttk.Button(tab_1, text='=', command=result, width=6)
button_result.grid(column=1, row=1)


def add():
    pass
button_add = ttk.Button(tab_1, text='+', command=add, width=6)
button_add.grid(column=2, row=1)


def subtract():
    pass
button_subtract = ttk.Button(tab_1, text='-', command=subtract, width=6)
button_subtract.grid(column=3, row=1)


def multiply():
    pass
button_multiply = ttk.Button(tab_1, text='*', command=multiply, width=6)
button_multiply.grid(column=3, row=2)


def divide():
    pass
button_divide = ttk.Button(tab_1, text='/', command=divide, width=6)
button_divide.grid(column=3, row=3)


def exp():
    pass
button_exp = ttk.Button(tab_1, text='exp', command=exp, width=6)
button_exp.grid(column=3, row=4)


def root():
    pass
button_root = ttk.Button(tab_1, text='root', command=root, width=6)
button_root.grid(column=3, row=5)


def comma():
    pass
button_comma = ttk.Button(tab_1, text=',', command=comma, width=6)
button_comma.grid(column=2, row=5)


def zero():
    pass
button_0 = ttk.Button(tab_1, text='0', command=zero, width=6)
button_0.grid(column=1, row=5)


def one():
    pass
button_1 = ttk.Button(tab_1, text='1', command=one, width=6)
button_1.grid(column=0, row=4)


def two():
    pass
button_2 = ttk.Button(tab_1, text='2', command=two, width=6)
button_2.grid(column=1, row=4)


def three():
    pass
button_3 = ttk.Button(tab_1, text='3', command=three, width=6)
button_3.grid(column=2, row=4)


def four():
    pass
button_4 = ttk.Button(tab_1, text='4', command=four, width=6)
button_4.grid(column=0, row=3)


def five():
    pass
button_5 = ttk.Button(tab_1, text='5', command=five, width=6)
button_5.grid(column=1, row=3)


def six():
    pass
button_6 = ttk.Button(tab_1, text='6', command=six, width=6)
button_6.grid(column=2, row=3)


def seven():
    pass
button_7 = ttk.Button(tab_1, text='7', command=seven, width=6)
button_7.grid(column=0, row=2)


def eight():
    pass
button_8 = ttk.Button(tab_1, text='8', command=eight, width=6)
button_8.grid(column=1, row=2)


def nine():
    pass
button_9 = ttk.Button(tab_1, text='9', command=nine, width=6)
button_9.grid(column=2, row=2)


for child in tab_1.winfo_children():
    child.grid_configure(padx=2, pady=2)

tab_2 = ttk.Frame(tabs)
tabs.add(tab_2, text='Settings')

div_prec_frame = ttk.LabelFrame(tab_2, text='Division Precision')
div_prec_frame.grid(column=0, row=0)
div_precision = tk.Spinbox(div_prec_frame, from_=0, to=16, width=4)
div_precision.grid(column=0, row=0)

main_window.mainloop()
