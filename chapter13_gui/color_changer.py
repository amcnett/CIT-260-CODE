import tkinter as tk
#from tkinter import colorchooser

def change_color():
    color = entry.get()
    # Attempt to set the button color based on user input
    try:
        button.config(bg=color)
    except tk.TclError:
        label.config(text="Invalid color name: "+color, fg="red")

# Create the main window
window = tk.Tk()
window.title("Change Button Color")
window.geometry("300x200")

# Add an entry widget
entry = tk.Entry(window, width=20)
entry.pack(pady=10)

# Add a button that changes color
button = tk.Button(window, text="Click Me!", width=15)
button.pack(pady=10)

# Add a label to display status messages
label = tk.Label(window, text="")
label.pack(pady=10)

# Add another button to trigger color change
change_button = tk.Button(window, text="Change Color", command=change_color)
change_button.pack(pady=10)

# Run the main loop
window.mainloop()
