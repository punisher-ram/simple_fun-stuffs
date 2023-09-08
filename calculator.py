import tkinter as tk

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to calculate and update the result as a float
def calculate_result():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to handle backspace
def backspace():
    current_text = display_var.get()
    if current_text != "0":
        updated_text = current_text[:-1]
        if not updated_text:
            updated_text = "0"
        display_var.set(updated_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a variable to store the display text
display_var = tk.StringVar()
display_var.set("0")

# Create the display
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, justify="right")
display.grid(row=0, column=0, columnspan=4)

# Define the buttons (without the "/" button)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', '<-'  # Removed the "/" button
]

# Function to handle button clicks
def button_click(value):
    if value == '=':
        calculate_result()
    elif value == 'C':
        clear_display()
    elif value == '<-':
        backspace()
    else:
        update_display(value)

# Create and place the buttons on the GUI
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
root.mainloop()
