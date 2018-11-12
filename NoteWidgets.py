import NoteFunction as NF
import os
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk
from tkinter import filedialog
matplotlib.use("TkAgg")


class FrontFrames(NF.Functions):
    """Class creating the application widgets"""
    def __init__(self, master):
        super()
        top_f = tk.Frame(master, bg="green")
        middle_f = tk.Frame(master)
        bottom_f = tk.Frame(master)
        top_f.pack(side="top", fill="both", expand=True)
        middle_f.pack(side="top", fill="both")
        bottom_f.pack(side="top", fill="both", expand=True)
        # ******Top_Entry******
        self.nodes = dict()
        self.tree = ttk.Treeview(top_f)
        ysb = ttk.Scrollbar(top_f, orient='vertical', command=self.tree.yview)
        xsb = ttk.Scrollbar(top_f, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)
        self.tree.heading('#0', text='Project tree', anchor='w')
        path = "/"
        abspath = os.path.abspath(path)
        self.insert_node('', abspath, abspath)
        self.tree.bind('<<TreeviewOpen>>', self.open_node)

        column = ("Title", "author", "year", "others")
        treeviewframe = tk.Frame(top_f)
        self.treeview = ttk.Treeview(treeviewframe, columns=column, show='headings')
        scroll = ttk.Scrollbar(treeviewframe, orient="vertical", command=self.treeview.yview)
        scroll.pack(side="right", fill="y")
        self.treeview.heading("Title", text="Title")
        self.treeview.heading("author", text="Author")
        self.treeview.heading("year", text="Year")
        self.treeview.heading("others", text="Others")
        self.treeview.bind("<<TreeviewSelect>>", self.select_table_content)
        self.treeview.configure(yscrollcommand=scroll.set)
        self.refresh()
        content = self.set_defaultfile()
        self.plotting()
        f = self.plotting()
        self.canvas = FigureCanvasTkAgg(f, top_f)

        # location where function-refresh was previously located
        # Location were plot function was previously located

        self.tree.pack(side="left", fill="both", expand=True)
        treeviewframe.pack(side="left", fill="both", expand=True)
        self.treeview.pack(side="left", fill="both", expand=True)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="right", fill="both")
        # ****Bottom_Entry*******
        title_label = tk.Label(bottom_f)
        title = tk.Label(title_label, text="Title", bd=1)
        self.title_entry = tk.Entry(title_label)
        author = tk.Label(title_label, text="Author", bd=2)
        self.author_entry = tk.Entry(title_label)
        year = tk.Label(title_label, text="Year", bd=3)
        self.year_entry = tk.Entry(title_label)
        others = tk.Label(title_label, text="Others...", bd=4)
        self.others_entry = tk.Entry(title_label)
        note = tk.Label(bottom_f, text="Notes")
        self.note_entry = tk.Text(bottom_f)
        self.save_button = tk.Button(middle_f, text="Save", command=self.save_button)
        self.refresh_button = tk.Button(middle_f, text="Refresh", command=self.refresh)
        # ****Bottom_Entry.pack()****
        self.save_button.pack(side="left")
        self.refresh_button.pack(side="left")
        title_label.pack(side="top", fill="x")
        title.pack(side="left", fill="x", expand=True)
        self.title_entry.pack(side="left", fill="x", expand=True)
        author.pack(side="left", fill="x", expand=True)
        self.author_entry.pack(side="left", fill="x", expand=True)
        year.pack(side="left", fill="x", expand=True)
        self.year_entry.pack(side="left", fill="x", expand=True)
        others.pack(side="left", fill="x", expand=True)
        self.others_entry.pack(side="left", fill="x", expand=True)
        note.pack(side="left", fill="y")
        self.note_entry.pack(side="top", fill="both", expand=True)