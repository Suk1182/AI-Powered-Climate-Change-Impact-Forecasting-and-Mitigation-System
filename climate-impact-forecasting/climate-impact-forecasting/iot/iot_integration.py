
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("iot/climate")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print("Received data:", data)
    # Process the data or send it to the model for predictions

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)
client.loop_forever()
