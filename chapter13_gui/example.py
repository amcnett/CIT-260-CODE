import tkinter as tk
from tkinter import PhotoImage

# Function to display selected options
def show_rules():

    selected_indices = listbox.curselection()  # Get selected index(es)
    if selected_indices:  # Ensure something is selected
        selected_rule = listbox.get(selected_indices[0])  # Get first selected item
    else:
        selected_rule = "No rule selected"
        
    selected_radio = radio_var.get()
    checkbox_selected = checkbox_var.get()
    scale_selected = scale.get()
    
    result = f"Selected Rule: {selected_rule}\n"
    result += f"Selected Option: {selected_radio}\n"
    result = f"Selected Slide: {scale_selected}\n"
    result += f"Checkbox Checked: {'Yes' if checkbox_selected else 'No'}"
    
    label_result.config(text=result)

# Initialize main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x400")

# need to load the image first
dog_image = PhotoImage(file="dog.png") # becareful as not all formats are supported

# label 
info_label = tk.Label(root, text="Example Widgets", font=28, image=dog_image)
info_label.pack()

# Radio Buttons
radio_var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio1.pack()
radio2.pack()

# Checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Accept Rules", variable=checkbox_var)
checkbox.pack()

listbox_frame = tk.Frame(root)
listbox_frame.pack(padx=20, pady=20)

# Listbox with rules
listbox = tk.Listbox(listbox_frame, height=2, width=30)
rules = ["Rule 1: Follow instructions", "Rule 2: Respect others", "Rule 3: Stay positive"]
for rule in rules:
    listbox.insert(tk.END, rule)
listbox.pack(side="left")

scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
scrollbar.pack(side='right', fill=tk.Y, expand=True)

scrollbar.config(command=listbox.yview)
scrollbar.config(width=15)
listbox.config(yscrollcommand=scrollbar.set)

# slider
scale = tk.Scale(root, from_=0, to=100, orient='horizontal') # note that "from" is a keyword, so we use "from_"
scale.pack()

# for longer text
message = tk.Message(root, text="This is a message for longer text. \n Even longer than a label.", width=200)
message.pack()

# Button to display selections
button = tk.Button(root, text="Show Rules", command=show_rules)
button.pack()

# Label for displaying results
label_result = tk.Label(root, text="")
label_result.pack()

# Run Tkinter event loop
root.mainloop()
