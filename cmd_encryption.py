from os import close
from sys import dllhandle


class Encryption:
    def __init__(self,xor_key):
        self.xor_key = int(xor_key)
    def bitwise_xor_encryption(self,text):
            return ''.join(chr(ord(char) ^ self.xor_key) for char in text)

    def encryption_discovery(self,text):
        decrypted = self.bitwise_xor_encryption(text)
        print(decrypted)

def nativ(parameter):
    parameter = str(parameter)
    path = parameter.split("\\")
    return path[-1]

def opening(parameter,xor_key):
    parameter = nativ(parameter)
    with open(parameter,'r') as file:
        b = Encryption(xor_key)
        print(b.encryption_discovery(file.readline()))



opening(str(input("enter path")),input("enter xor key"))







