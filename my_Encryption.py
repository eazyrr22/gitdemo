from os import close
from sys import dllhandle


def bytewise_xor(text):
    encrytion_key = 5
    return ''.join(chr(ord(char) ^ encrytion_key) for char in text)






