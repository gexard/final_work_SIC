# Authors: Fatma Nur & Gerardo Sánchez
# Date created: May 30, 2020

import paho.mqtt.client as mqtt
import time

broker_address = "127.0.0.1"
publisher_client = mqtt.Client("Tank 3 Publisher")
publisher_client.connect(broker_address)

def q_received(client,userdata,message):
    tank3.h2 = float(message.payload.decode("utf-8"))

listener_client = mqtt.Client("Tank 3 listener")
listener_client.on_message = q_received
listener_client.connect(broker_address)
listener_client.loop_start()

listener_client.subscribe("Tank2/h2")

# Tank dynamics
def tank1():
    tank3.h2 = #
    tank3.h3 = #
    publisher_client.publish("Tank3/h3",tank3.h3)

# Tank parameters
tank3.h2 = 0
tank3.h3 = 0

while True:
    tank3()
    time.sleep(0.05)
