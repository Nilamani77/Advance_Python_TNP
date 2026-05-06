import tkinter as tk

root = tk.Tk()
root.title("My First GUI App")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Python GUI Programming", font=("Arial", 14))
label.pack(pady=100)

root.mainloop()