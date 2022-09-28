#***************************************************************
#This code publish a message using Paho
#Source:https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
#Documentation: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php
#***************************************************************
import time
import argparse
import random
from paho.mqtt import client as mqtt_client


def run(client_id, topic):
    """
    This function call to others three functions:
    connecto_mqtt(): define ths MQTT client.
    subscribe: receive the data.
    client.loop_forever(): This is a blocking form of the network loop and will not return until the client calls disconnect()

    Arguments:
    client_id: client_id defined
    broker: defined by the user. Default: broker.emqx.io 
    port: defined by th user. Default: 1883
    topic: topic for subscribe
    
    Return: nothing
    """

    broker = "broker.emqx.io"
    port = 1883

    client = connect_mqtt(client_id, broker, port)
    subscribe(client, topic)
    client.loop_forever()


def connect_mqtt(client_id, broker, port):
    """
    Connect the client to the broker, using the port.

    Arguments: 
    client_id: id for the client
    broker: broker for send the message
    port: port refered to the broker
    """

    client = mqtt_client.Client(client_id)
    client.connect(broker, port)
    return client

def subscribe(client, topic):
    """
    Subscribe to a topic for listen a message. Use the on_message function for callback function
    
    Arguments:
    client: client mqtt
    topic: topic where subscribe
    """
    client.subscribe(topic)
    client.on_message = on_message


def on_message(client, userdata, msg):
    """
    on_message is a callback function. This function will be called after the client receives messages from the MQTT Broker.
    """
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


#For CLI

#Data processing
parser = argparse.ArgumentParser(description='Mqtt connection')
parser.add_argument('--topic', type=str, default = "recive_msg", help='Topic for message')

args = parser.parse_args()

if __name__ == '__main__':

    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    #Run ths script
    run(client_id, args.topic)
