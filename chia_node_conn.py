#[MONTECH][chia_node_conn][ver.1.5.e][260520]
"""
Please ReadMe before!!
support me to donate at
CHIA: xch1ek3yvx9yyspgdwh60hf3q09xjdh9xaqkrfm5tm69cu5j4y6exw0qd8alxr
BSC: 0xd816E919AA8A93d84B337D137301eF27ead44f42
"""
import urllib.request
import re
import webbrowser
import os
import pathlib
from tkinter import Tk
header_ip = []
#Http request
try:
    response = urllib.request.urlopen("https://chia.keva.app/")
    htmlBytes = response.read()
    response.close()
    htmlStr = htmlBytes.decode("utf8")
    #print(htmlStr) #chk_html_pull
    #GET_IP_ADDR_PULL
    try:
        get_IP_Addr = re.findall(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', htmlStr, re.MULTILINE)
        #print(get_IP_Addr) #chk_get_ip
        #Make a chia command to add all node connection
        for lines in get_IP_Addr:
            mask_data = lines.split(',')
            header_ip.append('./chia show -a ' + mask_data[0]+':8444')
        #print(header_ip) #chk_append_cmd
        #Make file completed node list
        try:          
            with open("chia_node_bloom.txt","w") as f:
                for i in header_ip:
                    f.write(i + "\n")
            f.close()
            #Copy all text command to clipboard
            with open("chia_node_bloom.txt","r+") as clp_node:
                clp_node_txt = clp_node.read()         
                r = Tk()
                r.withdraw()
                r.clipboard_clear()
                r.clipboard_append(clp_node_txt)
                r.update()
                r.destroy()
            clp_node.close()
            #Open node command list as text file
            #webbrowser.open("chia_node_bloom.txt")
        except:
            print("Error create file!!!")  
    except:
        print("Error get request!!!") 
except:
    print("Hosting down!!!")
try:
    with open("path.txt","r") as path_chia_deamon:
        path = path_chia_deamon.read()
        #print(path)
        path = path.replace("\\","/")
        path_chia_deamon.close
        with open("path.txt","w") as optimal_path:
            #print(path)
            optimal_path.write(path)
            os.system('start /D "'+ path +'" powershell')
    optimal_path.close
except:
    print("Error get path!!!") 
