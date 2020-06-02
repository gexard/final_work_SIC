# Authors: Fatma Nur & Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 2 Publisher")
publisher_client.connect(broker_address)

def h1_received(client,userdata,message):
    tank2.h1 = float(message.payload.decode("utf-8"))
    print("received Tank 1 h1: " + str(tank2.h1))

listener_client = mqtt.Client("Tank 2 listener")
listener_client.on_message = h1_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tanks/heights/h1")

# Tank dynamics
def tank2():
    tank2.h2 = tank2.h1 + 0.10
    publisher_client.publish("Tanks/heights/h2",tank2.h2)
    print("sending Tank 2 h2: " + str(tank2.h2))

# Tank parameters
tank2.h1 = 0
tank2.h2 = 0

while True:
    tank2()
    time.sleep(0.05)
