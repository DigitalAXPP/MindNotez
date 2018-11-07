import tkinter as tk


def AboutMeToplevel():
    """Creates a new window containing a label."""
    top = tk.Toplevel()
    top.title("General 1.1")

    central = tk.Label(top, text="This is general information about the application.")
    central.pack()
