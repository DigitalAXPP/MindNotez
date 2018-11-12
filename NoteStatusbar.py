import tkinter as tk

class StatusBar:
    """Class creating the status bar"""
    def __init__(self, master):
        tnb_status_bar = tk.Label(master, text="This is the status bar.", bd=1, relief="sunken", anchor="w")
        tnb_status_bar.pack(side="bottom", fill="x")