#***************************************************************
#This code publish a message using Paho
#Source:https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

#Author: Federico G. D'Angiolo
#***************************************************************

from paho.mqtt import client as mqtt_client
import argparse
import random
import time


def run(client_id, broker, port, topic, msg):
    """
    This function call to the three functions:
    connecto_mqtt(): define ths MQTT client
    loop_start(): loop for
    publish: publish the data

    Arguments:
    client_id: client_id defined
    broker: defined by the user. Default: broker.emqx.io 
    port: defined by th user. Default: 1883
    topic: topic for publish
    msg: message to sending
    
    Return: nothing
    """

    client = connect_mqtt(client_id, broker, port)
    publish(client, topic, msg)


def connect_mqtt(client_id, broker, port):
    """
    Connect the client to the broker, using the port.

    Arguments: 
    client_id: id for the client
    broker: broker for send the message
    port: port refered to the broker
    """

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_connect(rc):
    """
    Verify for possible errors
    """
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def publish(client, topic, msg):
    """
    Publish the msg

    Arguments:
    client: client generated.
    topic: topic for MQTT message.
    msg: message for send.
    """
    
    while True:
        time.sleep(1)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")


#For CLI

#Data processing
parser = argparse.ArgumentParser(description='Mqtt connection')
parser.add_argument('--broker', type=str, default = "broker.emqx.io", help='Select the broker')
parser.add_argument('--port', type=int, default = 1883, help='Port used by the broker')
parser.add_argument('--topic', type=str, default = "send_msg", help='Topic for message')
parser.add_argument('--msg', type=str, default = "hello world", help='Message sending')

args = parser.parse_args()

if __name__ == '__main__':

    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    #Run ths script
    run(client_id, args.broker, args.port, args.topic, args.msg)
