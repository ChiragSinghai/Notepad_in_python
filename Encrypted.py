from tkinter import *
from tkinter import filedialog, messagebox
import os.path
from tkinter import font, ttk
import fontsave
from tester import Replace,Find,configure

master = Tk()
fontandsize = fontsave.getFont()
default_font = font.Font(family=fontandsize[0], size=(fontandsize[1]), weight='bold' if fontandsize[2] == '1' else 'normal',
                         slant='italic' if fontandsize[3] == '1' else 'roman')
current_file = None
current_file_path = None
saved = False
wrap_value = IntVar()
wrap_value.set(0)
files_ext = (("Text file", "*.txt"), ("Python file", "*.py"), ("CSV files", "*.csv"),
             ("HTML file", "*.html"), ("All file", "*.*"))


def saved_position():
    global saved_content
    saved_content = myText.get(1.0, END)


def open_file_internal(file_arg=None):
    global current_file, current_file_path
    if file_arg is None:
        try:
            file_name = filedialog.askopenfilename(title='Open file', filetypes=files_ext)
            if file_name:
                current_file_path = file_name
                file = os.path.splitext(os.path.basename(file_name))
                current_file = file
                file_object = open(file_name)
                content = file_object.read()
                myText.delete(1.0, END)
                myText.insert(END, content)
                myText.mark_set('insert', 1.0)
                master.title(f'{file[0]}-Encrypted')
                saved_position()
        except UnicodeDecodeError:
            print(UnicodeDecodeError)
    else:
        file_name = file_arg
        current_file_path = file_name
        file = os.path.splitext(os.path.basename(file_name))
        current_file = file
        file_object = open(file_name)
        content = file_object.read()
        myText.delete(1.0, END)
        myText.insert(END, content)
        myText.mark_set('insert', 1.0)
        master.title(f'{file[0]}-Encrypted')
        saved_position()


def open_file():
    global current_file, saved
    save_check()
    if not saved:
        answer = messagebox.askyesnocancel(title='Encrypted', message=f'Do you want to hey save changes to {current_file[0] if current_file else "untitled"}')
        if answer:
            if current_file:
                save_file()
                open_file_internal()
            else:
                save_file()

        elif answer is None:
            pass
        else:
            open_file_internal()
    else:
        open_file_internal()


def new_file_internal():
    global saved, current_file, current_file_path
    myText.delete(1.0, END)
    master.title('untitled-Encrypted')
    saved = True
    current_file = None
    current_file_path = None
    saved_position()


def new_file():
    global current_file, saved
    save_check()
    if not saved:
        answer = messagebox.askyesnocancel(title='Encrypted',
                                           message=f'do you want to save changes to {current_file[0] if current_file else "untitled"}')
        if answer:
            if current_file:
                save_file()
                new_file_internal()
            else:
                save_file()

        elif answer is None:
            pass
        else:
            new_file_internal()
    else:
        new_file_internal()


def save_as_file():
    global current_file, current_file_path
    if current_file:
        found = False
        file_ext_name = (current_file[1], ('*' + current_file[1]))
        for file_ext_name in files_ext:
            if file_ext_name[1] == ('*'+current_file[1]):
                found = True
                break
        if not found:
            file_ext_name = (current_file[1], ('*'+current_file[1]))

        save_filename = filedialog.asksaveasfilename(initialdir=current_file_path, initialfile=current_file[0],
                                                     title='Save As', defaultextension=current_file[1],
                                                     filetypes=(file_ext_name, ('All files', '*.*')))
        if save_filename:
            os.rename(fr'{current_file_path}', fr'{save_filename}')
            current_file_path = save_filename
            current_file = os.path.splitext(os.path.basename(save_filename))
            master.title(f'{current_file[0]}-Encrypted')
            save_file()
    else:
        save_file()


def save_file():
    global saved, current_file, current_file_path
    save_check()
    if current_file:
        if not saved:
            file_object = open(current_file_path, 'w')
            file_object.write(myText.get(1.0, END))
            file_object.close()
            saved_position()
    else:
        save_filename = filedialog.asksaveasfilename(title='Save File', defaultextension='.txt', filetypes=files_ext)
        if save_filename:
            current_file_path = save_filename
            file_object = open(current_file_path, 'w')
            file_object.write(myText.get(1.0, END))
            file_object.close()
            current_file = os.path.splitext(os.path.basename(save_filename))
            master.title(f'{current_file[0]}-Encrypted')
            saved_position()


def rowandcolumn(event=None):
    global saved
    current_cursor = myText.index(INSERT).split(".")
    row_label.config(text=f'row: {current_cursor[0]}')
    column_label.config(text=f'column: {int(current_cursor[1])+1}')
    if event.state == 4 and event.keysym == 'o':
        open_file()
        return 'break'
    if event.state == 4 and event.keysym == 'n':
        new_file()
        return 'break'
    if event.state == 4 and event.keysym == 's':
        save_file()
        return 'break'
    if event.state == 5 and event.keysym == 'S':
        save_as_file()
        return 'break'


def check(event=None):
    global saved_content
    print(len(saved_content))
    print(len(myText.get(1.0, END)))
    print(myText.index(END))


def undo(event):
    try:
        print('undo')
        myText.edit_undo()
        return 'break'
    except TclError:
        try:
            print('redo')
            myText.edit_redo()
            return 'break'
        except TclError:
            pass


def select_all(event=None):
    myText.tag_add('sel',1.0, END)
    return "break"


def backspace(event):
    print('here')
    rowandcolumn(event)
    myText.edit_separator()


def search():
    start = 1.0
    while True:
        var = myText.search('hey',start, stopindex=END,count=True)
        if not var:
            print('here')
            break
        print(var)
        start = var + '+1c'


