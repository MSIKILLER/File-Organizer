import os
import shutil
import tkinter as tk
from tkinter import messagebox

def organize_files_by_type(folder_path, summary_text):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Audio': ['.mp3', '.wav'],
        'Videos': ['.mp4', '.avi'],
        'Archives': ['.zip', '.rar']
    }

    summary_text.delete(1.0, tk.END)
    for folder_name, extensions in file_types.items():
        folder_dir = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

        for file_name in os.listdir(folder_path):
            if any(file_name.endswith(ext) for ext in extensions):
                shutil.move(os.path.join(folder_path, file_name), folder_dir)
                summary_text.insert(tk.END, f"Moved {file_name} to {folder_name}\n")

    summary_text.insert(tk.END, "Organizing complete!")
