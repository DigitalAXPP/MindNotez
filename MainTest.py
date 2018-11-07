import AboutMe as AM
import InputSign as IS
import csv
import itertools
import os
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from tkinter import ttk
from tkinter import filedialog
from collections import Counter
matplotlib.use("TkAgg")


class Functions:

    def set_defaultfile(self):
        """Find the default file 'Note.csv' and read the content. If no file exists,
         a new file should be created according to standards."""

        # self.file = file
        file = ""
        if not file:
            file = os.getcwd() + "/Note.csv"
            print("File is read!")
        else:
            fopen = self.file_open()
            file = fopen
            print("Fopen is read!")

        df_content = {"title": [], "author": [], "year": [], "others": [], "note": []}
        df_headers = ['title', 'author', 'year', 'others', 'note']
        # df_content= ["title", "author", "year", "others", "note"]
        # df = pd.DataFrame(data=df_content)
        # df.to_csv(file + "Note.csv", sep=",", index=False)
        try:
            with open(file, "r") as test:
                f_reader = csv.DictReader(test, delimiter=',')
                f_correct = open(file)
                headers = f_reader.fieldnames
                print(headers)
                newline = os.linesep
                first_row = True
                # if headers != df_headers:
                #     print("Headers do not match!")
                #     for row in f_reader:
                #         if first_row:
                #             row = df_headers
                #             first_row = False
                #         f_correct.writerow(row + newline)

        except FileNotFoundError:
            with open(file, "a+") as f:
                f_writer = csv.DictWriter(f, fieldnames=df_content)
                f_writer.writeheader()
                f.close()

        file_content = file
        return file_content
            # else:
            #     file_content = file + "Note.csv"
            #     return file_content

    def content_collector(self):
        """Collects the inputs from the tkinter widgest in the bottom half of the app.
        It checks whether content has been added to the column 'others'. If not, an 'alarm'
        window appears."""

        try:
            dic = {"note": self.note_entry.get("1.0", "end-1c"),
                   "title": self.title_entry.get(),
                   "author": self.author_entry.get(),
                   "year": self.year_entry.get(),
                   "others": self.others_entry.get()}

            assert not dic["others"] == ""

        except AssertionError:
            IS.inputalarm()

        finally:
            return dic

    def save_button(self):
        """Function according to the widget-button. It takes the content of the widgets and saves it
        to the CSV-file. Finally, it refreshes the table and optimally also should update the piechart."""
        dic = self.content_collector()
        file_content = self.set_defaultfile()
        df_content = self.set_defaultfile()

        for key in dic.keys():
            title = dic["title"]
            author = dic["author"]
            year = dic["year"]
            other = dic["others"]
            note = dic["note"]
            row = title + "," + author + "," + year + "," + other + "," + note

        with open(file_content, "a", newline='') as f:
            #fwriter = csv.DictWriter(f, df_content)
            #fwriter.writerow(row)
            f.write(row + "\n")
            f.close()

        self.refresh()
        self.plotting()

    def file_saveas(self):
        """Takes widget contents, gets a filename and saves the text in the editor widget"""
        dic = self.content_collector()

        columntitles = "title, author, year, others, note\n"

        for key in dic.keys():
            title = dic["title"]
            author = dic["author"]
            year = dic["year"]
            other = dic["others"]
            note = dic["note"]
            row = title + "," + author + "," + year + "," + other + "," + note

        fout = filedialog.asksaveasfile(mode='w', defaultextension=".csv")

        fout.write(columntitles)
        fout.write(row)
        fout.close()

    def file_open(self):
        """In this order:
        opens editor widget, selects a file, clears table, inserts file content into table"""
        df_headers = self.set_defaultfile()
        headers = self.set_defaultfile()
        fopen = filedialog.askopenfilename(initialdir="C:/",
                                           title="Select file",
                                           filetypes=(("CSV file", "*.csv"), ("all files", "*.*")))

        # with open(fopen, 'r') as file:
        #     csv_reader = csv.DictReader(file, skipinitialspace=True)
        #     for row in csv_reader:
        #         self.title_entry.insert(0, f'{row["title"]}')
        #         self.author_entry.insert(0, f'{row["author"]}')
        #         self.year_entry.insert(0, f'{row["year"]}')
        #         self.others_entry.insert(0, f'{row["others"]}')
        #         self.note_entry.insert("1.0", f'{row["note"]}')

        self.clear_table()

        with open(fopen, 'r') as file:
            try:
                csv_reader = csv.DictReader(file, skipinitialspace=True)

                for row in csv_reader:
                    self.treeview.insert('', '0', values=(f'{row["title"]}',
                                                          f'{row["author"]}',
                                                          f'{row["year"]}',
                                                          f'{row["others"]}'))

            except KeyError:
                with open(fopen) as fin:
                    lines = fin.readlines()
                    lines[0] = lines[0].replace(headers, df_headers)

        # self.set_defaultfile(file=fopen)

    def open_node(self, event):
        """Opens a node in the path window (Top-Left)"""
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))

    def insert_node(self, parent, text, abspath):
        """Expands a node in the path window (Top-Left)"""
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def select_table_content(self, event):
        """Should enable a row selection from the table and inster the content into the widgets
        for editing"""

        lineselection = self.treeview.item(self.treeview.selection())
        #file_content = self.content_collector()
        file_content = self.set_defaultfile()

        print(type(lineselection))

        with open(file_content, 'r') as line:
            string = next(itertools.islice(csv.DictReader(line), lineselection-1, None))
            print(type(string))
            self.title_entry.insert(0, f'{string["values"][0]}')
            self.author_entry.insert(0, f'{string["values"][1]}')
            self.year_entry.insert(0, f'{string["values"][2]}')
            self.others_entry.insert(0, f'{string["values"][3]}')
            self.note_entry.insert("1.0", f'{string["values"][4]}')

    def clear_table(self):
        """Removes content from the table"""
        x = self.treeview.get_children()
        for child in x:
            self.treeview.delete(child)

    def refresh(self):
        """Updates/Refreshes the content in the table.
        1. Gets content from the file
        2. Gets the headers from the file
        3. Removes content from the table
        4. Reads content into the table"""
        file_content = self.set_defaultfile()
        df_headers = self.set_defaultfile()
        headers = self.set_defaultfile()
        self.clear_table()

        with open(file_content, 'r') as file:
            try:
                csv_reader = csv.DictReader(file, skipinitialspace=True)

                for row in csv_reader:
                    self.treeview.insert('', '0', values=(f'{row["title"]}',
                                                          f'{row["author"]}',
                                                          f'{row["year"]}',
                                                          f'{row["others"]}'))

            except KeyError:
                with open(file_content) as fin:
                    lines = fin.readlines()
                    lines[0] = lines[0].replace(headers, df_headers)

    def plotting(self):
        """Takes file content, selects the column 'others' and creates a pie chart"""
        file_content = self.set_defaultfile()
        with open(file_content, 'r') as chart:
            graph = csv.DictReader(chart, skipinitialspace=True)
            c = Counter(row["others"] for row in graph)

        header = list(c.keys())
        values = list(c.values())
        colors = ['r', 'g', 'b', 'c', 'y', 'm']
        f = plt.Figure(figsize=(4, 4))
        a = f.add_subplot(111)
        pie = a.pie(values, labels=header, colors=colors, startangle=90, autopct='%.1f%%')
        return f

        # self.canvas = FigureCanvasTkAgg(f, top_f)
        # self.canvas.draw()
        # self.canvas.get_tk_widget().pack(side="right", fill="both")

    def new_page(self):
        """PLANNED: To open a file and insert the content into the table"""
        self.file_open()
        self.refresh()


