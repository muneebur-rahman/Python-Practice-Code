# Real-Time Leaderboard System

# Project Statement:
# Design a leaderboard system using heaps and hashing to maintain real-time rankings.


import tkinter as tk
from tkinter import ttk, messagebox

scores = {}

# -------- FUNCTIONS -------- #

def add_score(event=None):
    name = name_entry.get().strip()
    score_text = score_entry.get().strip()

    if not name or not score_text:
        messagebox.showwarning("Warning", "Please enter name and score")
        return

    if not score_text.isdigit():
        messagebox.showerror("Error", "Score must be a number")
        return

    score = int(score_text)

    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

    update_table()

    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)


def update_table(data=None):
    for row in tree.get_children():
        tree.delete(row)

    display_data = data if data else sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(display_data):
        tag = ""
        if i == 0:
            tag = "gold"
        elif i == 1:
            tag = "silver"
        elif i == 2:
            tag = "bronze"

        tree.insert("", "end", values=(i+1, name, score), tags=(tag,))

    status_label.config(text=f"Total Players: {len(display_data)}")


def search_player():
    keyword = search_entry.get().lower()

    filtered = [(n, s) for n, s in scores.items() if keyword in n.lower()]
    filtered.sort(key=lambda x: x[1], reverse=True)

    update_table(filtered)


def reset_table():
    search_entry.delete(0, tk.END)
    update_table()


def clear_all():
    if messagebox.askyesno("Confirm", "Clear all data?"):
        scores.clear()
        update_table()


def delete_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a player to delete")
        return

    for item in selected:
        name = tree.item(item)['values'][1]
        if name in scores:
            del scores[name]

    update_table()


# -------- UI -------- #

root = tk.Tk()
root.title("🏆 Leaderboard System")
root.geometry("500x500")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="Real-Time Leaderboard", font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

tk.Label(frame, text="Name", fg="white", bg="#1e1e2f").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Score", fg="white", bg="#1e1e2f").grid(row=1, column=0)
score_entry = tk.Entry(frame)
score_entry.grid(row=1, column=1, padx=5)

tk.Button(frame, text="Add Score", command=add_score, bg="#4CAF50", fg="white").grid(row=2, columnspan=2, pady=5)

# Enter key support
root.bind('<Return>', add_score)

# Search Frame
search_frame = tk.Frame(root, bg="#1e1e2f")
search_frame.pack(pady=5)

search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(search_frame, text="Search", command=search_player).grid(row=0, column=1)
tk.Button(search_frame, text="Reset", command=reset_table).grid(row=0, column=2)

# Table
columns = ("Rank", "Name", "Score")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

tree.pack(pady=10)

# Row colors
tree.tag_configure("gold", background="#FFD700")
tree.tag_configure("silver", background="#C0C0C0")
tree.tag_configure("bronze", background="#CD7F32")

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack()

tk.Button(btn_frame, text="Delete Selected", command=delete_selected, bg="red", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_all).grid(row=0, column=1, padx=5)

# Status Bar
status_label = tk.Label(root, text="Total Players: 0", bg="#1e1e2f", fg="white")
status_label.pack(pady=5)

root.mainloop()