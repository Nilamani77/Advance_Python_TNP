import tkinter as tk

root = tk.Tk()
root.geometry("280x380")
root.title("Calculator")
root.config(bg="black")


def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))


def add():
    global first_number
    global operation

    first_number = int(entry.get())
    operation = "add"
    entry.delete(0, tk.END)

def subtract():
    global first_number
    global operation

    first_number = int(entry.get())
    operation = "sub"
    entry.delete(0, tk.END)

def multiply():
    global first_number
    global operation

    first_number=int(entry.get())
    operation="mul"
    entry.delete(0,tk.END)

def division():
    global first_number
    global operation

    first_number=int(entry.get())
    operation="div"
    entry.delete(0,tk.END)

def equal():
    second_number = int(entry.get())
    entry.delete(0, tk.END)

    if operation == "add":
        entry.insert(0, first_number + second_number)

    elif operation == "sub":
        entry.insert(0, first_number - second_number)
    
    elif operation == "mul":
        entry.insert(0,first_number * second_number)
    
    else:
        entry.insert(0,first_number / second_number)

def clear():
    entry.delete(0,tk.END)


entry = tk.Entry(root, text="0",width=16, font=("Arial", 20),
                 borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Row 1
btn1 = tk.Button(root, text="7", width=5,bg="yellow",fg="black", height=2, command=lambda: click(7))
btn1.grid(row=1, column=0)

btn2 = tk.Button(root, text="8", width=5,bg="yellow",fg="black", height=2, command=lambda: click(8))
btn2.grid(row=1, column=1)

btn3 = tk.Button(root, text="9", width=5,bg="yellow",fg="black", height=2, command=lambda: click(9))
btn3.grid(row=1, column=2)

addbtn = tk.Button(root, text="+", width=5, bg="green",fg="white",height=2, command=add)
addbtn.grid(row=1, column=3)

# Row 2
btn4 = tk.Button(root, text="4", width=5,bg="yellow",fg="black", height=2, command=lambda: click(4))
btn4.grid(row=2, column=0)

btn5 = tk.Button(root, text="5", width=5,bg="yellow",fg="black", height=2, command=lambda: click(5))
btn5.grid(row=2, column=1)

btn6 = tk.Button(root, text="6", width=5,bg="yellow",fg="black", height=2, command=lambda: click(6))
btn6.grid(row=2, column=2)

subbtn = tk.Button(root, text="-", width=5,bg="green",fg="white", height=2,
                   command=subtract)
subbtn.grid(row=2, column=3)

# Row 3
btn7 = tk.Button(root, text="1", width=5,bg="yellow", height=2,fg="black", command=lambda: click(1))
btn7.grid(row=3, column=0)

btn8 = tk.Button(root, text="2", width=5,bg="yellow", height=2,fg="black", command=lambda: click(2))
btn8.grid(row=3, column=1)

btn9 = tk.Button(root, text="3", width=5,bg="yellow", height=2,fg="black", command=lambda: click(3))
btn9.grid(row=3, column=2)

mulbtn = tk.Button(root, text="*", width=5,bg="green", height=2,fg="white",
                   command=multiply)
mulbtn.grid(row=3, column=3)

# Row 4

acbtn=tk.Button(root,text="AC",width=5,bg="green",height=2,fg="black",command=clear)
acbtn.grid(row=4,column=0)

btn10 = tk.Button(root, text="0", width=5, height=2,bg="yellow" ,fg="black",command=lambda: click(0))
btn10.grid(row=4, column=1)

equalbtn = tk.Button(root, text="=", width=5,bg="green", height=2,fg="white", command=equal)
equalbtn.grid(row=4, column=2)

divbtn = tk.Button(root, text="/", width=5, bg="green",height=2,fg="white",
                   command=division)
divbtn.grid(row=4, column=3)



root.mainloop()