class FrontFrames(Functions):
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
        self.treeview = ttk.Treeview(top_f, columns=column, show='headings')
        self.treeview.heading("Title", text="Title")
        self.treeview.heading("author", text="Author")
        self.treeview.heading("year", text="Year")
        self.treeview.heading("others", text="Others")
        self.treeview.bind("<<TreeviewSelect>>", self.select_table_content)
        self.refresh()
        content = self.set_defaultfile()
        self.plotting()
        f = self.plotting()
        self.canvas = FigureCanvasTkAgg(f, top_f)

        # location where function-refresh was previously located
        # Location were plot function was previously located

        self.tree.pack(side="left", fill="both", expand=True)
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


class TopMenu(FrontFrames):
    """Class creating the top menu bar. Only few of the menu options are actually executing a command"""
    def __init__(self, master):
        super().__init__(master)
        # *******Top-Navigation Bar (tnb)**********
        tnb = tk.Menu(master)
        root.config(menu=tnb)

        # *******tnb_file*******

        tnb_file = tk.Menu(tnb, tearoff=0)
        tnb.add_cascade(label="File", menu=tnb_file)
        tnb_file.add_command(label="New Project")
        tnb_file.add_command(label="New ...")
        tnb_file.add_command(label="Open ...", command=self.file_open)
        tnb_file.add_command(label="Save", command=self.save_button)
        tnb_file.add_command(label="Save as ...", command=self.file_saveas)
        tnb_file.add_separator()
        tnb_file.add_command(label="Exit", command=root.destroy)

        # ********tnb_edit********

        tnb_edit = tk.Menu(tnb, tearoff=0)
        tnb.add_cascade(label="Edit", menu=tnb_edit)
        tnb_edit.add_command(label="Undo Typing")
        tnb_edit.add_separator()
        tnb_edit.add_command(label="Cut")
        tnb_edit.add_command(label="Copy")
        tnb_edit.add_command(label="Paste")
        tnb_edit.add_command(label="Delete")

        # *******tnb_view********

        tnb_view = tk.Menu(tnb, tearoff=0)
        tnb.add_cascade(label="View", menu=tnb_view)
        tnb_view.add_command(label="Recent files")
        tnb_view.add_command(label="Recently changed file")
        tnb_view.add_command(label="Recent Changes")
        tnb_view.add_separator()
        self.command = tnb_view.add_command(label="Toolbar")
        tnb_view.add_command(label="Tool Buttons")
        tnb_view.add_command(label="Status Bar")
        tnb_view.add_command(label="Navigation Bar")

        # *******tnb_help********

        tnb_help = tk.Menu(tnb, tearoff=0)
        tnb.add_cascade(label="help", menu=tnb_help)
        tnb_help.add_command(label="Find Action")
        tnb_help.add_command(label="help")
        tnb_help.add_command(label="Getting Started")
        tnb_help.add_separator()
        tnb_help.add_command(label="Report Problem ...")
        tnb_help.add_command(label="Submit Feedback ...")
        tnb_help.add_separator()
        tnb_help.add_command(label="Check for Updates ...")
        tnb_help.add_command(label="About", command=AM.AboutMeToplevel)


class StatusBar:
    """Class creating the status bar"""
    def __init__(self, master):
        tnb_status_bar = tk.Label(master, text="This is the status bar.", bd=1, relief="sunken", anchor="w")
        tnb_status_bar.pack(side="bottom", fill="x")


def window(main):
    main.title('MindnoteZ')
    main.update_idletasks()
    width = main.winfo_width()
    height = main.winfo_height()
    x = (main.winfo_screenwidth() // 2) - (width // 2)
    y = (main.winfo_screenheight() // 2) - (height // 2)
    main.geometry('{}x{}+{}+{}'.format(width, height, x, y))


root = tk.Tk()
window(root)

m = TopMenu(root)
SB = StatusBar(root)

tk.mainloop()
