# Authors: Fatma Nur & Gerardo Sánchez
# Date created: May 28, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 1 Publisher")
publisher_client.connect(broker_address)

def q_received(client,userdata,message):
    tank1.q = float(message.payload.decode("utf-8"))
    print("received flow q: " + str(tank1.q))

listener_client = mqtt.Client("Tank 1 listener")
listener_client.on_message = q_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tank1/q")

# Tank dynamics
def tank1():
    tank1.h = tank1.q + 0.001
    publisher_client.publish("Tank1/h1",tank1.h1)
    print("sending Tank 1 h1: " + str(tank1.h))

# Tank parameters
tank1.q = 0
tank1.h1 = 1

while True:
    tank1()
    time.sleep(0.05)
