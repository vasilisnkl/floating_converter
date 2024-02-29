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


def decimalToBinary(num, k_prec) : 
  
    binary = ""  
  
    Integral = int(num)    
    fractional = num - Integral 
    
    while (Integral) : 
          
        rem = Integral % 2  
        binary += str(rem);  
  
        Integral //= 2
       
    binary = binary[ : : -1]    
    binary += '.'
    
    while (k_prec) : 
            
        fractional *= 2
        fract_bit = int(fractional)  
  
        if (fract_bit == 1) : 
              
            fractional -= fract_bit  
            binary += '1'
              
        else : 
            binary += '0'
  
        k_prec -= 1
  
    return binary

def reverse_convert_func():

    num = float(decimal_entry.get())

    binary_float = float(decimalToBinary(num, 4))
    exponent = 0
    while binary_float > 1:
        binary_float /= 10
        exponent += 1

    binary_exponent = str()
    for exp in excess_notation.keys():
        if excess_notation[exp] == exponent:
            binary_exponent = exp
    
    ls = str(binary_float).split('.')
    mantissa = ls[1]

    if num >= 0:
        sign = '0'
    else:
        sign = '1'
    
    result = sign + binary_exponent + mantissa
    while len(result) < 8:
        result += '0'

    result = result[:8]
    binary_label.configure(text = result)

def convert_menu(event):
    option = convert_option.get()

    if option == 'Binary to Decimal':
        binary_input_label.pack()
        entry_box.pack(pady=20)
        convert_button.pack(pady=20)
        result_label.pack(pady=20)

        decimal_input_label.pack_forget()
        decimal_entry.pack_forget()
        convert_to_binary_button.pack_forget()
        binary_label.pack_forget()


    elif option == 'Decimal to Binary':

        decimal_input_label.pack()
        decimal_entry.pack(pady = 20)
        convert_to_binary_button.pack(pady=20)
        binary_label.pack(pady = 20)

        binary_input_label.pack_forget()
        entry_box.pack_forget()
        convert_button.pack_forget()
        result_label.pack_forget()


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

convert_options = ["Binary to Decimal", "Decimal to Binary"]
convert_option = ttk.Combobox(root, values=convert_options, font=font2, state="readonly", width=25)
convert_option.current(0) 
convert_option.bind("<<ComboboxSelected>>", convert_menu)
convert_option.pack(pady = 20)


binary_input_label = CTkLabel(root, font=font2, text="Input Binary Float", text_color='#fff')
entry_box = CTkEntry(root, font=font1, width=150, height=60, validate='key', validatecommand=(root.register(on_validate), '%P'))
convert_button = CTkButton(root, command=convert_func, font=font1, text_color='#fff', text='Convert',
                            fg_color='#eb05ae', hover_color='#a8057d', cursor='hand2', corner_radius=10, width=200)

result_label = CTkLabel(root, text='', font=font1)

decimal_input_label = CTkLabel(root, font=font2, text="Input Decimal Float", text_color='#fff')
decimal_entry = CTkEntry(root, font=font1, width=150, height=60, validate='key', validatecommand=(root.register(on_validate), '%P'))
convert_to_binary_button = CTkButton(root, command=reverse_convert_func, font=font1, text_color='#fff', text='Convert',
                                     fg_color='#eb05ae', hover_color='#a8057d', cursor='hand2', corner_radius=10, width=200)
binary_label = CTkLabel(root, text='', font=font1)

binary_input_label.pack()
entry_box.pack(pady=20)
convert_button.pack(pady=20)
result_label.pack(pady=20)

decimal_input_label.pack_forget()
decimal_entry.pack_forget()
convert_to_binary_button.pack_forget()
binary_label.pack_forget()

root.mainloop()











    
