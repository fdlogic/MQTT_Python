# Send message with Paho
Simple python scripts that publish and subscribe in topics, through MQTT with Paho.


### Prerequisites 
For this example, use the provided requirements file to get the same version for paho-mqtt.

```
pip install -r requirements.txt
```

## Usage
For __publish__, execute: python send_data.py -h

Usage 

```
python send_data.py -h
usage: send_data.py [-h] [--topic TOPIC] [--msg MSG]

Mqtt connection

optional arguments:
  -h, --help     show this help message and exit
  --topic TOPIC  Topic for message
  --msg MSG      Message sending
```

For __subscribe__, execute: python receive_data.py -h

Mqtt connection

optional arguments:
  -h, --help     show this help message and exit
  --topic TOPIC  Topic for message

### Example for publish
This example publish the message "ON", in the topic "light", using the broker "broker.emqx.io" by default. 

```
python send_data.py --topic light --msg "ON"
```

If you don't use the options, the script send a message and topic by deafult. The next example send a message "Hello world" in the topic "send_msg". The broker by default is "broker.emqx.io". 

```
python send_data.py
```

### Example for subscribe
This example show how to subscribe in the topic "light"

```
python receive_data.py --topic light
```

