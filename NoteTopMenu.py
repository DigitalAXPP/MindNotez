import AboutMe as AM
import NoteMainApp as Main
import NoteWidgets as NW
import tkinter as tk


class TopMenu(NW.FrontFrames):
    """Class creating the top menu bar. Only few of the menu options are actually executing a command"""
    def __init__(self, master):
        super().__init__(master)
        # *******Top-Navigation Bar (tnb)**********
        tnb = tk.Menu(master)
        Main.root.config(menu=tnb)

        # *******tnb_file*******

        tnb_file = tk.Menu(tnb, tearoff=0)
        tnb.add_cascade(label="File", menu=tnb_file)
        tnb_file.add_command(label="New Project")
        tnb_file.add_command(label="New ...")
        tnb_file.add_command(label="Open ...", command=self.file_open)
        tnb_file.add_command(label="Save", command=self.save_button)
        tnb_file.add_command(label="Save as ...", command=self.file_saveas)
        tnb_file.add_separator()
        tnb_file.add_command(label="Exit", command=Main.root.destroy)

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