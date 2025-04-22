import tkinter as tk

root = tk.Tk()
root.geometry("600x460")

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white", font=32)
#rectangle_1.pack(ipadx=100, ipady=100, fill="both")
#rectangle_1.place(x=100, y=200)
rectangle_1.grid(row=0, column=0, padx=10, pady=10)

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white", font=32)
#rectangle_2.pack(padx=100, pady=100, ipadx=10, ipady=10)
#rectangle_2.place(relx=0.5, rely=0.5)
rectangle_2.grid(row=0, column=1,  padx=20, pady=20)

rectangle_3 = tk.Label(root, text="Rectangle 3", bg="purple", fg="white", font=32)
rectangle_3.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, padx=20, pady=20)
rectangle_4 = tk.Label(root, text="Rectangle 4", bg="orange", fg="white", font=32)
rectangle_4.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

root.mainloop()