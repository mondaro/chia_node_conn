#[MONTECH][inc_module][ver.1.1.e][212905]
import time
import urllib.request
from urllib.request import urlopen, Request
from datetime import datetime
import re
import os
import sys, subprocess
import pathlib
from tkinter import Tk
import pyperclip

FILE_STORE_NODE_CMD = "chia_node_bloom.txt"
FILE_PATH_DAEMON = "path.txt"

def synctime():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y-%H:%M:%S")
    return date_time

def get_node_conn():
    try:
        HEADER_IP = []
        response = urllib.request.urlopen("https://chia.keva.app/")
        htmlBytes = response.read()
        htmlStr = htmlBytes.decode("utf8")
        get_IP_Addr = re.findall(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', htmlStr, re.MULTILINE)
        
        for lines in get_IP_Addr:
            mask_data = lines.split(',')
            HEADER_IP.append('./chia show -a ' + mask_data[0]+':8444')  
        try:          
            with open(FILE_STORE_NODE_CMD,'w') as file_store:
                for i in HEADER_IP:
                    file_store.write(i + '\n')
                file_store.truncate()
                file_store.close()
                print(synctime()," [chia_node_conn] Create node file completed.")
        except:
            print(synctime()," [chia_node_conn] **Error** create node file!!!")  
    except:
        print(synctime()," [chia_node_conn] **Error** get http-request!!!")

def do_action_powershell():
    try:
        with open(FILE_PATH_DAEMON,'r') as path_chia_deamon:
            path = path_chia_deamon.read()
            path = path.replace("/","\\")
            path_chia_deamon.close()
        
        with open(FILE_PATH_DAEMON,'w') as optimal_path:
            optimal_path.write(path)
            optimal_path.truncate()
            optimal_path.close()

        try:
            with open(FILE_STORE_NODE_CMD,'r') as clp_node:
                clp_node_txt = clp_node.read()
                clp_node.close()
                pyperclip.copy(clp_node_txt)

            #----FIX HERE ----  
            os.system('start /D "'+ path +'" powershell')
            #os.system("start /D C:\\Users\\uppat\\AppData\\Local\\chia-blockchain\\app-1.1.6\\resources\\app.asar.unpacked\\daemon powershell")
            #os.system('start /D "'+ path +'" powershell Get-Clipboard -Raw')
            
            print(synctime()," [chia_node_conn]  UPDATE node completed.")
            print(synctime()," [Hosting]-[chia.keve.app] syncing...")
        except:
            print(synctime()," [chia_node_conn]  **Error** PowerShell illegal execute command")
            
    except:
        print(synctime()," [chia_node_conn] **Error** Chia daemon path missmatch!!!")
