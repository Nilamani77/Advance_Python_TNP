import tkinter as tk


def login():
    email = email_entry.get()
    password = password_entry.get()
    print("Email:", email)
    print("Password:", password)



root = tk.Tk()
root.title("Facebook Login")
root.geometry("400x500")
root.configure(bg="yellow")


title = tk.Label(root, text="Log in to Facebook", font=("Arial",16,"bold"), bg="red")
title.pack(pady=20)


email_entry = tk.Entry(root, width=35, font=("Arial",12))
email_entry.insert(0, "Email address or mobile number")
email_entry.pack(pady=10, ipady=8)


password_entry = tk.Entry(root, width=35, font=("Arial",12))
password_entry.insert(0, "Password")
password_entry.pack(pady=10, ipady=8)

login_btn = tk.Button(root, text="Log in", bg="#1877F2", fg="white",
                      font=("Arial",12,"bold"), width=25,command=login)
login_btn.pack(pady=20)


forgot = tk.Label(root, text="Forgotten password?",font=("Arial",12), fg="black", bg="white", cursor="hand2")
forgot.pack(pady=10)


create_btn = tk.Button(root, text="Create new account",
                       font=("Arial",12), width=25,fg="blue")
create_btn.pack(pady=20)


meta = tk.Label(root, text="Meta", font=("Arial",12), bg="white")
meta.pack(side="bottom", pady=20)

root.mainloop()