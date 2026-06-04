import tkinter as tk
import matplotlib.pyplot as plt

def show_graph():
    text = entry.get().lower()

    count = {}

    for letter in text:
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

    plt.bar(count.keys(), count.values())
    plt.title("Letter Frequency Counter")
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    plt.show()

root = tk.Tk()
root.title("Letter Frequency Counter")
root.geometry("1200x200")

tk.Label(root, text="Enter Any Text").pack(pady=10)

entry = tk.Entry(root, width=150)
entry.pack()

tk.Button(root, text="Show Graph", command=show_graph).pack(pady=10)

root.mainloop()