def paste():
    myText.event_generate('<<Paste>>')

    '''
    selected_text = master.clipboard_get()
    print(selected_text)
    myText.insert(INSERT, selected_text)
    '''


def cut():
    myText.event_generate('<<Cut>>')
    '''
    selected_text = myText.selection_get()
    myText.delete("sel.first", "sel.last")
    master.clipboard_clear()
    master.clipboard_append(selected_text)
    '''


def copy():
    myText.event_generate('<<Copy>>')
    '''
    selected_text = myText.selection_get()
    master.clipboard_clear()
    master.clipboard_append(selected_text)
    '''


def redo(event):
    try:
        print('bitch')
        myText.edit_redo()
        return 'break'
    except TclError:
        pass


def wrap():
    if wrap_value.get():
        myText.config(wrap=WORD)
        horizontal_scroll.pack_forget()
    else:
        myText.config(wrap=NONE)
        horizontal_scroll.pack(side=BOTTOM, fill=X)


def position(event):
    print(event)
    myText.mark_set('insert', "@%d,%d" % (event.x, event.y))
    current_cursor = myText.index(INSERT).split(".")
    row_label.config(text=f'row: {current_cursor[0]}')
    column_label.config(text=f'column: {int(current_cursor[1]) + 1}')


def save_check():
    global saved_content, saved
    print(myText.index(END))
    check_content = myText.get(1.0, END)
    if check_content == saved_content:
        saved = True
    else:
        saved = False


def onclose():
    save_check()
    if not saved:
        answer = messagebox.askyesnocancel(parent=master, title='Encrypted',
                                           message=f'Do you want to save changes to {current_file[0] if current_file else "untitled"}')
        if answer:
            if current_file:
                save_file()
                master.destroy()
            else:
                save_file()
        elif answer is None:
            pass
        else:
            master.destroy()
    else:
        master.destroy()


def editmenu_post():
    try:
        if myText.selection_get():
            editmenu.entryconfig(0, state=NORMAL)
            editmenu.entryconfig(1, state=NORMAL)
    except:
        editmenu.entryconfig(0, state=DISABLED)
        editmenu.entryconfig(1, state=DISABLED)

def find():
    obj = Find(master,myText)


def replace():
    obj=Replace(master,myText)

menubar = Menu(master)
master.config(menu=menubar)
# filemenu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New playlist", accelerator="Ctrl+N", command=new_file)
filemenu.add_command(label="Open file", accelerator='Ctrl+O', command=open_file)
filemenu.add_command(label="Save", accelerator='Ctrl+S', command=save_file)
filemenu.add_command(label="Save as...", accelerator='Ctrl+Shift+S', command=save_as_file)
filemenu.add_command(label="Close", command='')
filemenu.add_separator()
filemenu.add_command(label="Exit", command=onclose)

# editmenu
editmenu = Menu(menubar, tearoff=0,postcommand=editmenu_post)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_separator()
editmenu.add_command(label="Select All", command=select_all, accelerator='Ctrl-A')
editmenu.add_separator()
editmenu.add_command(label="Find", command=find, accelerator='Ctrl-F')
editmenu.add_command(label='Replace', command=replace, accelerator='Ctrl-R')

# editmenu.add_command(label="Paste")

# optionmenu
optionmenu = Menu(menubar, tearoff=0 )
menubar.add_cascade(label="Option", menu=optionmenu)
optionmenu.add_checkbutton(label="Wrap", onvalue=1, offvalue=0, variable=wrap_value, command=wrap)
# optionmenu.add_command(label="Pause",image=pause_option,compound=LEFT)
optionmenu.add_command(label='Font', image='', compound=LEFT, command=lambda:configure(master, master.winfo_x(),
                                                                                       master.winfo_y(),default_font))

# Help
helpmenu = Menu(menubar, tearoff=0, )
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About us", command=search)
# status_bar
status_bar = Frame(master, height=15, relief=RIDGE, bd=1)
status_bar.pack(side=BOTTOM, fill=X)
column_label = Label(status_bar, text='column: 1', width=35, anchor=W, relief=RIDGE, bd=1)
column_label.pack(side=RIGHT)
row_label = Label(status_bar, text='row: 1', width=35, anchor=W, relief=RIDGE, bd=1)
row_label.pack(side=RIGHT)
horizontal_scroll = Scrollbar(master, orient=HORIZONTAL)
horizontal_scroll.pack(side=BOTTOM, fill=X)
vertical_scroll = Scrollbar(master)
vertical_scroll.pack(side=RIGHT, fill=Y)
myText = Text(master, xscrollcommand=horizontal_scroll.set, yscrollcommand=vertical_scroll.set, height=1, width=1,
              wrap=NONE, undo=True, font=default_font)
myText.bind('<Control-z>', undo)
myText.bind('<Control-a>', select_all)
myText.bind('<Control-Shift-Z>', redo)
myText.bind('<BackSpace>', backspace)
myText.focus_set()
myText.pack(fill=BOTH, expand=True)
vertical_scroll.config(command=myText.yview)
horizontal_scroll.config(command=myText.xview)
myText.bind('<KeyRelease>', rowandcolumn)
myText.bind('<KeyPress>', rowandcolumn)
myText.bind('<ButtonPress>', position)
master.protocol("WM_DELETE_WINDOW", onclose)
saved_content = myText.get(1.0, END)
height = int(master.winfo_screenheight()*0.5)
width = int(master.winfo_screenwidth()*0.5)
master.title('untitled-Encrypted')
master.geometry(f'{width}x{height}+20+20')
if len(sys.argv) >= 2:
    open_file_internal(sys.argv[1])
master.mainloop()