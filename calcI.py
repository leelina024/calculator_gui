import tkinter as tk

calculation = ""

def add_to_caclculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_caculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


#create gui shape
root = tk.Tk()
root.title("Python GUI Calculator")
root.geometry("300x275")
root.config(bg = 'Pink')

text_result = tk.Text(root, height=2, width=16, font=('Roboto', 24))
text_result.grid(columnspan=5)

#create button geometry
btn_1 = tk.Button(root, text="1", command=lambda: add_to_caclculation(1), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_1.grid(row = 2, column = 1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_caclculation(2), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_2.grid(row = 2, column = 2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_caclculation(3), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_3.grid(row = 2, column = 3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_caclculation(4), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_4.grid(row = 3, column = 1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_caclculation(5), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_5.grid(row = 3, column = 2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_caclculation(6), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_6.grid(row = 3, column = 3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_caclculation(7), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_7.grid(row = 4, column = 1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_caclculation(8), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_8.grid(row = 4, column = 2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_caclculation(9), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_9.grid(row = 4, column = 3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_caclculation(0), width = 5, font = ("Roboto", 14), bg='LightBlue')
btn_0.grid(row = 5, column = 2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_caclculation("+"), width = 5, font = ("Roboto", 14), bg='Orange')
btn_plus.grid(row = 2, column = 4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_caclculation("-"), width = 5, font = ("Roboto", 14), bg='Orange')
btn_minus.grid(row = 3, column = 4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_caclculation("*"), width = 5, font = ("Roboto", 14), bg='Orange')
btn_mult.grid(row = 4, column = 4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_caclculation("/"), width = 5, font = ("Roboto", 14), bg='Orange')
btn_div.grid(row = 5, column = 4)

btn_openpar = tk.Button(root, text="(", command=lambda: add_to_caclculation("("), width = 5, font = ("Roboto", 14), bg='Orange')
btn_openpar.grid(row = 5, column = 1)

btn__closepar = tk.Button(root, text=")", command=lambda: add_to_caclculation(")"), width = 5, font = ("Roboto", 14), bg='Orange')
btn__closepar.grid(row = 5, column = 3)

btn_equal = tk.Button(root, text="=", command=evaluate_caculation, width = 12, font = ("Roboto", 14), bg='LightGreen')
btn_equal.grid(row = 6, column = 3, columnspan=2)

btn_clear = tk.Button(root, text="CLEAR", command=clear_field, width = 12, font = ("Roboto", 14), bg = 'Lightgray')
btn_clear.grid(row = 6, column = 1, columnspan=2)

root.mainloop()