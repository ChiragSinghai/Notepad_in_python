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
    XOR_value=randint(1,100)
    key += str(XOR_value)
    #print(key)
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
    XOR_value = int(key[n+1:])
    S = ''
    for i in range(len(alphabet)):
        char = shifted[i]
        char = chr(ord(char) ^ XOR_value)
        S += char
    encryptdict = {}
    #print(S)

    for k,v in zip(alphabet,S):
        encryptdict[k] = v
    return encryptdict



def encrypt(text):
    key = getKey()
    endict = getdict(key)
    text = list(text)
    #print(text)
    for i in range(len(text)):
        if text[i] in endict:
            text[i]=endict[text[i]]
    #print(endict)
    return ''.join(text),key


def getDecryptDict(key):
    alphabet = string.ascii_letters + string.digits + string.punctuation +string.whitespace
    #alphabet = alphabet.replace(" ", "")
    #print(len(alphabet))
    shifted = alphabet

    m = int(key[0])
    for i in range(1, m + 1):
        shift = int(key[i])
        shifted = shifted[shift:] + shifted[:shift]

    XOR_value = int(key[m + 1:])
    S = ''
    for i in range(len(alphabet)):
        char = shifted[i]
        char = chr(ord(char) ^ XOR_value)
        S += char
    decryptdict = {}


    for k, v in zip(S,alphabet):
        decryptdict[k] = v
    #print(decryptdict)
    return decryptdict

def decrypt(text,key):
    dedict = getDecryptDict(key)
    text = list(text)
    #print(text)
    for i in range(len(text)):
        if text[i] in dedict:
            text[i] = dedict[text[i]]
    #print(endict)
    return ''.join(text)

if __name__=='__main__':
    text,key = encrypt('hello world 45@12')
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
