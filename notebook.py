from tkinter import ttk
from tkinter import *
class NB:
    def __init__(self,root):
        self.NB = ttk.Notebook(root)
        self.NB.pack(pady=6, expand=True)

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

