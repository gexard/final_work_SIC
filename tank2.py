# Author: Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time
import socket

################ WEBSOCKET receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost',7776))

################ WEBSOCKET sender
sender_address = ("localhost",7777)
senderSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
senderSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

################ MQTT
broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 2 Publisher")
publisher_client.connect(broker_address)

def on_message(client,userdata,message):
    if message.topic == "Tanks/constants/a":
        tank2.a = float(message.payload.decode("utf-8"))
        #print("MQTT received constant a: " + str(tank2.a))
    if message.topic == "Tanks/constants/A":
        tank2.A = float(message.payload.decode("utf-8"))
        #print("MQTT received constant a: " + str(tank2.A))

listener_client = mqtt.Client("Tank 2 listener")
listener_client.on_message = on_message
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/constants/+")

# Tank dynamics
def tank2():
    ################ WEBSOCKET receiver
    data, addr = sock.recvfrom(1024)
    #print ("received  websocket message: ", data.decode())
    tank2.h1 = float(data)#.decode()

    tank2.h2 = tank2.h1 + 0.10
    publisher_client.publish("Tanks/heights/h2",tank2.h2)
    #print("MQTT is sending Tank 2 h2: " + str(tank2.h2))

    ################ WEBSOCKET sender
    data = str(tank2.h2)
    if(senderSock.sendto(data.encode(), sender_address)):
        #print('Websocket is sending: ' + data)

# Tank parameters
tank2.h1 = 0
tank2.h2 = 0
tank2.a = 0.00013104
tank2.A = 0.03

while True:
    tank2()
    time.sleep(0.05)
