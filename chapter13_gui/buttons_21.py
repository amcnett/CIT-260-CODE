import tkinter as tk

root = tk.Tk()
root.geometry("200x350")

b1 = tk.Button(root, text="Button 1")
b2 = tk.Button(root, text="Button 2")
b3 = tk.Button(root, text="Button 3")
b4 = tk.Button(root, text="Button 4", width=10, height=10)
b5 = tk.Button(root, text="Button 5")
b6 = tk.Button(root, text="Button 6")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
b4.grid(row=2, column=0, rowspan=2, sticky=tk.NS)
b5.grid(row=2, column=1)
b6.grid(row=4, column=0)

root.mainloop()