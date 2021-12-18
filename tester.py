from tkinter import *


class Replace:
    exist = False
    def __init__(self, master, textobj):
        if not Replace.exist:
            self.master = master
            self.replacemaster = Toplevel(self.master, takefocus=True)
            self.replacemaster.iconbitmap('folder/Icon.ico')
            self.replacemaster.protocol("WM_DELETE_WINDOW",self.onclose)
            self.textobj = textobj
            self.current_index = None
            self.current_word = None
            self.find_list = []
            self.design()
            Replace.exist = True
            #self.replacemaster.mainloop()
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
        self.replaceEntry = Entry(self.replacemaster,textvariable=self.replacevar, width=28,font=('Arial', 10,'bold'))
        self.findButton = Button(self.replacemaster,text='Find',width=10,command=self.findnext,relief='solid')
        self.findallButton = Button(self.replacemaster,text='Find All',command=self.findall,width=10,relief='solid')
        self.replaceButton = Button(self.replacemaster,text='Replace',width=10,relief='solid',command=self.replace)
        self.repAllButton = Button(self.replacemaster,text='Replace All',command=self.replaceall,width=10,relief='solid')
        self.casecheck = Checkbutton(self.replacemaster,text='Case',variable=self.case,command=self.case_fun)
        self.exactcheck = Checkbutton(self.replacemaster,text='Regexp',variable=self.exact,command=self.exact_fun)
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
        self.tagremover()
        self.replacemaster.destroy()

    def replace(self):
        if self.current_word == self.findEntry.get():
            if self.find_list:
                replaced_word = self.replaceEntry.get()
                lastidx = '% s+% dc' % (self.find_list[self.current_index], len(self.findEntry.get()))
                self.textobj.delete(self.find_list[self.current_index], lastidx)
                self.textobj.insert(self.find_list[self.current_index], replaced_word)
                self.get_txt_list()
                if self.current_index <= len(self.find_list)-2:
                    self.current_index -= 1
                else:
                    self.current_index = 0
                self.findnext()

        else:
            self.findnext()
            self.replace()

    def replaceall(self):
        self.current_word = None
        self.findnext()
        self.textobj.tag_remove('replace_all','1.0',END)
        for _ in range(len(self.find_list)):
            replaced_word = self.replaceEntry.get()
            lastidx = '% s+% dc' % (self.find_list[self.current_index], len(self.findEntry.get()))
            self.textobj.delete(self.find_list[self.current_index], lastidx)
            self.textobj.insert(self.find_list[self.current_index], replaced_word)
            idx = '% s+% dc' % (self.find_list[self.current_index], len(self.replaceEntry.get()))
            self.textobj.tag_add('replace_all',self.find_list[self.current_index],idx)
            self.get_txt_list()
            if self.current_index <= len(self.find_list) - 2:
                self.current_index -= 1
            else:
                self.current_index = 0
            self.findnext()
        self.textobj.tag_config('replace_all',background='blue')

    def case_fun(self):
        self.find_list.clear()
        self.current_word = None
        self.findnext()

    def exact_fun(self):
        self.find_list.clear()
        self.current_word = None
        self.findnext()

    def tagremover(self):
        #print(self.textobj.tag_names())
        for tag in self.textobj.tag_names():
            if tag != 'sel':
                self.textobj.tag_remove(tag,'1.0',END)

    def findnext(self):
        #print(self.exact.get(),self.case.get())
        self.textobj.tag_remove('Found','1.0',END)
        #self.tagremover()
        if self.current_word == self.findEntry.get():
            if self.current_index+1 >= len(self.find_list):
                self.current_index = 0
            else:
                self.current_index += 1
        else:
            self.tagremover()
            self.current_word = self.findEntry.get()
            self.get_txt_list()
            self.current_index = 0
        if self.find_list:
            lastidx = '% s+% dc' % (self.find_list[self.current_index], len(self.current_word))
            self.textobj.tag_add('Found', self.find_list[self.current_index], lastidx)
            self.textobj.tag_config('Found', background='orange')
            self.textobj.tag_raise('Found')

    def findall(self):
        #self.tagremover()
        if self.current_word != self.findEntry.get():
            self.tagremover()
        else:
            self.textobj.tag_remove('All','1.0',END)
        self.get_txt_list()
        for word_index in self.find_list:
            lastidx = '% s+% dc' % (word_index, len(self.findEntry.get()))
            self.textobj.tag_add('All',word_index,lastidx)
        self.textobj.tag_config('All',background='yellow')

    def get_txt_list(self):
        if self.findEntry.get():
            self.find_list.clear()
            txt_to_search = self.findEntry.get()
            if txt_to_search:
                idx = '1.0'
                while True:
                    idx = self.textobj.search(txt_to_search,idx,nocase=not(self.case.get()),regexp=self.exact.get(),stopindex=END)
                    if not idx:
                        break
                    self.find_list.append(idx)
                    lastidx = '% s+% dc' % (idx, len(self.findEntry.get()))
                    idx = lastidx

