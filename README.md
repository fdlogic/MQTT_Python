# Send message with Paho
Simple python script that send message thorugh MQTT with Paho.


### Prerequisites 
For this example, use the provided requirements file to get the same version for paho-mqtt.

```
pip install -r requirements.txt
```

## Usage
For see the documentation, execute: python MQTT_communication.py -h

Usage 

```
usage: send_data.py [-h] [--broker BROKER] [--port PORT] [--topic TOPIC]
                    [--msg MSG]

Mqtt connection

optional arguments:
  -h, --help       show this help message and exit
  --broker BROKER  Select the broker
  --port PORT      Port used by the broker
  --topic TOPIC    Topic for message
  --msg MSG        Message sending

```

### Example 
This example publish the message "ON", in the topic "light", using the broker "broker.emqx.io" by default. If you want to change the broker, use --broker.

```
python send_data.py --topic light --msg "ON"
```

If you don't use the options, the script send a message and topic by deafult. The next example send a message "Hello world" in the topic "send_msg". The broker by default is "broker.emqx.io". If you want to change the broker, use the option --broker.

```
python MQTT_communication.py
```


