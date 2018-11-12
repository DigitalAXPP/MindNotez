import NoteStatusbar as SB
import NoteTopMenu as TM
import NoteWidgets as NW
import tkinter as tk


class MainApp(tk.Frame):

    def __init__(self, parent):

        tk.Frame.__init__(self,parent)
        super().__init__(parent)
        self.topbar = TM.TopMenu(parent)
        self.widget = NW.FrontFrames(parent)
        self.statusbar = SB.StatusBar(parent)

        def window(main):
            main.title('MindnoteZ')
            main.update_idletasks()
            width = main.winfo_width()
            height = main.winfo_height()
            x = (main.winfo_screenwidth() // 2) - (width // 2)
            y = (main.winfo_screenheight() // 2) - (height // 2)
            main.geometry('{}x{}+{}+{}'.format(width, height, x, y))


root = tk.Tk()
# MainApp.window(root)
MainApp(root).pack(side="top", fill="both")

root.mainloop()