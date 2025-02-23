from os import close
from sys import dllhandle


class Encryption:
    def __init__(self,xor_key):
        self.xor_key = int(xor_key)
    def bitwise_xor_encryption(self,text):
            xored =  ''.join(chr(ord(char) ^ self.xor_key) for char in text)
            print(xored)
            return xored

    def encryption_discovery(self,text):
        decrypted = self.bitwise_xor_encryption(text)
        # print(decrypted)
        return decrypted

a = Encryption(5)

def nativ(parameter):
    parameter = str(parameter)
    path = parameter.split("\\")
    return path[-1]

def opening(parameter,xor_key):
    parameter = nativ(parameter)
    with open(f"{parameter}",'r') as file:
        b = Encryption(xor_key)
        print(b.encryption_discovery(file.readline()))


a = Encryption(5)
c = a.bitwise_xor_encryption("yeshaya david teller")
a.encryption_discovery(c)







