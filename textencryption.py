import string
from random import randint

def getKey():
    key = ''
    keylength = randint(5,10)
    key+=str(keylength)
    for i in range(keylength):
        pass

def encrypt(text):
    key=getKey()



if __name__=='__main__':
    encrypt('Hello world')