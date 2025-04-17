import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Number Adder")

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
button = tk.Button(root, text="Add")
button.pack(pady=5)

# Display result
result_label = tk.Label(root)
result_label.pack(pady=5)

# Start the GUI
root.mainloop()
