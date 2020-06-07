# Authors: Fatma Nur Arabaci & Gerardo Sánchez
# Date created: May 28, 2020

import paho.mqtt.client as mqtt
import time
import socket

################ WEBSOCKET
addr = ("localhost",7776)
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDPSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

################ MQTT
broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 1 Publisher")
publisher_client.connect(broker_address)

def q_received(client,userdata,message):
    tank1.q = float(message.payload.decode("utf-8"))
    print("MQTT received flow q: " + str(tank1.q))

listener_client = mqtt.Client("Tank 1 listener")
listener_client.on_message = q_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/flows/q")

# Tank dynamics
def tank1():
    tank1.h1 = tank1.q + 1.00
    publisher_client.publish("Tanks/heights/h1",tank1.h1)
    print("MQTT is sending Tank 1 h1: " + str(tank1.h1))

    ################ WEBSOCKET
    data = str(tank1.h1)
    if(UDPSock.sendto(data.encode(),addr)):
        print('Websocket is sending: ' + data)

# Tank parameters
tank1.q = 0
tank1.h1 = 0

while True:
    tank1()
    time.sleep(0.05)
