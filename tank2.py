# Authors: Fatma Nur Arabaci & Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time
import socket

################ WEBSOCKET receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost',7776))

################ WEBSOCKET sender
addr = ("localhost",7777)
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

################ MQTT
broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 2 Publisher")
publisher_client.connect(broker_address)

'''
def h1_received(client,userdata,message):
    tank2.h1 = float(message.payload.decode("utf-8"))
    print("received Tank 1 h1: " + str(tank2.h1))

listener_client = mqtt.Client("Tank 2 listener")
listener_client.on_message = h1_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/heights/h1")
'''

# Tank dynamics
def tank2():
    ################ WEBSOCKET receiver
    data, addr = sock.recvfrom(1024)
    print ("received  websocket message: ", data.decode())
    tank2.h1 = float(data)#.decode()

    tank2.h2 = tank2.h1 + 0.10
    publisher_client.publish("Tanks/heights/h2",tank2.h2)
    print("MQTT is sending Tank 2 h2: " + str(tank2.h2))

    ################ WEBSOCKET sender
    data = str(tank2.h2)
    if(UDPSock.sendto(data.encode(),addr)):
        print('Websocket is sending: ' + data)

# Tank parameters
tank2.h1 = 0
tank2.h2 = 0

while True:
    tank2()
    time.sleep(0.05)
