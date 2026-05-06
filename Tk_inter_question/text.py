import tkinter as tk

def submit_feedback():
    feedback = text_box.get("1.0", tk.END)
    print("Feedback:", feedback)

root = tk.Tk()
root.title("Feedback App")
root.geometry("400x300")

label = tk.Label(root, text="Write your feedback")
label.pack()

text_box = tk.Text(root, height=10, width=40)
text_box.pack(pady=10)

button = tk.Button(root, text="Submit Feedback", command=submit_feedback)
button.pack()

root.mainloop()