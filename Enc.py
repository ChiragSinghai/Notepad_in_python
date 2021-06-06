from tkinter import *
from tkinter import filedialog, messagebox
import os.path
from tkinter import font, ttk
from fontsave import getFont
from tester import Replace, Find, configure


class Main:
    def __init__(self, master):
        self.fontandsize = getFont()
        self.default_font = font.Font(family=self.fontandsize[0], size=(self.fontandsize[1]),
                                      weight='bold' if self.fontandsize[2] == '1' else 'normal',
                                      slant='italic' if self.fontandsize[3] == '1' else 'roman')
        self.current_file = None
        self.current_file_path = None
        self.saved = False
        self.wrap_value = IntVar(0)
        self.files_ext = (("Text file", "*.txt"), ("Python file", "*.py"), ("CSV files", "*.csv"),
                          ("HTML file", "*.html"), ("All file", "*.*"))

        self.master = master
        self.menu_implement()
        self.design()
        self.bind_keys()
        self.geometry()
        self.master.protocol("WM_DELETE_WINDOW", self.onclose)
        self.saved_position()
        self.loop()

    def geometry(self):
        height = int(self.master.winfo_screenheight() * 0.5)
        width = int(self.master.winfo_screenwidth() * 0.5)
        self.master.title('untitled-Encrypted')
        self.master.geometry(f'{width}x{height}+20+20')

    def menu_implement(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        # self.filemenu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New playlist", accelerator="Ctrl+N", command=self.new_file)
        self.filemenu.add_command(label="Open file", accelerator='Ctrl+O', command=self.open_file)
        self.filemenu.add_command(label="Save", accelerator='Ctrl+S', command=self.save_file)
        self.filemenu.add_command(label="Save as...", accelerator='Ctrl+Shift+S', command=self.save_as_file)
        self.filemenu.add_command(label="Close", command='')
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.onclose)

        # self.editmenu
        self.editmenu = Menu(self.menubar, tearoff=0, postcommand=self.editmenu_post)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.editmenu.add_command(label="Cut", command=self.cut, accelerator='Ctrl-X')
        self.editmenu.add_command(label="Copy", command=self.copy, accelerator='Ctrl-C')
        self.editmenu.add_command(label="Paste", command=self.paste, accelerator='Ctrl-V')
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Select All", command=self.select_all, accelerator='Ctrl-A')
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Find", command='', accelerator='Ctrl-F')
        self.editmenu.add_command(label='Replace', command='', accelerator='Ctrl-R')

        # self.editmenu.add_command(label="Paste")

        # self.optionmenu
        self.optionmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Option", menu=self.optionmenu)
        self.optionmenu.add_checkbutton(label="Wrap", onvalue=1, offvalue=0, variable=self.wrap_value,
                                        command=self.wrap)
        # self.optionmenu.add_command(label="Pause",image=pause_option,compound=LEFT)
        self.optionmenu.add_command(label='Font', image='', compound=LEFT,
                                    command=lambda: configure(self.master, self.master.winfo_x(),
                                                              self.master.winfo_y(),self.default_font))

        # Help
        self.helpmenu = Menu(self.menubar, tearoff=0, )
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About us", command='')

    def loop(self):
        self.master.mainloop()

    def design(self):
        # self.status_bar
        self.status_bar = Frame(self.master, height=15, relief=RIDGE, bd=1)
        self.status_bar.pack(side=BOTTOM, fill=X)
        self.column_label = Label(self.status_bar, text='column: 1', width=35, anchor=W, relief=RIDGE, bd=1)
        self.column_label.pack(side=RIGHT)
        self.row_label = Label(self.status_bar, text='row: 1', width=35, anchor=W, relief=RIDGE, bd=1)
        self.row_label.pack(side=RIGHT)
        self.horizontal_scroll = Scrollbar(self.master, orient=HORIZONTAL)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)
        self.vertical_scroll = Scrollbar(self.master)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)
        self.myText = Text(self.master, xscrollcommand=self.horizontal_scroll.set,
                           yscrollcommand=self.vertical_scroll.set, height=1,
                           width=1, wrap=NONE, undo=True, font=self.default_font)
        self.myText.focus_set()
        self.myText.pack(fill=BOTH, expand=True)
        self.vertical_scroll.config(command=self.myText.yview)
        self.horizontal_scroll.config(command=self.myText.xview)

    def bind_keys(self):
        self.myText.bind('<Control-z>', self.undo)
        self.myText.bind('<Control-a>', self.select_all)
        self.myText.bind('<Control-Shift-Z>', self.redo)
        self.myText.bind('<BackSpace>', self.backspace)
        self.myText.bind('<KeyRelease>', self.rowandcolumn)
        self.myText.bind('<KeyPress>', self.rowandcolumn)
        self.myText.bind('<ButtonPress>', self.position)

    def editmenu_post(self):
        try:
            if self.myText.selection_get():
                self.editmenu.entryconfig(0, state=NORMAL)
                self.editmenu.entryconfig(1, state=NORMAL)
        except TclError:
            self.editmenu.entryconfig(0, state=DISABLED)
            self.editmenu.entryconfig(1, state=DISABLED)

    def onclose(self):
        self.save_check()
        if not self.saved:
            answer = messagebox.askyesnocancel(parent=self.master, title='Encrypted',
                                               message=f'Do you want to save changes to {self.current_file[0] if self.current_file else "untitled"}')
            if answer:
                if self.current_file:
                    self.save_file()
                    self.master.destroy()
                else:
                    self.save_file()
            elif answer is None:
                pass
            else:
                self.master.destroy()
        else:
            self.master.destroy()

    def saved_position(self):
        self.saved_content = self.myText.get(1.0, END)

    def open_file_internal(self, file_arg=None):
        if file_arg is None:
            try:
                file_name = filedialog.askopenfilename(title='Open file', filetypes=self.files_ext)
                if file_name:
                    self.current_file_path = file_name
                    file = os.path.splitext(os.path.basename(file_name))
                    self.current_file = file
                    file_object = open(file_name)
                    content = file_object.read()
                    self.myText.delete(1.0, END)
                    self.myText.insert(END, content)
                    self.myText.mark_set('insert', 1.0)
                    self.master.title(f'{file[0]}-Encrypted')
                    self.saved_position()
            except UnicodeDecodeError:
                print(UnicodeDecodeError)
        else:
            file_name = file_arg
            self.current_file_path = file_name
            file = os.path.splitext(os.path.basename(file_name))
            self.current_file = file
            file_object = open(file_name)
            content = file_object.read()
            self.myText.delete(1.0, END)
            self.myText.insert(END, content)
            self.myText.mark_set('insert', 1.0)
            self.master.title(f'{file[0]}-Encrypted')
            self.saved_position()

    def open_file(self):
        self.save_check()
        if not self.saved:
            answer = messagebox.askyesnocancel(title='Encrypted',
                                               message=f'Do you want to hey save changes to {self.current_file[0] if self.current_file else "untitled"}')
            if answer:
                if current_file:
                    self.save_file()
                    self.open_file_internal()
                else:
                    self.save_file()

            elif answer is None:
                pass
            else:
                self.open_file_internal()
        else:
            self.open_file_internal()

    def new_file_internal(self):
        print('hey')
        self.myText.delete(1.0, END)
        self.master.title('untitled-Encrypted')
        self.saved = True
        self.current_file = None
        self.current_file_path = None
        self.saved_position()

    def new_file(self):
        self.save_check()
        if not self.saved:
            answer = messagebox.askyesnocancel(title='Encrypted',
                                               message=f'do you want to save changes to {self.current_file[0] if self.current_file else "untitled"}')
            if answer:
                if self.current_file:
                    self.save_file()
                    self.new_file_internal()
                else:
                    self.save_file()

            elif answer is None:
                pass
            else:
                self.new_file_internal()
        else:
            if self.current_file:
                self.new_file_internal()

    def save_as_file(self):
        if self.current_file:
            found = False
            file_ext_name = (self.current_file[1], ('*' + self.current_file[1]))
            for file_ext_name in self.files_ext:
                if file_ext_name[1] == ('*' + self.current_file[1]):
                    found = True
                    break
            if not found:
                file_ext_name = (self.current_file[1], ('*' + self.current_file[1]))

            save_filename = filedialog.asksaveasfilename(initialdir=self.current_file_path,
                                                         initialfile=self.current_file[0],
                                                         title='Save As', defaultextension=self.current_file[1],
                                                         filetypes=(file_ext_name, ('All files', '*.*')))
            if save_filename:
                os.rename(fr'{self.current_file_path}', fr'{save_filename}')
                self.current_file_path = save_filename
                self.current_file = os.path.splitext(os.path.basename(save_filename))
                self.master.title(f'{current_file[0]}-Encrypted')
                self.save_file()
        else:
            self.save_file()

    def save_file(self):
        self.save_check()
        if self.current_file:
            if not self.saved:
                file_object = open(self.current_file_path, 'w')
                file_object.write(self.myText.get(1.0, END))
                file_object.close()
                self.saved_position()
        else:
            save_filename = filedialog.asksaveasfilename(title='Save File', defaultextension='.txt',
                                                         filetypes=self.files_ext)
            if save_filename:
                self.current_file_path = save_filename
                file_object = open(self.current_file_path, 'w')
                file_object.write(self.myText.get(1.0, END))
                file_object.close()
                self.current_file = os.path.splitext(os.path.basename(save_filename))
                self.master.title(f'{self.current_file[0]}-Encrypted')
                self.saved_position()

    def rowandcolumn(self, event=None):
        current_cursor = self.myText.index(INSERT).split(".")
        self.row_label.config(text=f'row: {current_cursor[0]}')
        self.column_label.config(text=f'column: {int(current_cursor[1]) + 1}')
        if event.state == 4 and event.keysym == 'o':
            self.open_file()
            return 'break'
        if event.state == 4 and event.keysym == 'n':
            self.new_file()
            return 'break'
        if event.state == 4 and event.keysym == 's':
            self.save_file()
            return 'break'
        if event.state == 5 and event.keysym == 'S':
            self.save_as_file()
            return 'break'

    def check(self, event=None):
        pass

    def undo(self, event=None):
        try:
            print('undo')
            self.myText.edit_undo()
            return 'break'
        except TclError as e:
            self.redo()
            return 'break'

    def redo(self, event=None):
        try:
            print('bitch')
            self.myText.edit_redo()
            return 'break'
        except TclError as e:
            self.undo()
            return 'break'

    def select_all(self, event=None):
        print(self.myText.index(END))
        print(type(self.myText.index(END)))
        for i in range(1,int(self.myText.index(END).split('.')[0])):
            self.myText.tag_add('sel',f'{i}.0',f'{i}.end')
        #self.myText.tag_add('sel', 1.0, END)
        return "break"

    def backspace(self, event):
        print('here')
        self.rowandcolumn(event)
        #self.myText.edit_separator()

    def paste(self):
        self.myText.event_generate('<<Paste>>')

        '''
        selected_text = master.clipboard_get()
        print(selected_text)
        self.myText.insert(INSERT, selected_text)
        '''

    def cut(self):
        self.myText.event_generate('<<Cut>>')
        '''
        selected_text = self.myText.selection_get()
        self.myText.delete("sel.first", "sel.last")
        master.clipboard_clear()
        master.clipboard_append(selected_text)
        '''

    def copy(self):
        self.myText.event_generate('<<Copy>>')
        '''
        selected_text = self.myText.selection_get()
        master.clipboard_clear()
        master.clipboard_append(selected_text)
        '''

    def wrap(self):
        if self.wrap_value.get():
            self.myText.config(wrap=WORD)
            self.horizontal_scroll.pack_forget()
        else:
            self.myText.config(wrap=NONE)
            self.horizontal_scroll.pack(side=BOTTOM, fill=X)

    def position(self, event):
        print(event)
        self.myText.mark_set('insert', "@%d,%d" % (event.x, event.y))
        current_cursor = self.myText.index(INSERT).split(".")
        self.row_label.config(text=f'row: {current_cursor[0]}')
        self.column_label.config(text=f'column: {int(current_cursor[1]) + 1}')

    def save_check(self):
        check_content = self.myText.get(1.0, END)
        if check_content == self.saved_content:
            self.saved = True
        else:
            self.saved = False


root = Tk()
obj = Main(root)
print('this is the end')
