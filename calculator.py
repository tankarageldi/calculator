import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")

# Entry widget to display the input and result
display = tk.Entry(root, font=('Helvetica', 20), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)
display.insert(0, "0")

# Define a maximum length for the display
MAX_DISPLAY_LENGTH = 15

def click(value):
    current_text = display.get()
    if current_text == "0":
        display.delete(0, tk.END)
        current_text = ""
    if len(current_text) + len(str(value)) <= MAX_DISPLAY_LENGTH:
        display.delete(0, tk.END)
        display.insert(0, current_text + str(value))
    else:
        display.delete(0, tk.END)
        display.insert(0, current_text + str(value))

# Define button clear event handler
def clear_display():
    display.delete(0, tk.END)
    display.insert(0, "0")

# Define button equal event handler with error handling for large numbers
def calculate():
    try:
        result = eval(display.get())
        result_str = str(result)
        if len(result_str) > MAX_DISPLAY_LENGTH:
            raise OverflowError("Result too large")
        display.delete(0, tk.END)
        display.insert(0, result_str)
    except OverflowError as oe:
        display.delete(0, tk.END)
        display.insert(0, "Error: Large Num")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Create buttons
buttons = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '.', '=', '/'
]


row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(root, text=button, width=5, height=3, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=3, command=lambda b=button: click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text="C", width=10, height=3, command=clear_display).grid(row=row_val, column=0, columnspan=4)

#start the main loop
root.mainloop()
