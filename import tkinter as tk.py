import tkinter as tk

# Function to perform the arithmetic operation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()
        if operator == "+":
            result.set(num1 + num2)
        elif operator == "-":
            result.set(num1 - num2)
        elif operator == "*":
            result.set(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields for input numbers
entry_num1 = tk.Entry(root)
entry_num1.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Dropdown menu to select the operator
operator_var = tk.StringVar()
operator_var.set("+")  # Default operator is addition
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.pack()

# Button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Label to display the result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the main event loop
root.mainloop()