import tkinter as tk
from tkinter import filedialog, messagebox
from organizer import organize_files_by_type
from theme import toggle_theme

def browse_folder(folder_entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

def convert_files(folder_entry, summary_text):
    folder_path = folder_entry.get()
    if folder_path:
        organize_files_by_type(folder_path, summary_text)
    else:
        messagebox.showerror("Error", "Please select a folder first!")
#create GUI
def create_gui():
    dark_mode = True

    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("500x400")

    root.configure(bg="#2E2E2E")

    label = tk.Label(root, text="Organize files by type", font=("Arial", 14, "bold"), bg="#2E2E2E", fg="white")
    label.pack(pady=10)

    folder_frame = tk.Frame(root, bg="#2E2E2E")
    folder_frame.pack(pady=5)

    folder_entry = tk.Entry(folder_frame, width=40, bg="#555", fg="white", font=("Arial", 10))
    folder_entry.pack(side=tk.LEFT, padx=5)

    browse_button = tk.Button(folder_frame, text="Browse", command=lambda: browse_folder(folder_entry), bg="#555", fg="white", font=("Arial", 10))
    browse_button.pack(side=tk.LEFT)

    convert_button = tk.Button(root, text="Convert", command=lambda: convert_files(folder_entry, summary_text), bg="#555", fg="white", font=("Arial", 10))
    convert_button.pack(pady=10)

    # Summary Text
    summary_text = tk.Text(root, height=10, width=60, bg="#555", fg="white", font=("Arial", 10))
    summary_text.pack(pady=10)

    # Toggle Button
    toggle_button = tk.Button(root, text="Dark Theme ON", command=lambda: toggle_theme_wrapper(), bg="#555", fg="white", font=("Arial", 10))
    toggle_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#555", fg="white", font=("Arial", 10))
    exit_button.pack(pady=5)

    def toggle_theme_wrapper():
        nonlocal dark_mode
        dark_mode = toggle_theme(dark_mode, root, label, folder_entry, browse_button, convert_button, exit_button, toggle_button, summary_text)

    print("GUI created")

    root.mainloop()