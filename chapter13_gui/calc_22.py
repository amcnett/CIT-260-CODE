import tkinter as tk

def addNums():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        total = num1 + num2
        #result_label.config(text=total, fg="black")
        result_var.set(total)
    except ValueError:
        #result_label.config(text="Incorrect Input", fg="red")
        result_var.set("Invalid Input")

# Create main window
root = tk.Tk() # really calling the init function
root.title("Number Adder")
root.geometry("300x200")

# Create entry fields for numbers
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5) # external vertical padding

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create a button to perform addition
button = tk.Button(root, text="Add", command=addNums)
button.pack(pady=5)

result_var = tk.StringVar()

# Display result
result_label = tk.Label(root, textvariable=result_var)
result_label.pack(pady=5)

# Start the GUI
root.mainloop()