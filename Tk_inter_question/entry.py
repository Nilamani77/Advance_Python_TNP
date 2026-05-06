import tkinter as tk

def say_hello():
    name = entry.get() 
    print("Hello", name)

root = tk.Tk()
root.title("Tk")
root.geometry("300x200")

label = tk.Label(root, text="Enter Your Name:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=25)
entry.pack(pady=5)

button = tk.Button(root, text="Submit", command=say_hello)
button.pack(pady=20)

root.mainloop()