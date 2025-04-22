import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Place Example")
root.geometry("400x300")  # Set window size
# Label to display messages
label = tk.Label(root, text="Click a button", font=("Arial", 14))
label.place(x=120, y=20)

# Create buttons positioned with place()
button1 = tk.Button(root, text="Button 1")
button1.place(x=50, y=80)

button2 = tk.Button(root, text="Button 2")
button2.place(x=250, y=80)

button3 = tk.Button(root, text="Button 3")
button3.place(x=50, y=150)

button4 = tk.Button(root, text="Button 4")
button4.place(x=250, y=150)

# Run the Tkinter event loop
root.mainloop()
