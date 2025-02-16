def bytewise_xor(text):
    xorer = 5
    return ''.join(chr(ord(char) ^ xorer) for char in text)

