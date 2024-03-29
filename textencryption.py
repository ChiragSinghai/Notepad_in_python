#import random
from string import ascii_letters,digits,whitespace,punctuation
from random import randint


def getKey(*ranges):
    key = ''
    keylength = randint(2,5)
    key += str(keylength)
    for _ in range(keylength):
        shift = randint(1,5)
        key += str(shift)
    #print(key)
    XOR_value = randint(1,31)
    key += str(XOR_value)
    if len(ranges) != 0:
        start,end = ranges[0],ranges[1]
        key='1'+key+' '+str(start)+' '+str(end)
    else:
        key='0'+key
    return key


def getdict(key):
    alphabet = ascii_letters + digits + punctuation + whitespace
    #alphabet = alphabet.replace(" ","")
    #print(len(alphabet))
    #print(bool(key[0]))
    if bool(int(key[0])):
        key,start,end = key.split(' ')
    #print(key)
    shifted = alphabet
    n = int(key[1])
    for i in range(2,n+2):
        shift = int(key[i])
        shifted = shifted[shift:] + shifted[:shift]

    encryptdict = {}
    XOR_value = int(key[n + 2:])
    #print(XOR_value)
    for k,v in zip(alphabet,shifted):
        if k=='\n' or v=='\n':
            encryptdict[k] = k
        else:
            encryptdict[k] = v
    return encryptdict,XOR_value


def encrypt(text,ranges=False):
    if not ranges:
        key = getKey()
    else:
        key = getKey(*ranges)
    endict,XOR_value = getdict(key)
    text = list(text)
    #print(XOR_value)
    #print(text)
    #print(endict['{'])
    for i in range(len(text)):
        if text[i] in endict:
            text[i] = endict[text[i]]
    #print(endict)
    text = ''.join(text)
    text = XOR(XOR_value, text)
    #print(text)
    return text,key

def getDecryptDict(key):

    m = int(key[1])
    XOR_value = int(key[m + 2:])
    #print(XOR_value)
    alphabet = ascii_letters + digits + punctuation +whitespace
    #alphabet = alphabet.replace(" ", "")
    #print(len(alphabet))
    shifted = alphabet


    for i in range(2, m + 2):
        shift = int(key[i])
        shifted = shifted[shift:] + shifted[:shift]

    decryptdict = {}


    for k, v in zip(shifted,alphabet):
        if k == '\n' or v == '\n':
            decryptdict[v] = v
        else:
            decryptdict[k] = v
    return decryptdict,XOR_value

def XOR(XOR_value,text):
    S = ''
    for i in range(len(text)):
        if text[i]=='\n':
            #print('hey')
            S+=text[i]
        else:
            char = chr(ord(text[i]) ^ XOR_value)
            if char != '\n':
                S += char
            else:
                S+=text[i]
    #print(S)
    return S


def decrypt(text,key):
    dedict,XOR_value = getDecryptDict(key)
    text = XOR(XOR_value, text)
    text = list(text)
    #print(text)
    #print(dedict[' '])
    for i in range(len(text)):
        if text[i] in dedict:
            text[i] = dedict[text[i]]
    #print(text)
    text = ''.join(text)

    return text

if __name__=='__main__':

    text,key = encrypt(digits+ascii_letters+punctuation+whitespace)
    print(decrypt(text,key))
