import tkinter as tk

def addNums(): # callback function
    try:
        firstNum = float(entry1.get())
        secondNum = float(entry2.get())
        total = firstNum + secondNum
        # result_label.config(text=total, fg="black")
        var_result.set(total)
        result_label.config(fg="black")
    except ValueError:
        # result_label.config(text="Invalid Input", fg="red")
        var_result.set("Invalid input")
        result_label.config(fg="red")

# Create main window
root = tk.Tk()  #  calls the __init__/constructor of Tk to create a window
root.title("Number Adder")
root.geometry("200x250")

# Create entry fields for numbers
label1 = tk.Label(root, text="Enter first number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Create a button to perform addition
button = tk.Button(root, text="Add", command=addNums)
button.pack(pady=5)

# StringVar addition
var_result = tk.StringVar()
# starts out empty to no set() is needed

# Display result
result_label = tk.Label(root, textvariable=var_result)
result_label.pack(pady=5)

# Start the GUI
root.mainloop()
