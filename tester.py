from tkinter import *


class Replace:
    exist = False
    def __init__(self, master, textobj):
        if not Replace.exist:
            self.master = master
            self.replacemaster = Toplevel(self.master, takefocus=True)
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
        self.findLabel = Label(self.replacemaster,text='Find', font=('Arial', 10, 'bold'))
        self.findEntry = Entry(self.replacemaster,textvariable=self.findvar, width=28, font=('Arial', 10, 'bold'))
        self.replaceLabel=Label(self.replacemaster,text='Replace', font=('Arial', 10, 'bold'))
        self.replaceEntry = Entry(self.replacemaster,textvariable=self.replacevar, width=28,font=('Arial', 10, ))
        self.findButton = Button(self.replacemaster,text='Find',width=10,command='',relief='solid')
        self.findallButton = Button(self.replacemaster,text='Find Next',command='',width=10,relief='solid')
        self.replaceButton = Button(self.replacemaster,text='Find All',command='',width=10,relief='solid')
        self.repAllButton = Button(self.replacemaster,text='Replace All',command='',width=10,relief='solid')
        self.findLabel.place(x=20, y=10)
        self.findEntry.place(x=80, y=10)
        self.replaceLabel.place(x=15, y=50)
        self.replaceEntry.place(x=80, y=50)
        self.findButton.place(x=310,y=10)
        self.findallButton.place(x=310,y=40)
        self.replaceButton.place(x=310,y=70)
        self.repAllButton.place(x=310,y=100)

if __name__ == '__main__':
    root = Tk()
    text = Text(root)
    text.pack(fil=BOTH)
    button = Button(root, text='press', command=lambda: Replace(root, text))
    button.pack()
    root.mainloop()
