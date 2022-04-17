# Pinger
# First Project !

import platform
import subprocess
import threading
import requests
import time


def Ping():
    while True:

        IP = "http://Google.com"
        PORT = "9100"


        request = requests.get(IP, PORT)
        print(request.status_code)
        if request.status_code == 200:
            print("Success!")
        elif request.status_code == 429:
            print("Cooldown!")
            time.sleep(10)

threads = []
for i in range(100):
    t = threading.Thread(target=Ping)
    threads.append(t)
    t.start()
