#[MONTECH][chia_node_conn][ver.1.7.b][212905]
"""
Please ReadMe before!!
support me to donate at
CHIA: xch1ek3yvx9yyspgdwh60hf3q09xjdh9xaqkrfm5tm69cu5j4y6exw0qd8alxr
BSC: 0xd816E919AA8A93d84B337D137301eF27ead44f42
"""
import urllib.request
from urllib.request import urlopen, Request
import time
import hashlib
from datetime import datetime
import re
import os
import pathlib
from tkinter import Tk
from inc_module import synctime, get_node_conn, do_action_powershell

TIME_SLEEP = 180

def conn_request(url):
    response = urllib.request.urlopen(url)
    htmlBytes = response.read()
    return htmlBytes

# Initial_state
print(synctime()," [chia_node_conn] Init system.")

# Start_state 
try:
    print(synctime()," [chia_node_conn] running...")
    currentHash = hashlib.sha224(conn_request("https://chia.keva.app/")).hexdigest()
    print(synctime()," [Hosting]-[chia.keve.app] syncing...")
    get_node_conn()
    do_action_powershell()
    time.sleep(10)
    while True:
        try:
            currentHash = hashlib.sha224(conn_request("https://chia.keva.app/")).hexdigest()
            time.sleep(TIME_SLEEP)
            newHash = hashlib.sha224(conn_request("https://chia.keva.app/")).hexdigest()
            if newHash == currentHash:
                print(synctime()," [Hosting] IP node as a whole remains the same")
                continue
            else:
                # notify
                print(synctime()," [Hosting] IP Node was changed")
                get_node_conn()
                time.sleep(10)
                do_action_powershell()
                continue
        except Exception as e:
            print(synctime()," [Hash] **Error** check hash HTML-Request")
except:
    print(synctime()," [Hosting] Hosting down!!!")
