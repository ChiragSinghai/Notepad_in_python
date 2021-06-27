from tkinter import ttk
from tkinter import *
class NB:
    def __init__(self):
        root=Toplevel()
        self.NB = ttk.Notebook(root,takefocus=True)
        self.NB.pack(expand=True,pady=5)
        #self.NB.focus_set()
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", borderwidth=0)
        style.configure("TNotebook.Tab", foreground='black', lightcolor='#DF7401', borderwidth=0,padding=[3,3],relief='solid',font=('helvetica',12))
        style.configure("TFrame", background='white',borderwidth=0)
        style.map('TNotebook.Tab',background=[('selected','white'),('active','#add8e6')],expand=[("selected", [1,1,1,0])],
                  padding=[('selected',[5,5])],
                  )
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                         [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                         # [('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                             [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                                # })],
                                                })],
                                        })]
                     )
        print(style.element_options('TNotebook.tab'))
        # create frames
        frame1 = ttk.Frame(self.NB, width=400, height=280)
        frame2 = ttk.Frame(self.NB, width=400, height=280)

        frame1.pack(fill='both', expand=True)
        frame2.pack(fill='both', expand=True)

        # add frames to notebook

        self.NB.add(frame1, text='Encrypt')
        self.NB.add(frame2, text='Decrypt')
if __name__=='__main__':
    root = Tk()
    def call():
        obj = NB()
    button = Button(root,text='press',command=call)
    button.pack()
    root.mainloop()
