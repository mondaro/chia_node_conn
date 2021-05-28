#[MONTECH][chia_node_conn][ver.1.6.b][280520]
"""
Please ReadMe before!!
support me to donate at
CHIA: xch1ek3yvx9yyspgdwh60hf3q09xjdh9xaqkrfm5tm69cu5j4y6exw0qd8alxr
BSC: 0xd816E919AA8A93d84B337D137301eF27ead44f42
"""
import urllib.request
import time
import hashlib
from urllib.request import urlopen, Request
from datetime import datetime
import re
import webbrowser
import os
import pathlib
import logging
from tkinter import Tk

FILE_STORE_NODE_CMD = "chia_node_bloom.txt"
FILE_PATH_DAEMON = "path.txt"
TIME_SLEEP = 180

def synctime():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return date_time

# Initial_state
print(synctime()," [chia_node_conn] Init system.")

# Http request
def conn_request(url):
    response = urllib.request.urlopen(url)
    htmlBytes = response.read()
    return htmlBytes

def get_node_conn():
    try:
        HEADER_IP = []
        htmlStr = conn_request("https://chia.keva.app/").decode("utf8")
        get_IP_Addr = re.findall(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', htmlStr, re.MULTILINE)
        #print(get_IP_Addr) #chk_get_ip
        # Make a chia command to add all node connection
        for lines in get_IP_Addr:
            mask_data = lines.split(',')
            HEADER_IP.append('./chia show -a ' + mask_data[0]+':8444')
        #print(HEADER_IP) #chk_append_cmd
        # Make file completed node list
        try:          
            with open(FILE_STORE_NODE_CMD,'r+') as file_store:
                data = file_store.read()
                file_store.seek(0)
                for i in HEADER_IP:
                    file_store.write(i + "\n")
                file_store.truncate()
                file_store.close()
            # Copy all text command to clipboard
            with open(FILE_STORE_NODE_CMD,'r') as clp_node:
                clp_node_txt = clp_node.read()         
                root = Tk()
                root.withdraw()
                root.clipboard_clear()
                root.clipboard_append(clp_node_txt)
                root.update()
                #root.destroy()
            clp_node.close()
            #print(clp_node_txt)
            # Open node command list as text file
            #webbrowser.open("chia_node_bloom.txt")
            print(synctime()," [chia_node_conn] Create node file completed.")
            
        except:
            print(synctime()," [chia_node_conn] **Error** create file!!!")  
    except:
        print(synctime()," [chia_node_conn] **Error** get request!!!")

def do_action_powershell():
    try:
        with open(FILE_PATH_DAEMON,'r') as path_chia_deamon:
            path = path_chia_deamon.read()
            #print(path)
            path = path.replace("\\","/")
            path_chia_deamon.close
            with open(FILE_PATH_DAEMON,'w+') as optimal_path:
                #print(path)
                optimal_path.write(path)
            root = Tk()
            root.withdraw()
            data = root.clipboard_get()
            root.clipboard_clear()
            root.clipboard_append(data)
            root.update()
            #print(data)
            os.system('start /D "'+ path +'" powershell')
            print(synctime()," [chia_node_conn]  UPDATE node completed.")
        optimal_path.close
    except:
        print(synctime()," [chia_node_conn] **Error** PowerShell!!!") 
    
try:
    print(synctime()," [chia_node_conn] running...")
    #logging.info('[chia_node_conn] running...')
    currentHash = hashlib.sha224(conn_request("https://chia.keva.app/")).hexdigest()
    print(synctime()," [Hosting]-[chia.keve.app] syncing...")
    get_node_conn()
    do_action_powershell()
    time.sleep(10)
    #response.close()
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
                do_action_powershell()
                currentHash = hashlib.sha224(conn_request("https://chia.keva.app/")).hexdigest()
                time.sleep(TIME_SLEEP)
                continue    
        # To handle exceptions
        except Exception as e:
            print(synctime()," [Hash] **Error** check hash HTML-Request")
    #print(htmlStr) #chk_html_pull
    # GET_IP_ADDR_PULL 
except:
    print(synctime()," [Hosting] Hosting down!!!")