class Find:
    exist = False
    def __init__(self, master, textobj):
        self.current_index = None
        self.current_word = None
        self.find_list = []
        if not Find.exist:
            self.master = master
            self.findmaster = Toplevel(self.master, takefocus=True)
            self.findmaster.iconbitmap('folder/Icon.ico')
            self.findmaster.protocol("WM_DELETE_WINDOW", self.onclose)
            self.textobj = textobj
            self.design()
            Find.exist = True
            #self.findmaster.mainloop()
        else:
            pass

    def design(self):
        self.findmaster.transient(self.master)
        self.findmaster.geometry(f"400x110+{self.master.winfo_x()+20}+{self.master.winfo_y()+10}")
        self.findmaster.resizable(False, False)
        self.findmaster.title('Find')
        self.findvar = StringVar('')
        self.case = IntVar(0)
        self.exact = IntVar(0)
        self.findLabel = Label(self.findmaster, text='Find', font=('Arial', 10, 'bold'))
        self.findEntry = Entry(self.findmaster, textvariable=self.findvar, width=28, font=('Arial', 10, 'bold'))
        self.findButton = Button(self.findmaster, text='Find', width=10, command=self.findnext, relief='solid')
        self.findallButton = Button(self.findmaster, text='Find All', command=self.findall, width=10, relief='solid')
        self.casecheck = Checkbutton(self.findmaster, text='Case', variable=self.case,command=self.case_fun)
        self.exactcheck = Checkbutton(self.findmaster, text='Regexp', variable=self.exact,command=self.exact_fun)
        self.closebutton = Button(self.findmaster,text='Close',command=self.onclose,width=10,relief='solid')
        self.findButton.place(x=310, y=10)
        self.findallButton.place(x=310, y=40)
        self.findLabel.place(x=20, y=10)
        self.findEntry.place(x=80, y=10)
        self.closebutton.place(x=310,y=70)
        self.casecheck.place(x=80, y=40)
        self.exactcheck.place(x=130, y=40)
        self.findEntry.focus_set()

    def case_fun(self):
        self.find_list.clear()
        self.current_word = None
        self.findnext()

    def exact_fun(self):
        self.find_list.clear()
        self.current_word = None
        self.findnext()

    def onclose(self):
        Find.exist = False
        self.tagremover()
        self.findmaster.destroy()

    def tagremover(self):
        #print(self.textobj.tag_names())
        for tag in self.textobj.tag_names():
            if tag != 'sel':
                self.textobj.tag_remove(tag,'1.0',END)

    def findnext(self):
        #print(self.exact.get(),self.case.get())
        self.textobj.tag_remove('Found','1.0',END)
        #self.tagremover()
        if self.current_word == self.findEntry.get():
            if self.current_index+1 >= len(self.find_list):
                self.current_index = 0
            else:
                self.current_index += 1
        else:
            self.tagremover()
            self.current_word = self.findEntry.get()
            self.get_txt_list()
            self.current_index = 0
        if self.find_list:
            lastidx = '% s+% dc' % (self.find_list[self.current_index], len(self.current_word))
            self.textobj.tag_add('Found', self.find_list[self.current_index], lastidx)
            self.textobj.tag_config('Found', background='orange')
            self.textobj.tag_raise('Found')

    def findall(self):
        #self.tagremover()
        if self.current_word != self.findEntry.get():
            self.tagremover()
        else:
            self.textobj.tag_remove('All','1.0',END)
        self.get_txt_list()
        for word_index in self.find_list:
            lastidx = '% s+% dc' % (word_index, len(self.findEntry.get()))
            self.textobj.tag_add('All',word_index,lastidx)
        self.textobj.tag_config('All',background='yellow')

    def get_txt_list(self):
        if self.findEntry.get():
            self.find_list.clear()
            txt_to_search = self.findEntry.get()
            if txt_to_search:
                idx = '1.0'
                while True:
                    idx = self.textobj.search(txt_to_search,idx,nocase=not(self.case.get()),regexp=self.exact.get(),stopindex=END)
                    if not idx:
                        break
                    self.find_list.append(idx)
                    lastidx = '% s+% dc' % (idx, len(self.findEntry.get()))
                    idx = lastidx


if __name__ == '__main__':
    master = Tk()
    text = Text(master)
    text.pack(fil=BOTH)
    text.insert('1.0','hy and why and Hy')
    button = Button(master, text='press', command=lambda: Find(master, text))
    button.pack()
    master.mainloop()
