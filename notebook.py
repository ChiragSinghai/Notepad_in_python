from tkinter import ttk
from tkinter import *
import textencryption
class NB:
    def __init__(self,master):
        self.master = master
        self.top = Toplevel(self.master)
        self.NB = ttk.Notebook(self.top,takefocus=True)
        self.NB.pack(expand=True,pady=5)
        #self.NB.focus_set()
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", borderwidth=2,background='#e6e8eb')
        style.configure("TNotebook.Tab",backgorund='#e6e8eb',foreground='black', lightcolor='#DF7401', borderwidth=2,padding=[3,3],relief='groove',font=('helvetica',12))
        style.configure("TFrame", background='#e6e8eb',borderwidth=2,relief='groove')
        style.map('TNotebook.Tab',background=[('selected','white'),('active','#add8e6')],expand=[("selected", [1,1,1,0])],
                  padding=[('selected',[5,5])],
                  )
        style.layout("Tab",
                     [('Notebook.tab', {'sticky': 'nswe', 'children':
                         [('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
                         # [('Notebook.focus', {'side': 'top', 'sticky': 'nswe', 'children':
                             [('Notebook.label', {'side': 'top', 'sticky': ''})],
                                            })],
                                        })]
                     )
        #print(style.element_options('TNotebook.tab'))
        # create frames
        self.design()
    def design(self):
        self.frame1 = ttk.Frame(self.NB, width=400, height=280)
        self.frame2 = ttk.Frame(self.NB, width=400, height=280)
        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        #adding checkboxes
        self.check1 = IntVar(0)
        self.check2 = IntVar(0)
        self.checkbox1 = Checkbutton(self.frame1,variable=self.check1,text='Encrypt selected Text',background='#e6e8eb',takefocus=False,
                                     activebackground='#add8e6')
        self.checkbox1.place(relx=0.1,rely=0.06)
        self.checkbox2 = Checkbutton(self.frame2,variable=self.check2,text='Decrypt selected Text',background='#e6e8eb',takefocus=False)
        self.checkbox2.place(relx=0.1,rely=0.06)
        self.okbutton1 = Button(self.frame1,text='Generate key and Encrypt',command='',background='white',activebackground='#add8e6',relief='solid')
        self.okbutton1.place(relx=0.5,rely=0.06)
        self.imagelabel = Label(self.frame1)
        self.imagelabel.place(relx=0.1,rely=0.17,relwidth=0.8,relheight=0.8)
        # add frames to notebook
        self.NB.add(self.frame1, text='Encrypt')
        self.NB.add(self.frame2, text='Decrypt')

    def callEncrypt(self):
if __name__=='__main__':
    root = Tk()
    def call():
        obj = NB(root)
    button = Button(root,text='press',command=call)
    button.pack()
    root.mainloop()
