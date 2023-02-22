from delete_files_in_subdirs import delete_files_in_subdirs
import tkinter as tk
from fetch_string import fetch_string
from prefix_rename import prefix_rename

# delete_files_in_subdirs()

# root = tk.Tk()
# string_var = fetch_string(root)
# root.mainloop()
# the_str = fetch_string()
# prefix_rename("testpre_")

TEAL = "#2596be"
PURPLE = "#6c25be"
GOLD = "#bea925"
IRON = "#D8D9DA"
BOULDER = "#7D7D7D"

if __name__ == "__main__":

    # creating an object of the Tk() class
    win_root = tk.Tk()
    # setting the title of the main window
    win_root.title("Demo")
    # set the size and position of the window
    win_root.geometry("300x600+650+250")
    # disabling the resizable option
    win_root.resizable(0, 0)
    # setting the background color to #D8E9E6
    win_root.configure(bg=PURPLE)

    # creating the frames using the Frame() widget
    header_frame = tk.Frame(win_root, bg=PURPLE, borderwidth=3, relief="solid")
    buttons_frame = tk.Frame(
        win_root, bg=PURPLE, borderwidth=3, relief="solid")

    # using the pack() method to place the frames in the window
    header_frame.pack(fill="both")
    buttons_frame.pack(expand=True, fill="both")

    # creating a label using the Label() widget
    header_label = tk.Label(
        header_frame,
        text="Script Demos",
        font=("arial bold", "36"),
        fg=IRON,
        bg=TEAL,
        borderwidth=6,
        relief="solid"
    )

    # using the pack() method to place the label in the window
    header_label.pack(expand=True, fill="both", pady=8,
                      padx=8, ipady=10)

    # Button that calls the delete_files_in_subdirs() function
    del_in_subdirs_button = tk.Button(
        buttons_frame,
        text="Delete All Files in Subdirs",
        font=("arial bold", "18"),
        bg=IRON,
        fg=TEAL,
        activeforeground=PURPLE,
        relief="groove",
        command=delete_files_in_subdirs
    )

    del_in_subdirs_button.pack(pady=10)

    def open_prefix_window():
        pre_win =
        prefix_button = tk.Button(
            buttons_frame,
            text="Delete All Files in Subdirs",
            font=("arial bold", "18"),
            bg=IRON,
            fg=TEAL,
            activeforeground=PURPLE,
            relief="groove",
            command=delete_files_in_subdirs
        )

    win_root.mainloop()
