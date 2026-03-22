import os
import tkinter as tk
from tkinter import filedialog, messagebox
import datetime

def write_log(message):
    with open("rename_log.txt", "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{timestamp} - {message}\n")

def choose_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def rename_files():
    folder = folder_path.get()
    base_name = name_entry.get().strip()

    if not folder:
        messagebox.showerror("Error", "Choose a folder first.")
        return

    if not base_name:
        messagebox.showerror("Error", "Enter a new base name.")
        return

    if not os.path.exists(folder):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return

    files = os.listdir(folder)
    count = 1
    renamed = 0

    for filename in files:
        old_path = os.path.join(folder, filename)

        if os.path.isfile(old_path):
            file_ext = os.path.splitext(filename)[1]
            new_name = f"{base_name}_{count}{file_ext}"
            new_path = os.path.join(folder, new_name)

            try:
                os.rename(old_path, new_path)
                write_log(f"{filename} -> {new_name}")
                count += 1
                renamed += 1
            except Exception as e:
                write_log(f"Error renaming {filename}: {e}")

    messagebox.showinfo("Done", f"Renamed {renamed} files.\nLog saved to rename_log.txt")

def count_files():
    folder = folder_path.get()

    if not folder:
        messagebox.showerror("Error", "Choose a folder first.")
        return

    if not os.path.exists(folder):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    messagebox.showinfo("Files found", f"Found {len(files)} files in the selected folder.")

root = tk.Tk()
root.title("File Renamer App PRO")
root.geometry("450x300")

folder_path = tk.StringVar()

title_label = tk.Label(root, text="File Renamer App PRO", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

folder_label = tk.Label(root, text="Choose folder")
folder_label.pack()

folder_entry = tk.Entry(root, textvariable=folder_path, width=48)
folder_entry.pack(pady=5)

choose_button = tk.Button(root, text="Choose folder", command=choose_folder)
choose_button.pack(pady=5)

count_button = tk.Button(root, text="Count files", command=count_files)
count_button.pack(pady=5)

name_label = tk.Label(root, text="New base name")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

rename_button = tk.Button(root, text="Rename files", command=rename_files)
rename_button.pack(pady=15)

root.mainloop()