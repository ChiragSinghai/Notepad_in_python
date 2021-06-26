from tkinter import ttk
from tkinter import *
class NB:
    def __init__(self,root):
        self.NB = ttk.Notebook(root)
        self.NB.pack(expand=True)
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook",foreground='green')
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                         [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                         # [('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                             [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                                # })],
                                                })],
                                        })]
                     )

        # create frames
        frame1 = ttk.Frame(self.NB, width=400, height=280)
        frame2 = ttk.Frame(self.NB, width=400, height=280)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        self.NB.add(frame1, text='General Information')
        self.NB.add(frame2, text='Profile')
if __name__=='__main__':
    root = Tk()
    master=Toplevel(root)
    obj=NB(master)
    root.mainloop()

