import random
import string
from random import randint,shuffle
def getKey():
    key = ''
    keylength = randint(2,5)
    key+=str(keylength)
    for _ in range(keylength):
        shift = randint(1,5)
        key += str(shift)
    #print(key)
    XOR_value=randint(1,31)
    key+=str(XOR_value)
    return key

def getdict(key):
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    #alphabet = alphabet.replace(" ","")
    #print(len(alphabet))
    shifted = alphabet
    n = int(key[0])
    for i in range(1,n+1):
        shift = int(key[i])
        shifted = shifted[shift:] + shifted[:shift]

    encryptdict = {}
    XOR_value = int(key[n + 1:])
    #print(XOR_value)
    for k,v in zip(alphabet,shifted):
        encryptdict[k] = v
    return encryptdict,XOR_value



def encrypt(text):
    key = getKey()
    endict,XOR_value = getdict(key)
    text = list(text)
    #print(text)
    #print(endict)
    for i in range(len(text)):
        if text[i] in endict:
            text[i] = endict[text[i]]
    #print(endict)
    text = ''.join(text)
    text = XOR(XOR_value, text)
    #print(text)
    return text,key

def getDecryptDict(key):
    m = int(key[0])
    XOR_value = int(key[m + 1:])
    #print(XOR_value)
    alphabet = string.ascii_letters + string.digits + string.punctuation +string.whitespace
    #alphabet = alphabet.replace(" ", "")
    #print(len(alphabet))
    shifted = alphabet


    for i in range(1, m + 1):
        shift = int(key[i])
        shifted = shifted[shift:] + shifted[:shift]

    decryptdict = {}


    for k, v in zip(shifted,alphabet):
        decryptdict[k] = v
    print(decryptdict)
    return decryptdict,XOR_value

def XOR(XOR_value,text):
    S = ''
    for i in range(len(text)):
        S += chr(ord(text[i]) ^ XOR_value)
    return S


def decrypt(text,key):
    dedict,XOR_value = getDecryptDict(key)
    text = XOR(XOR_value, text)
    text = list(text)
    #print(text)
    for i in range(len(text)):
        if text[i] in dedict:
            text[i] = dedict[text[i]]
    text = ''.join(text)

    return text

if __name__=='__main__':
    '''
    with open('P:\\College\\position_salaries.csv') as f:
        txt = f.read()
    print(txt)
    '''
    text,key = encrypt('hey bitch this is encoding')
    print(decrypt(text,key))
    '''
    alphabet = string.ascii_letters + string.digits + string.punctuation
    print(alphabet)
    print(len(alphabet))
    S=alphabet
    S=S[7:]+S[:7]
    print(S)
    S=S[94-7:]+S[:94-7]
    print(S)
    char='j'
    char = chr(ord(char) ^ 50)
    print(char)
    char = chr(ord(char) ^ 50)
    print(char)
    '''
    #print(string.whitespace)
