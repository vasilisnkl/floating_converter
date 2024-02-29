from customtkinter import *
from tkinter import ttk

excess_notation = {
    '111': 3,
    '110': 2,
    '101': 1,
    '100': 0,
    '011': -1,
    '010': -2,
    '001': -3,
    '000': -4
}

def convert_func():

    num = entry_box.get()
    try:
        sign = int(num[0])
        exponent = num[1:4]
        mantissa = float('0.' + num[4:])

        times = excess_notation[exponent]
        if times < 0:
            for i in range(abs(times)):
                mantissa /= 10
        else:
            for i in range(times):
                mantissa *= 10
        mantissa = "{:.8f}".format(mantissa)
        parts = str(mantissa).split('.')
        float_part = parts[1]

        i = 0
        p = 1/2
        dec = 0
        while i < len(float_part):
            dec += float(float_part[i]) * p
            p *= 1/2
            i += 1
    
        result = int(parts[0], 2) + dec
        if sign == 0:
            result_label.configure(text = str(result))
        else:
            result_label.configure(text = str(-result))
    except:
        result_label.configure(text = 'Wrong Input')


root = CTk()
root.title("Binary Converter")
root.geometry('700x500')
root.resizable(width=False, height=False)

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 20, 'bold')

max_chars = 8

def on_validate(P):
    if len(P) <= max_chars:
        return True
    else:
        return False

title_label = CTkLabel(root, font=font1, text="Binary 8-bit Floating Point Converter", text_color='#fff')
title_label.pack(padx=20, pady=20)


binary_input_label = CTkLabel(root, font=font2, text="Input Binary Float", text_color='#fff')
entry_box = CTkEntry(root, font=font1, width=150, height=60, validate='key', validatecommand=(root.register(on_validate), '%P'))
convert_button = CTkButton(root, command=convert_func, font=font1, text_color='#fff', text='Convert',
                            fg_color='#eb05ae', hover_color='#a8057d', cursor='hand2', corner_radius=10, width=200)

result_label = CTkLabel(root, text='', font=font1)

binary_input_label.pack(pady=20)
entry_box.pack(pady=20)
convert_button.pack(pady=20)
result_label.pack(pady=20)

root.mainloop()











    
