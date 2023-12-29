import tkinter as tk
from tkinter import filedialog
import os
import shutil
from tkinter import simpledialog


class InfoInputApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Information input")
        self.title = None
        self.description = None
        self.link = None

        self.select_files()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Title (max 100 chars):").pack()
        self.title_entry = tk.Entry(self.root, width=100)
        self.title_entry.pack()

        tk.Label(self.root, text="Link (max 100 chars):").pack()
        self.link_entry = tk.Entry(self.root, width=100)
        self.link_entry.pack()

        tk.Label(self.root, text="Description (max 500 chars):").pack()
        self.description_text = tk.Text(self.root, width=100, height=5)
        self.description_text.pack()

        submit_button = tk.Button(
            self.root, text="Submit", command=self.submit_info)
        submit_button.pack()

    def submit_info(self):
        self.title = self.title_entry.get()
        self.link = self.link_entry.get()
        self.description = self.description_text.get("1.0", "end-1c")

        self.root.quit()  # Ferme la fenêtre

    def copy_files(self, files):
        temp_dir = 'temp'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        for file in files:
            shutil.copy(file, temp_dir)

        return len(files)

    def select_files(self):
        file_types = [('JPEG', '*.jpg'), ('JPEG', '*.jpeg')]
        files = filedialog.askopenfilenames(filetypes=file_types)
        if files:
            count = self.copy_files(files)
            print(f"{count} files copied to the temp directory.")

    def run(self):
        self.root.mainloop()
        return self.title, self.description, self.link
