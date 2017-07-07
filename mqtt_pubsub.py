import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

Broker = "192.168.42.1"

pub_topic = "bot_sub/1"
sub_topic = "bot_pub/1"

def on_connect(client, userdata, flags, rc):
        client.subscribe(sub_topic)

def on_message(client, userdata, msg):
        message = str(msg.payload)
        print(msg.topic+" "+message)
        
def publish_mqtt(sensor_data):
        mqttc = mqtt.Client("Client")
        mqttc.connect(Broker, 1883)
        
def on_publish(mosq, obj, mid):
        print("on_publish")
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(Broker, 1883, 60)
client.publish(pub_topic, 'LXXXX')
client.loop_forever()
