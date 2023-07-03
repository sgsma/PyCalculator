import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def create_button(text, row, col, func=None):
    button = tk.Button(root, text=text, padx=10, pady=5, command=func)
    button.grid(row=row, column=col)

root = tk.Tk()
root.title("Calculadora")

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

create_button("C", 1, 0, clear)
create_button("7", 2, 0, lambda: button_click("7"))
create_button("8", 2, 1, lambda: button_click("8"))
create_button("9", 2, 2, lambda: button_click("9"))
create_button("/", 2, 3, lambda: button_click("/"))

create_button("4", 3, 0, lambda: button_click("4"))
create_button("5", 3, 1, lambda: button_click("5"))
create_button("6", 3, 2, lambda: button_click("6"))
create_button("*", 3, 3, lambda: button_click("*"))

create_button("1", 4, 0, lambda: button_click("1"))
create_button("2", 4, 1, lambda: button_click("2"))
create_button("3", 4, 2, lambda: button_click("3"))
create_button("-", 4, 3, lambda: button_click("-"))

create_button("0", 5, 0, lambda: button_click("0"))
create_button(".", 5, 1, lambda: button_click("."))
create_button("=", 5, 2, calculate)
create_button("+", 5, 3, lambda: button_click("+"))

root.mainloop()
