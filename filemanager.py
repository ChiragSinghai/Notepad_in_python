import os
from tkinter import *
path = 'P://Encrypted//'
def createFolder():
    if os.path.isdir(path):
        return
    else:
        os.mkdir('P://Encrypted')
def getsize(master):
    createFolder()
    #print(path)
    if not(os.path.isfile(path+'size.txt')):
        file = open(path+'size.txt','w')
        file.write(str(master.winfo_screenheight()//2)+'\n')
        file.write(str(master.winfo_screenwidth()//2)+'\n')
        file.write('10'+'\n')
        file.write('10'+'\n')
        file.close()
    filename = path+'size.txt'
    file = open(filename,'r')
    height,width,X,Y = map(int,file.readlines())
    file.close()
    return height,width,X,Y

def setsize(master):
    createFolder()
    filename = path + 'size.txt'
    file = open(filename, 'w')
    file.write(str(min(master.winfo_screenheight()//2,master.winfo_height()))+'\n')
    file.write(str(min(master.winfo_width(),master.winfo_screenwidth()//2))+'\n')
    file.write(str(master.winfo_x())+'\n')
    file.write(str(master.winfo_y())+'\n')
    file.close()
    if not(os.path.isfile(filename)):
        file = open(filename,'x')
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