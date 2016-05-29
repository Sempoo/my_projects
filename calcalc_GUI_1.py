import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg_box
import calcalc as engine


main_window = tk.Tk()
main_window.title('Calcalc')
main_window.configure(background='#4D4D4D')
main_window.resizable(False, False)


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


display_frame = ttk.LabelFrame(tab_1, text='24 Digit Display')
display_frame.grid(column=0, row=0, columnspan=4, sticky='we')


display_text = tk.StringVar()

display = ttk.Entry(display_frame, textvariable=display_text, width=24,
                    font='bold, 14', justify=tk.RIGHT)
display_text.set('')
display.grid(column=0, row=0, columnspan=4, sticky='e')

style = ttk.Style()
style.configure('red.TButton', foreground='red', font=18)
style.configure('blue.TButton', foreground='blue', font=18)
style.configure('black.TButton', foreground='black', font=18)

memory = ''
number_1 = ''
action = ''
number_2 = ''


def get_num1():
    global action, number_1
    if action is not None:
        number_1 = memory


def get_num2():
    global number_2
    cut = len(number_1)
    number_2 = memory[cut:]


def clear(backspace_sym):
    display_text.set('')
    print('BackSpace pressed')
    global memory, number_1, number_2, action
    memory = ''
    number_1 = ''
    action = ''
    number_2 = ''
button_clear = ttk.Button(tab_1, text='C', width=6, style='red.TButton')
button_clear.grid(column=0, row=1)
button_clear.bind('<Button-1>', clear)
tab_1.bind_all('<BackSpace>', clear)


def result(return_sym):
    print('Return pressed')
    global number_1, number_2, action
    get_num2()
    if action == engine.division:
        res = action(float(number_1), float(number_2), int(div_prec.get()))
    elif action == engine.root:
        res = action(float(number_1), float(number_2), int(root_iter.get()))
    else:
        res = action(float(number_1), float(number_2))

    if str(res)[-2:] == '.0':
        display_text.set(int(res))
    else:
        display_text.set(res)
button_result = ttk.Button(tab_1, text='=', width=6, style='blue.TButton')
button_result.grid(column=1, row=1)
button_result.bind('<Button-1>', result)
tab_1.bind_all('<Return>', result)


def add(plus_sym):
    print('+ pressed')
    global memory, number_1, action
    display_text.set(memory + ' + ')
    number_1 = memory
    action = engine.addition
    get_num1()
button_add = ttk.Button(tab_1, text='+', width=6, style='blue.TButton')
button_add.grid(column=2, row=1)
button_add.bind('<Button-1>', add)
tab_1.bind_all('+', add)


def subtract(minus_sym):
    print('- pressed')
    global memory, number_1, action
    if memory == '':
        display_text.set('-')
        memory = '-'
    else:
        display_text.set(memory + ' - ')
    number_1 = memory
    action = engine.subtraction
    get_num1()
button_subtract = ttk.Button(tab_1, text='-', width=6, style='blue.TButton')
button_subtract.grid(column=3, row=1)
button_subtract.bind('<Button-1>', subtract)
tab_1.bind_all('-', subtract)


def multiply(asterisk_sym):
    print('* pressed')
    global memory, number_1, action
    display_text.set(memory + ' * ')
    number_1 = memory
    action = engine.multiplication
    get_num1()
button_multiply = ttk.Button(tab_1, text='*', width=6, style='blue.TButton')
button_multiply.grid(column=3, row=2)
button_multiply.bind('<Button-1>', multiply)
tab_1.bind_all('*', multiply)


def divide(slash_sym):
    print('/ pressed')
    global memory, number_1, action
    display_text.set(memory + ' / ')
    number_1 = memory
    action = engine.division
    get_num1()
button_divide = ttk.Button(tab_1, text='/', width=6, style='blue.TButton')
button_divide.grid(column=3, row=3)
button_divide.bind('<Button-1>', divide)
tab_1.bind_all('/', divide)


def exp(e_sym):
    print('e pressed')
    global memory, number_1, action
    display_text.set(memory + ' exp ')
    number_1 = memory
    action = engine.int_exp
    get_num1()
button_exp = ttk.Button(tab_1, text='exp', width=6, style='blue.TButton')
button_exp.grid(column=3, row=4)
button_exp.bind('<Button-1>', exp)
tab_1.bind_all('e', exp)


def root(r_sym):
    print('r pressed')
    global memory, number_1, action
    display_text.set(memory + ' root ')
    number_1 = memory
    action = engine.root
    get_num1()
button_root = ttk.Button(tab_1, text='root', width=6, style='blue.TButton')
button_root.grid(column=3, row=5)
button_root.bind('<Button-1>', root)
tab_1.bind_all('r', root)


def dev(d_sym):
    print('\ndev info:\n---------')
    print('memory   =', memory)
    print('number_1 =', number_1)
    print('number_2 =', number_2)
    print('action   =', action)
    print('div_prec =', div_prec.get())
    print('root_iter =', root_iter.get())
    try:
        if action == engine.multiplication:
            print('multipl_ref =', float(number_1) * float(number_2))
        if action == engine.division:
            print('div_ref =', float(number_1) / float(number_2))
        if action == engine.int_exp:
            print('exp_ref =', float(number_1) ** float(number_2))
        if action == engine.root:
            print('root_ref =', float(number_1) ** (1/float(number_2)))
    except ValueError:
        print('press \'dev\' after pressing \'=\' to obtain ref_result')
