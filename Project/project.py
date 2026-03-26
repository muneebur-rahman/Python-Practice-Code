# Real-Time Leaderboard System

# Project Statement:
# Design a leaderboard system using heaps and hashing to maintain real-time rankings.


import tkinter as tk
from tkinter import ttk, messagebox

# Store data
scores = {}

def add_score():
    name = name_entry.get()
    try:
        score = int(score_entry.get())

        if name in scores:
            scores[name] += score
        else:
            scores[name] = score

        update_table()

        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Enter valid score")

def update_table(data=None):
    # clear table
    for row in tree.get_children():
        tree.delete(row)

    # use given data or full data
    display_data = data if data else sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # insert into table
    for i, (name, score) in enumerate(display_data):
        tree.insert("", "end", values=(i+1, name, score))

def search_player():
    keyword = search_entry.get().lower()
    
    filtered = [(name, score) for name, score in scores.items() if keyword in name.lower()]
    
    # sort filtered data
    filtered = sorted(filtered, key=lambda x: x[1], reverse=True)
    
    update_table(filtered)

def reset_table():
    search_entry.delete(0, tk.END)
    update_table()

def clear_all():
    scores.clear()
    update_table()

# Window
root = tk.Tk()
root.title("Leaderboard with Search")
root.geometry("420x400")

# Input
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Score").pack()
score_entry = tk.Entry(root)
score_entry.pack()

tk.Button(root, text="Add Score", command=add_score).pack(pady=5)

# Search
tk.Label(root, text="Search Player").pack()
search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(root, text="Search", command=search_player).pack(pady=3)
tk.Button(root, text="Reset", command=reset_table).pack(pady=3)

tk.Button(root, text="Clear All", command=clear_all).pack(pady=5)

# Table
columns = ("Rank", "Name", "Score")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=10)

root.mainloop()