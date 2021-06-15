import os
from tkinter import *
def createFolder():
    if os.path.isdir('C://Encrypted/'):
        return
    else:
        os.mkdir('C://Encrypted')
def getsize(master):
    createFolder()
    if not(os.path.isfile('C://Encrypted//size.txt')):
        file = open('C://Encrypted//size.txt','w')
        file.write(str(master.winfo_screenheight()//2)+'\n')
        file.write(str(master.winfo_screenwidth()//2)+'\n')
        file.write('10'+'\n')
        file.write('10'+'\n')
        file.close()
    file = open('C://Encrypted//size.txt','r')
    height,width,X,Y = map(int,file.readlines())
    file.close()
    return height,width,X,Y

def setsize(master):
    createFolder()
    file = open('C://Encrypted//size.txt', 'w')
    file.write(str(master.winfo_height())+'\n')
    file.write(str(master.winfo_width())+'\n')
    file.write(str(master.winfo_x())+'\n')
    file.write(str(master.winfo_y())+'\n')
    file.close()
    if not(os.path.isfile('C://Encrypted//size.txt')):
        file = open('C://Encrypted//size.txt','x')
        file.write(str(master.winfo_screenheight())+'\n')
        file.write(str(master.winfo_screenwidth())+'\n')
        file.close()

if __name__=='__main__':
    root = Tk()
    h,w,x,y = getsize(root)
    root.geometry(f'{w}x{h}+{x}+{y}')
    def fun():
        setsize(root)

    button=Button(root,text='Press',command=fun)
    button.pack()
    root.mainloop()