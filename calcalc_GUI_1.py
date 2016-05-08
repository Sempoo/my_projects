import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg_box

main_window = tk.Tk()
main_window.title('Calcalc')
main_window.configure(background='#4D4D4D')
# main_window.geometry('600x600')


menu_bar = Menu(main_window)
main_window.config(menu=menu_bar)

tabs = ttk.Notebook(main_window)

tab_1 = ttk.Frame(tabs)
tabs.add(tab_1, text='Main Panel')
tabs.pack(expand=1, fill='both')


def info_box():
    msg_box.showinfo('Information', 'I learn programming :)')

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label='About', command=info_box)
menu_bar.add_cascade(label='Help', menu=help_menu)


display_frame = ttk.LabelFrame(tab_1, text='Display')
display_frame.grid(column=0, row=0, columnspan=4, sticky='WE')


display_text = tk.StringVar()
display = ttk.Entry(display_frame, textvariable=display_text)
display.grid(column=0, row=0, columnspan=4, sticky='WE')
x = display_text.get()
print(x)

s = ttk.Style()
s.configure('c.TButton', foreground='red')
s.configure('blue.TButton', foreground='blue')

def clear(backspace_sym):
    print('BackSpace pressed')
button_clear = ttk.Button(tab_1, text='C', width=6, style='c.TButton')
button_clear.grid(column=0, row=1)
button_clear.bind('<Button-1>', clear)



def result(return_sym):
    print('Return pressed')
button_result = ttk.Button(tab_1, text='=', width=6, style='blue.TButton')
button_result.grid(column=1, row=1)
button_result.bind('<Button-1>', result)


def add(plus_sym):
    print('+ pressed')
button_add = ttk.Button(tab_1, text='+', width=6, style='blue.TButton')
button_add.grid(column=2, row=1)
button_add.bind('<Button-1>', add)


def subtract(minus_sym):
    print('- pressed')
button_subtract = ttk.Button(tab_1, text='-', width=6, style='blue.TButton')
button_subtract.grid(column=3, row=1)
button_subtract.bind('<Button-1>', subtract)


def multiply(asterisk_sym):
    print('* pressed')
button_multiply = ttk.Button(tab_1, text='*', width=6, style='blue.TButton')
button_multiply.grid(column=3, row=2)
button_multiply.bind('<Button-1>', multiply)


def divide(slash_sym):
    print('/ pressed')
button_divide = ttk.Button(tab_1, text='/', width=6, style='blue.TButton')
button_divide.grid(column=3, row=3)
button_divide.bind('<Button-1>', divide)


def exp(e_sym):
    print('e pressed')
button_exp = ttk.Button(tab_1, text='exp', width=6, style='blue.TButton')
button_exp.grid(column=3, row=4)
button_exp.bind('<Button-1>', exp)


def root(r_sym):
    print('r pressed')
button_root = ttk.Button(tab_1, text='root', width=6, style='blue.TButton')
button_root.grid(column=3, row=5)
button_root.bind('<Button-1>', root)


def comma(comma_sym):
    print(', pressed')
button_comma = ttk.Button(tab_1, text=',', width=6)
button_comma.grid(column=2, row=5)
button_comma.bind('<Button-1>', comma)


def zero(zero_sym):
    print('0 pressed')
button_0 = ttk.Button(tab_1, text='0', width=6)
button_0.grid(column=1, row=5)
button_0.bind('<Button-1>', zero)


def one(one_sym):
    print('czemu to sie wyswietla?!')
button_1 = ttk.Button(tab_1, text='1', width=6)
button_1.grid(column=0, row=4)
button_1.bind('<Button-1>', one)


def two(two_sym):
    print('2 pressed')
button_2 = ttk.Button(tab_1, text='2', width=6)
button_2.grid(column=1, row=4)
button_2.bind('<Button-1>', two)


def three(three_sym):
    print('3 pressed')
button_3 = ttk.Button(tab_1, text='3', width=6)
button_3.grid(column=2, row=4)
button_3.bind('<Button-1>', three)


def four(four_sym):
    print('4 pressed')
button_4 = ttk.Button(tab_1, text='4', width=6)
button_4.grid(column=0, row=3)
button_4.bind('<Button-1>', four)


def five(five_sym):
    print('5 pressed')
button_5 = ttk.Button(tab_1, text='5', width=6)
button_5.grid(column=1, row=3)
button_5.bind('<Button-1>', five)


def six(six_sym):
    print('6 pressed')
button_6 = ttk.Button(tab_1, text='6', width=6)
button_6.grid(column=2, row=3)
button_6.bind('<Button-1>', six)


def seven(seven_sym):
    print('7 pressed')
button_7 = ttk.Button(tab_1, text='7', width=6)
button_7.grid(column=0, row=2)
button_7.bind('<Button-1>', seven)


def eight(eight_sym):
    print('8 pressed')
button_8 = ttk.Button(tab_1, text='8', width=6)
button_8.grid(column=1, row=2)
button_8.bind('<Button-1>', eight)


def nine(nine_sym):
    print('9 pressed')
button_9 = ttk.Button(tab_1, text='9', width=6)
button_9.grid(column=2, row=2)
button_9.bind('<Button-1>', nine)


# left_mouse_button = ['<Button-1>']
# keysym = ['<BackSpace>',
#           '<Return>',
#           '<plus>',
#           '<minus>',
#           '<asterisk>',
#           '<slash>',
#           '<e>',
#           '<r>',
#           '<comma>',
#           '<0>',
#           '<1>',
#           '<2>',
#           '<3>',
#           '<4>',
#           '<5>',
#           '<6>',
#           '<7>',
#           '<8>',
#           '<9>'
#           ]
# functions = [clear,
#              result,
#              add,
#              subtract,
#              multiply,
#              divide,
#              exp,
#              root,
#              comma,
#              zero,
#              one,
#              two,
#              three,
#              four,
#              five,
#              six,
#              seven,
#              eight,
#              nine
#              ]
#
# for button_func in zip(keysym, functions):
#     tab_1.bind_all(button_func)
#     # print(button_func)
#
# for mouse_func in zip(left_mouse_button, functions):
#     tab_1.bind_all(mouse_func)
#     # print(mouse_func)

for child in tab_1.winfo_children():
    child.grid_configure(padx=2, pady=2)

# print(zero)
tab_1.bind_all('<BackSpace>', clear)
tab_1.bind_all('<Return>', result)
tab_1.bind_all('<plus>', add)
tab_1.bind_all('<minus>', subtract)
tab_1.bind_all('<asterisk>', multiply)
tab_1.bind_all('<slash>', divide)
tab_1.bind_all('<e>', exp)
tab_1.bind_all('<r>', root)
tab_1.bind_all('<comma>', comma)
tab_1.bind_all('<0>', zero)
tab_1.bind_all('<1>', one)
tab_1.bind_all('<2>', two)
tab_1.bind_all('<3>', three)
tab_1.bind_all('<4>', four)
tab_1.bind_all('<5>', five)
tab_1.bind_all('<6>', six)
tab_1.bind_all('<7>', seven)
tab_1.bind_all('<8>', eight)
tab_1.bind_all('<9>', nine)


tab_2 = ttk.Frame(tabs)
tabs.add(tab_2, text='Settings')

div_prec_frame = ttk.LabelFrame(tab_2, text='Division Precision')
div_prec_frame.grid(column=0, row=0)
div_precision = tk.Spinbox(div_prec_frame, from_=0, to=16, width=4)
div_precision.grid(column=0, row=0)

main_window.mainloop()
