import tkinter as tk
from tkinter import messagebox

def getSize(): # callback function
    if pickupInt.get() == 1: 
        messagebox.showinfo("Order", "Selected: " + var_result.get() + " and order will be picked up.")
    else:
        messagebox.showinfo("Order", "Selected: " + var_result.get() + " and order will be delivered.")

# Create main window
root = tk.Tk()  #  calls the __init__/constructor of Tk to create a window
root.title("T-shirt size selector")
root.geometry("300x200")

# Create entry fields for numbers
label1 = tk.Label(root, text="Select your t-shirt size")
label1.pack(pady=5)

# StringVar addition
var_result = tk.StringVar()
var_result.set("Small")
# starts out empty to no set() is needed

#radiobutton group
radioS = tk.Radiobutton(root, text="Small", value="Small", variable=var_result)
radioM = tk.Radiobutton(root, text="Medium",  value="Medium", variable=var_result)
radioL= tk.Radiobutton(root, text="Large",  value="Large", variable=var_result)
radioX = tk.Radiobutton(root, text="X-Large",  value="X-Large", variable=var_result)

radioS.pack()
radioM.pack()
radioL.pack()
radioX.pack()

pickupInt = tk.IntVar()

pickupCheck = tk.Checkbutton(root, text="Will pick up order", variable=pickupInt)
pickupCheck.pack()

# Create a button to perform addition
button = tk.Button(root, text="Submit", command=getSize)
button.pack(pady=5)

# Start the GUI
root.mainloop()
