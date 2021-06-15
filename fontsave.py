import os
def setFont(fontname,size,font):
    if(os.path.isfile("folder/fontdata.txt")):
        file=open("folder/fontdata.txt",'w')
        file.write(fontname+"\n")
        file.write(str(size)+"\n")
        file.write(str(font)+'\n')
        #file.write(str(slant)+'\n')
        file.close()   
    else:
        os.mkdir("folder")
        file = open("folder/fontdata.txt",'x')
        file.close()
        setFont(fontname)


def getFont():
    if(os.path.isfile("folder/fontdata.txt")):        
        file=open("folder/fontdata.txt",'r')
        fontandsize=file.readlines()
        i=0
        for line in fontandsize:
            fontandsize[i]=line.strip()
            i+=1
        file.close()
        return fontandsize
    else:
        os.mkdir("folder")
        file=open("folder/fontdata.txt",'x')
        file.write('Arial'+'\n')
        file.write('18'+'\n')
        file.write('0'+'\n')
        #file.write('0'+'\n')
        file.close()
        var = getFont()
        return var


if __name__ == '__main__':
    getFont()
    setFont('Jokerman',14,1)
    getFont()
