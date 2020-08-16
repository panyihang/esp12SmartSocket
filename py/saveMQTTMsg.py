import paho.mqtt.client as mqtt
import json
import time
import pymysql

HOST = "mqtt.panyihang.top"
PORT = 1883
client_id = "智能声控开关-控制端-test"
topic = 'test0'

connect = pymysql.Connect(
host        =   'localhost',
port        =   3306,
user        =   'root',
passwd      =   'panyihang233',
db          =   'testDB',
charset     =   'utf8',
cursorclass = pymysql.cursors.DictCursor
)

cursor = connect.cursor()

sql = "INSERT INTO trade (driverName, time, temperature,humidity,wifiInfo,freeMemey) VALUES ( '%s', '%s', '%s','%s','%s','%s')"

def is_json(inputJson):
    try:
        json_object = json.loads(inputJson)
    except ValueError:
        return False
    return True


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic)


def on_message(client, userdata, msg):
    global cursor
    if is_json(str(msg.payload.decode('utf-8'))) and str(msg.topic) == str(topic):
        mqttGetMsg = json.loads(str(msg.payload.decode('utf-8')))
        data = (str(mqttGetMsg['driverName']),str(mqttGetMsg['time']),str(mqttGetMsg['temperature']),str(mqttGetMsg['humidity']),str(mqttGetMsg['wifiInfo']),str(mqttGetMsg['freeMemey']))
        cursor.execute(sql % data)
        connect.commit()

def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)

client = mqtt.Client(client_id)
client.username_pw_set("saveMsgServerTest", "")
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.on_disconnect = on_disconnect
client.connect(HOST, PORT, 10)
client.loop_forever()