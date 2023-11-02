import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Python GUI")

# Function to display a message when the button is clicked
def display_message():
    label.config(text="Hello, World!")

# Create a button
button = tk.Button(root, text="Click Me!", command=display_message)
button.pack()

# Create a label to display the message
label = tk.Label(root, text="")
label.pack()

# Start the main event loop
root.mainloop()