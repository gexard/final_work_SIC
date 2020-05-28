# Authors: Fatma Nur & Gerardo Sánchez
# Date created: May 28, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 1 Publisher")
publisher_client.connect(broker_address)

def q_received(client,userdata,message):
    tank1.q = float(message.payload.decode("utf-8"))

listener_client = mqtt.Client("Tank 1 listener")
listener_client.on_message = q_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tank1/q")

# Tank dynamics
def tank1():
    tank1.q = #
    tank1.h1 = #

publisher_client.publish("Tank1/h1",h1)

# Tank parameters
tank1.q = 0
tank1.h1 = 0

while True:
    tank1()
    time.sleep(0.05)
