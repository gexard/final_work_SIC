# Authors: Fatma Nur Arabaci & Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time
import socket

################ WEBSOCKET receiver
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost',7777))

################ WEBSOCKET sender
broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 3 Publisher")
publisher_client.connect(broker_address)

def on_message(client,userdata,message):
    if message.topic == "Tanks/constants/a":
        tank3.a = float(message.payload.decode("utf-8"))
        #print("MQTT received constant a: " + str(tank3.a))
    if message.topic == "Tanks/constants/A":
        tank3.A = float(message.payload.decode("utf-8"))
        #print("MQTT received constant a: " + str(tank3.A))

listener_client = mqtt.Client("Tank 3 listener")
listener_client.on_message = on_message
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/constants/+")

# Tank dynamics
def tank3():
    ################ WEBSOCKET receiver
    data, addr = sock.recvfrom(1024)
    print ("received  websocket message: ", data.decode())
    tank3.h2 = float(data)#.decode()

    tank3.h3 = tank3.h2 + 0.01
    publisher_client.publish("Tanks/heights/h3",tank3.h3)
    #print("MQTT is sending Tank 3 h3: " + str(tank3.h3))

# Tank parameters
tank3.h2 = 0
tank3.h3 = 0
tank3.a = 0.00013104
tank3.A = 0.03

while True:
    tank3()
    time.sleep(0.05)
