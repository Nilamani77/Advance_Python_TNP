import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do List")
root.geometry("350x450")
root.config(bg="#f0f0f0")


title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)


entry = tk.Entry(root, width=25, font=("Arial", 12),highlightbackground="#e2db0b",highlightthickness=2)
entry.pack(pady=10)


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END,"✓"+task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning","Please enter a task")

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Warning","Please select a valid task.")


frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", bg="#4CAF50", fg="black", width=10, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(frame, text="Delete Task", bg="#f44336", fg="black", width=10, command=delete_task)
delete_btn.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=35, height=12,  font=("Arial", 12),highlightbackground="#f44336",highlightthickness=2)
listbox.pack(pady=15)

root.mainloop()