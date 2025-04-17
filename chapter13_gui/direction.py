from tkinter import *
from tkinter import messagebox  #IMPORTANT

def goNorth():
    #messagebox.showinfo("Direction", "You are going north!")
    user_input = northentry.get() # returns string
    print(user_input)
    westlabel.config(text=user_input)

root = Tk()
root.geometry("500x300")

northentry = Entry(root)
northentry.pack(side = 'top')

northbutton = Button(root, text="north", fg="green", command=goNorth)
northbutton.pack(side = 'top')

westlabel = Label(root, text="west", fg="red",  borderwidth="2", relief="solid")
westlabel.pack(side = 'left')

eastlabel = Label(root, text="east", fg="yellow",  borderwidth="2", relief="solid")
eastlabel.pack(side = 'right')

southlabel = Label(root, text="south", fg="purple",  borderwidth="2", relief="solid")
southlabel.pack(side = 'bottom')

root.mainloop()