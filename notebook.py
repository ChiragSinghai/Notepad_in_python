from tkinter import ttk,filedialog
from tkinter import *
import textencryption
from PIL import ImageTk,Image
from io import StringIO
import qrcode
class NB:
    def __init__(self,master,myText):
        self.myText = myText
        self.master = master
        self.top = Toplevel()
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
        self.okbutton1 = Button(self.frame1,text='Generate key and Encrypt',command=self.callEncrypt,background='white',activebackground='#add8e6',relief='solid')
        self.okbutton1.place(relx=0.5,rely=0.06)
        img = PhotoImage("P://pythonfiles//yo.png")
        '''
        canvas=Canvas(self.frame1)
        canvas.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)
        canvas.create_image(20, 20, anchor=NW, image=img)
        canvas.image = img
        '''
        self.imagelabel = ttk.Label(self.frame1,image=(img))
        self.imagelabel.place(relx=0.2,rely=0.2,relwidth=0.8,relheight=0.8)
        self.imagelabel.config(image=img)
        # add frames to notebook
        self.NB.add(self.frame1, text='Encrypt')
        self.NB.add(self.frame2, text='Decrypt')

    def callEncrypt(self):
        ranges = self.myText.tag_ranges(SEL)
        if ranges and self.check1.get():
            text = self.myText.get(*ranges)
        else:
            text = self.myText.get(1.0,END)
            text=text[:-1]
        text1, key = textencryption.encrypt(text)
        img = qrcode.make(key)
        savepath = filedialog.asksaveasfilename(title='Save File', defaultextension='.png',filetypes=(("Text file", "*.png"), ("Python file", "*.jpeg")))
        print(savepath)
        img.save(savepath)
        img = ImageTk.PhotoImage(file=savepath)
        self.imagelabel.config(image=img)
        #self.myText.delete(1.0,END)

        #if text==textencryption.decrypt(text1,key):
         #   print('hey')

if __name__=='__main__':
    master = Tk()
    text = Text(master)
    text.pack(fil=BOTH)
    text.insert('1.0', 'hy and why and Hy')
    button = Button(master, text='press', command=lambda: NB(master, text))
    button.pack()
    master.mainloop()