button_comma = ttk.Button(tab_1, text='dev', width=6, style='red.TButton')
button_comma.grid(column=2, row=5)
button_comma.bind('<Button-1>', dev)
tab_1.bind_all('d', dev)


def comma(comma_sym):
    print(', pressed')
    display.insert('end', '.')
    global memory
    memory += '.'
button_comma = ttk.Button(tab_1, text=',', width=6, style='black.TButton')
button_comma.grid(column=1, row=5)
button_comma.bind('<Button-1>', comma)
tab_1.bind_all(',', comma)


def zero(zero_sym):
    print('0 pressed')
    display.insert('end', '0')
    global memory
    memory += '0'
button_0 = ttk.Button(tab_1, text='0', width=6, style='black.TButton')
button_0.grid(column=0, row=5)
button_0.bind('<Button-1>', zero)
tab_1.bind_all('0', zero)


def one(one_sym):
    print('1 pressed')
    display.insert('end', '1')
    global memory
    memory += '1'
button_1 = ttk.Button(tab_1, text='1', width=6, style='black.TButton')
button_1.grid(column=0, row=4)
button_1.bind('<Button-1>', one)
tab_1.bind_all('1', one)


def two(two_sym):
    print('2 pressed')
    display.insert('end', '2')
    global memory
    memory += '2'
button_2 = ttk.Button(tab_1, text='2', width=6, style='black.TButton')
button_2.grid(column=1, row=4)
button_2.bind('<Button-1>', two)
tab_1.bind_all('2', two)


def three(three_sym):
    print('3 pressed')
    display.insert('end', '3')
    global memory
    memory += '3'
button_3 = ttk.Button(tab_1, text='3', width=6, style='black.TButton')
button_3.grid(column=2, row=4)
button_3.bind('<Button-1>', three)
tab_1.bind_all('3', three)


def four(four_sym):
    print('4 pressed')
    display.insert('end', '4')
    global memory
    memory += '4'
button_4 = ttk.Button(tab_1, text='4', width=6, style='black.TButton')
button_4.grid(column=0, row=3)
button_4.bind('<Button-1>', four)
tab_1.bind_all('4', four)


def five(five_sym):
    print('5 pressed')
    display.insert('end', '5')
    global memory
    memory += '5'
button_5 = ttk.Button(tab_1, text='5', width=6, style='black.TButton')
button_5.grid(column=1, row=3)
button_5.bind('<Button-1>', five)
tab_1.bind_all('5', five)


def six(six_sym):
    print('6 pressed')
    display.insert('end', '6')
    global memory
    memory += '6'
button_6 = ttk.Button(tab_1, text='6', width=6, style='black.TButton')
button_6.grid(column=2, row=3)
button_6.bind('<Button-1>', six)
tab_1.bind_all('6', six)


def seven(seven_sym):
    print('7 pressed')
    display.insert('end', '7')
    global memory
    memory += '7'
button_7 = ttk.Button(tab_1, text='7', width=6, style='black.TButton')
button_7.grid(column=0, row=2)
button_7.bind('<Button-1>', seven)
tab_1.bind_all('7', seven)


def eight(eight_sym):
    print('8 pressed')
    display.insert('end', '8')
    global memory
    memory += '8'
button_8 = ttk.Button(tab_1, text='8', width=6, style='black.TButton')
button_8.grid(column=1, row=2)
button_8.bind('<Button-1>', eight)
tab_1.bind_all('8', eight)


def nine(nine_sym):
    print('9 pressed')
    display.insert('end', '9')
    global memory
    memory += '9'
button_9 = ttk.Button(tab_1, text='9', width=6, style='black.TButton')
button_9.grid(column=2, row=2)
button_9.bind('<Button-1>', nine)
tab_1.bind_all('9', nine)


for child in tab_1.winfo_children():
    child.grid_configure(padx=2, pady=2)


tab_2 = ttk.Frame(tabs)
tabs.add(tab_2, text='Settings')

div_prec_frame = ttk.LabelFrame(tab_2, text='Division Precision')
div_prec_frame.grid(column=0, row=0)
div_prec_frame.grid_configure(padx=7)
div_prec = tk.StringVar()
div_precision = tk.Spinbox(div_prec_frame, from_=0, to=16, width=4,
                           textvariable=div_prec)
div_precision.pack_configure(padx=5, pady=5)
div_prec.set(16)
div_precision.pack()


root_iter_frame = ttk.LabelFrame(tab_2, text='Root Iterations')
root_iter_frame.grid(column=1, row=0)
root_iter = tk.StringVar()
root_iterations = tk.Spinbox(root_iter_frame, from_=0, to=16, width=4,
                             textvariable=root_iter)
root_iterations.pack_configure(padx=5, pady=5)
root_iter.set(6)
root_iterations.pack()

main_window.mainloop()
