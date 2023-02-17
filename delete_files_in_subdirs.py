import os
import tkinter as tk
from tkinter import filedialog

def delete_files_in_subdirs():
    # Create a tkinter window and hide it
    root = tk.Tk()
    root.withdraw()

    # Use filedialog.askdirectory() to display a folder selection dialog and get the selected folder
    root_dir = filedialog.askdirectory()

    # Loop through all subdirectories and files in the root directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Loop through all files in the current directory
        for filename in filenames:
            # Create the full file path by joining the directory path and file name
            file_path = os.path.join(dirpath, filename)
            # Use os.remove to delete the file at the full file path
            os.remove(file_path)

# Call the function to run the script
# delete_files_in_subdirs()
