import paho.mqtt.client as mqtt
import json
import time

HOST = "mqtt.panyihang.top"
PORT = 1883
client_id = "智能声控开关-控制端-test"

def on_connect(client, userdata, flags, rc):
    client.subscribe("test0")


def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

def main(sendMsg):
    client = mqtt.Client(client_id)
    client.username_pw_set("sandServerTest", "")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_disconnect = on_disconnect
    client.connect(HOST, PORT, 10)
    client.publish("test0", payload=str(sendMsg), qos=2)
    client.disconnect()