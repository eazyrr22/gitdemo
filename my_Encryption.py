from os import close
from sys import dllhandle


class Encryption:
    def bytewise_xor(self,text):
        xorer = 5
        return ''.join(chr(ord(char) ^ xorer) for char in text)

    def decryped(self,text):
        decrypted = self.bytewise_xor(text)
        print(decrypted)

a = Encryption()
# ההצפנה !
with open("decripteddata.txt",'w') as f:
    f.write(a.bytewise_xor(open("keydata.txt").read()))
# פיענוח ההצפנה
with open("keydata.txt",'w') as file:
    file.write(a.bytewise_xor(open("decripteddata.txt").read()))


