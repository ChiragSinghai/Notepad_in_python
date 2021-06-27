from tkinter import ttk,filedialog
from tkinter import *
import textencryption
from PIL import ImageTk,Image
import qrcode
class NB:
    def __init__(self,master,myText):
        self.myText = myText
        self.master = master
        self.top = Toplevel()
        self.top.title('Encrypt/Decrypt')
        self.top.geometry(f"400x370+{self.master.winfo_x()}+{self.master.winfo_y()}")
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
        #style.configure('TButton',font=('arial',12,'bold'))
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
        self.frame1 = ttk.Frame(self.NB, width=400, height=370)
        self.frame2 = ttk.Frame(self.NB, width=400, height=370)
        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        # add frames to notebook
        self.NB.add(self.frame1, text='Encrypt')
        self.NB.add(self.frame2, text='Decrypt')
        self.setupFrame1()
        self.setupFrame2()
        
    def setupFrame2(self):


    def setupFrame1(self):
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
        self.imagelabel = Label(self.frame1,image='',background='white')
        self.imagelabel.place(relx=0.1,rely=0.15,relwidth=0.8,relheight=0.7)
        self.keylabel = Label(self.frame1,text='Key is',font=('arial',12,'bold'))
        self.keylabel.place(relx=0.05,rely=0.9)
        self.keylabel1 = Label(self.frame1,text='',font=('arial',12,'bold'))
        self.keylabel1.place(relx=0.2,rely=0.9)
        self.clipimage = PhotoImage(file='C://Encrypted//clipboard.png')
        self.copybutton = Button(self.frame1,image=self.clipimage,compound='center',command=self.copy)
        self.copybutton.place(relx=0.45,rely=0.89)
        self.saveQR = Button(self.frame1,text='Save QR',background='white',activebackground='#add8e6',relief='solid',padx=10)
        self.saveQR.place(relx=0.7,rely=0.9)
    def callEncrypt(self):
        ranges = self.myText.tag_ranges(SEL)
        if ranges and self.check1.get():
            text = self.myText.get(*ranges)
        else:
            text = self.myText.get(1.0,END)
            text=text.strip()
        print(text)
        text1, key = textencryption.encrypt(text)
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=8,
            border=4,)
        qr.add_data(key)
        qr.make(fit=True)
        self.img = qr.make_image()
        #self.save('hey.png')
        savepath = 'C://Encrypted//hey.png'
        #savepath = filedialog.asksaveasfilename(title='Save File', defaultextension='.png',filetypes=(("Text file", "*.png"), ("Python file", "*.jpeg")))
        self.img.save(savepath)
        self.img = PhotoImage(file=savepath)
        self.imagelabel.config(image=self.img)
        if self.check1.get() and ranges:
            self.myText.delete(*ranges)
            self.myText.insert(ranges[0],text1)
        else:
            self.myText.delete(1.0,END)
            self.myText.insert(1.0,text1)
        self.keylabel1['text'] = key
        #if text==textencryption.decrypt(text1,key):
         #   print('hey')

    def copy(self):
        if self.keylabel1['text']:
            self.master.clipboard_append(self.keylabel1['text'])
            self.master.update()

    def callDecrypt(self):
        pass

if __name__=='__main__':
    master = Tk()

    text = Text(master)
    text.pack(fil=BOTH)
    text.insert('1.0', 'hy and why and Hy')
    button = Button(master, text='press', command=lambda: NB(master, text))
    button.pack()
    master.mainloop()
