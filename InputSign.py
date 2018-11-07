import tkinter as tk


def inputalarm():
    """Creates a new window containing a label"""
    window = tk.Toplevel()
    window.title("Warning")

    central = tk.Label(window,
                       text="Please enter content in the text boxes. The more information you provide to your "
                            "comments the better later indexing will be.",
                       wraplength=200)
    central.pack()