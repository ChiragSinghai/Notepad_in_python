from tkinter import *


class Replace:
    exist = False
    def __init__(self, master, textobj):
        if not Replace.exist:
            self.master = master
            self.replacemaster = Toplevel(self.master, takefocus=True)
            self.replacemaster.protocol("WM_DELETE_WINDOW", onclose)
            self.textobj = textobj
            self.design()
            Replace.exist = True
            self.replacemaster.mainloop()
        else:
            pass

    def design(self):
        self.replacemaster.transient(self.master)
        self.replacemaster.geometry(f"400x150+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.replacemaster.resizable(False, False)
        self.replacemaster.title('Replace')
        self.findvar = StringVar()
        self.replacevar = StringVar()
        self.case = IntVar()
        self.exact = IntVar()
        self.findLabel = Label(self.replacemaster,text='Find', font=('Arial', 10, 'bold'))
        self.findEntry = Entry(self.replacemaster,textvariable=self.findvar, width=28, font=('Arial', 10, 'bold'))
        self.replaceLabel=Label(self.replacemaster,text='Replace', font=('Arial', 10, 'bold'))
        self.replaceEntry = Entry(self.replacemaster,textvariable=self.replacevar, width=28,font=('Arial', 10, ))
        self.findButton = Button(self.replacemaster,text='Find',width=10,command='',relief='solid')
        self.findallButton = Button(self.replacemaster,text='Find ALL',command='',width=10,relief='solid')
        self.replaceButton = Button(self.replacemaster,text='Replace',command='',width=10,relief='solid')
        self.repAllButton = Button(self.replacemaster,text='Replace All',command='',width=10,relief='solid')
        self.casecheck = Checkbutton(self.replacemaster,text='Case',variable=self.case)
        self.exactcheck = Checkbutton(self.replacemaster,text='Exact',variable=self.exact)
        self.findLabel.place(x=20, y=10)
        self.findEntry.place(x=80, y=10)
        self.replaceLabel.place(x=15, y=50)
        self.replaceEntry.place(x=80, y=50)
        self.findButton.place(x=310,y=10)
        self.findallButton.place(x=310,y=40)
        self.replaceButton.place(x=310,y=70)
        self.repAllButton.place(x=310,y=100)
        self.casecheck.place(x=80,y=80)
        self.exactcheck.place(x=130,y=80)

    def onclose(self):
        Replace.exist = False
        self.replacemaster.destroy()

class Find:
    exist = False
    def __init__(self, master, textobj):
        if not Find.exist:
            self.master = master
            self.findmaster = Toplevel(self.master, takefocus=True)
            self.findmaster.protocol("WM_DELETE_WINDOW", self.onclose)
            self.textobj = textobj
            self.design()
            Find.exist = True

            self.findmaster.mainloop()
        else:
            pass

    def design(self):
        self.findmaster.transient(self.master)
        self.findmaster.geometry(f"400x150+{self.master.winfo_x()}+{self.master.winfo_y()}")
        self.findmaster.resizable(False, False)
        self.findmaster.title('Find')
        self.findvar = StringVar()
        self.case = IntVar()
        self.exact = IntVar()
        self.findLabel = Label(self.findmaster, text='Find', font=('Arial', 10, 'bold'))
        self.findEntry = Entry(self.findmaster, textvariable=self.findvar, width=28, font=('Arial', 10, 'bold'))
        self.findButton = Button(self.findmaster, text='Find', width=10, command=self.findnext, relief='solid')
        self.findallButton = Button(self.findmaster, text='Find All', command='', width=10, relief='solid')
        self.casecheck = Checkbutton(self.findmaster, text='Case', variable=self.case)
        self.exactcheck = Checkbutton(self.findmaster, text='Exact', variable=self.exact)
        self.closebutton = Button(self.findmaster,text='Close',command=self.onclose,width=10,relief='solid')
        self.findButton.place(x=310, y=10)
        self.findallButton.place(x=310, y=40)
        self.findLabel.place(x=20, y=10)
        self.findEntry.place(x=80, y=10)
        self.closebutton.place(x=310,y=70)
        self.casecheck.place(x=80, y=40)
        self.exactcheck.place(x=130, y=40)

    def onclose(self):
        Find.exist = False
        self.findmaster.destroy()
        #self.findmaster.quit()

    def findnext(self):
        print(self.exact.get(),self.case.get())



if __name__ == '__main__':
    root = Tk()
    text = Text(root)
    text.pack(fil=BOTH)
    button = Button(root, text='press', command=lambda: Find(root, text))
    button.pack()
    root.mainloop()
