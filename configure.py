from tkinter import *
import time
from tkinter import font,ttk

import fontsave


class configure():
    def __init__(self,root,X,Y,defaultfont):
        self.top = Toplevel(root)
        self.defaultfont = defaultfont
        self.width=600
        self.height=root.winfo_screenheight()-100
        X+=20
        Y+=20
        self.top.grab_set()   
        self.top.transient(root)
        self.top.geometry(f"{self.width}x{self.height}+{X}+{Y}")
        self.top.resizable(False,False)
        self.top.title('Fonts')
    #===============================================
        
        self.exampletextfont=font.Font(family=self.defaultfont['family'],size=self.defaultfont['size'],weight=self.defaultfont['weight'],slant=self.defaultfont['slant'])
        #===============================================
        self.frame=Frame(self.top)
        self.frame.pack(fill=BOTH,expand=True)
    #================================================
        self.fontframe=LabelFrame(self.frame,text="Fonts")
        self.fontframe.place(relx=0.0,rely=0,relwidth=0.4,relheight=0.7)
        self.sb=Scrollbar(self.fontframe)
        self.sb.place(relx=0.9,relheight=1)
        self.textlist=Listbox(self.fontframe,font=('Arial',14),activestyle='none',height=15,width=20
                                        , bg="thistle1", fg="light slate gray"
                                        ,selectbackground="light slate gray", selectforeground="thistle1"
                                        ,yscrollcommand=self.sb.set)
        self.textlist.place(relx=0,rely=0,relwidth=0.9,relheight=1)
        self.sb.config(command=self.textlist.yview)
    #========================================================
        self.textlistname=font.families()
        #print(self.defaultfont['family'])
        for textname in self.textlistname:
            self.textlist.insert(END,textname)
            if textname==self.defaultfont['family']:
                self.textlist.activate(END)
                self.textlist.index(END)
                self.textlist.selection_set(END,last=None)
                self.textlist.see(END)

    #========================================================
        self.exampleframe=LabelFrame(self.frame,text="Sample(Editable)")
        self.exampleframe.place(relx=0.4,relwidth=0.6,relheight=0.9)
        self.verticalscroll=Scrollbar(self.exampleframe)
        self.verticalscroll.place(relx=0.95,relheight=0.95)
        self.horizontalscroll=Scrollbar(self.exampleframe,orient='horizontal')
        self.horizontalscroll.place(rely=0.95,relwidth=0.95)
        self.textexample=Text(self.exampleframe,wrap='none',xscrollcommand=self.horizontalscroll.set
                         ,yscrollcommand=self.verticalscroll.set,font=self.exampletextfont)
        self.textexample.place(relx=0,relwidth=0.95,relheight=0.95)
        self.verticalscroll.config(command=self.textexample.yview)
        self.horizontalscroll.config(command=self.textexample.xview)
        
    #=======================================================
        self.buttonframe=Frame(self.frame)
        self.buttonframe.place(rely=0.9,relwidth=1,relheight=0.1)
        self.applybutton=ttk.Button(self.buttonframe,text="Apply",command=self.ok)
        self.applybutton.place(relx=0.3,rely=0.2)
        self.okbutton=ttk.Button(self.buttonframe,text="Cancel",command=self.cancel)
        self.okbutton.place(relx=0.6,rely=0.2)
    #==============================
        sizeoptions=[12,14,16,18,20,22,24,26,28,30,32,34]
        self.sizevar=IntVar()
        self.boldvar=IntVar()
        self.italic = IntVar()
        self.italic.set(0 if self.exampletextfont['slant'] == 'roman' else 1)
        self.boldvar.set(0 if self.exampletextfont['weight']=='normal' else 1)
        self.sizevar.set(self.exampletextfont['size'])
        self.sizemenu=OptionMenu(self.top,self.sizevar,*sizeoptions,command=self.sizeselected)
        self.sizemenu.place(relx=0.1,rely=0.75)
    
        self.italic_checkbutton = Checkbutton(self.top,variable=self.italic,command=self.italic_click,text='Italic',font=("Arial",14))
        self.italic_checkbutton.place(relx=0.2,rely=0.8)
        self.checkbutton=Checkbutton(self.top,variable=self.boldvar,command=self.boldclick
                                     ,text="Bold",font=("Arial",14))
        self.checkbutton.place(relx=0.2,rely=0.75)
        
    
        self.textlist.bind('<<ListboxSelect>>',self.listboxselect)
        self.top.mainloop()   
    def boldclick(self):
        if self.boldvar.get():
            self.exampletextfont.configure(weight="bold")
            
        else:
            self.exampletextfont.configure(weight="normal")
    def italic_click(self):
        if self.italic.get():
            self.exampletextfont.configure(slant='italic')
        else:
            self.exampletextfont.configure(slant='roman')

    def sizeselected(self,event):
        selectedsize=self.sizevar.get()
        self.exampletextfont.configure(size=selectedsize)

    def listboxselect(self,event):
        selected=self.textlist.curselection()
        selectedfont=self.textlist.get(selected[0],last=None)
        self.exampletextfont.configure(family=selectedfont)

    def ok(self):
        selected=self.textlist.curselection()
        selectedfont=self.textlist.get(selected[0],last=None)
        bold=self.boldvar.get()
        selectedsize=self.sizevar.get()
        italic=self.italic.get()
        self.defaultfont.configure(family=selectedfont,size=selectedsize,weight='bold' if bold else 'normal',slant='italic' if italic else 'roman')
        fontsave.setFont(selectedfont,selectedsize,bold,italic)
        #return selectedfont,selectedsize,bold
##        print(self.defaultfont.actual())
##        print(self.exampletextfont.actual())
        self.top.destroy()
        

    def cancel(self):
        self.top.destroy()

    
if __name__ == '__main__':
    master = Tk()
    master.geometry('200x200+0+0')
    fontandsize = fontsave.getFont()

    defaultfont = font.Font(family=fontandsize[0], size=(fontandsize[1]),
                            weight='bold' if fontandsize[2] == '1' else 'normal',
                            slant='italic' if fontandsize[3] == '1' else 'roman')

    button = Button(master,text="press",command=lambda:configure(master,master.winfo_x(),master.winfo_y(),defaultfont))
    button.pack()
    label = Label(master,text='hey font is changing',font=defaultfont)
    label.pack()
    master.mainloop()
