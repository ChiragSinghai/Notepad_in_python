import os
from filemanager import createFolder,path

def setFont(fontname,size,font,slant):
    filename = path+"fontdata.txt"
    if(os.path.isfile(filename)):
        file=open(filename,'w')
        file.write(fontname+"\n")
        file.write(str(size)+"\n")
        file.write(str(font)+'\n')
        file.write(str(slant)+'\n')
        file.close()   
    else:
        createFolder()
        file = open(filename,'x')
        file.close()
        setFont(fontname)


def getFont():
    filename = path + "fontdata.txt"
    if(os.path.isfile(filename)):
        file=open(filename,'r')
        fontandsize=file.readlines()
        i=0
        for line in fontandsize:
            fontandsize[i]=line.strip()
            i+=1
        file.close()
        return fontandsize
    else:
        createFolder()
        file = open(filename,'x')
        file.write('Arial'+'\n')
        file.write('18'+'\n')
        file.write('0'+'\n')
        file.write('0'+'\n')
        file.close()
        var = getFont()
        return var


if __name__ == '__main__':
    getFont()
    setFont('Jokerman',14,1,0)
    getFont()
