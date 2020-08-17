import gc
import os
import dht
import time
import ujson
import machine
import webrepl
from cpu import cpu
from wifi import wlan
from machine import Pin
from machine import WDT
from machine import Timer
from simple import MQTTClient


wifiSsid    =   'xxxx'          #wifi的ssid
wifiPasswd  =   'xxxx'          #wifi的密码
server      =   'xxxx'          #mqtt服务器
clienID     =   'ESP8266--'     #mqtt id的前缀
userName    =   'xxxx'          #mqtt帐号
passwd      =   'xxxx'          #mqtt密码
topic       =   'xxxx'          #订阅的主题

testMsg     =    {}
light0      =    'on'
light1      =    'on'
cpufreq     =     str(machine.freq())
clienID     =    str(clienID)+str(''.join([('0'+hex(ord(os.urandom(1)))[2:])[-2:] for x in range(4)]))

flage       =    False

temperature =       []
humidity    =       []


relLight0 = Pin(16,Pin.OUT)
led0 = Pin(5, Pin.OUT)


def start():
    global flage
    global testMsg
    global led0
    global temperature
    global humidity
    readDHT = Timer(-1)
    readDHT.init(period=3500, mode=Timer.PERIODIC, callback=getDHTInfo)
    led0ON = Timer(-1)
    led0OFF = Timer(-1)
    led0ON.init(period=500, mode=Timer.PERIODIC, callback=lambda t:led0.on())
    time.sleep(0.25)
    led0OFF.init(period=500, mode=Timer.PERIODIC, callback=lambda t:led0.off())
    cpu.cpuFrep(1)
    #wifi连接
    wlan.wifiConnect(wifiSsid,wifiPasswd)
    webrepl.start()
    #mqtt连接
    mqttConnect = MQTTClient(clienID,server,user=userName,password=passwd,keepalive=15)
    mqttConnect.set_callback(subCD)
    mqttConnect.connect()
    mqttConnect.subscribe(topic)
    wdt = WDT()
    while True:
        wdt.feed()
        mqttConnect.check_msg()
        if flage:
            sandMsg = ujson.dumps(testMsg)
            mqttConnect.publish(topic='test0',msg=sandMsg)
            wdt.feed()
            led1TwinkleTimer = Timer(1)
            led1TwinkleTimer.init(period=0, mode=Timer.ONE_SHOT, callback=led1Twinkle)
            testMsg ={}
            temperature=[]
            humidity=[]
            wdt.feed()
            flage = False
        else:
            if int(time.time()) % 15 == 0:
                flage = True
                getInfo()
                wdt.feed()
        time.sleep(0.75)
        wdt.feed()

def findText(text,msg):
    if text in msg:
        return True
    else:
        return False

def getInfo():
    global temperature
    global humidity
    testMsg['time'] = str(time.time())
    testMsg['light0'] = str(light0)
    testMsg['light1'] = str(light1)
    testMsg['freeMemey'] = str(gc.mem_free())
    testMsg['cpuFreq'] = str(machine.freq())
    if len(temperature) >= 1:
        testMsg['temperature'] = str(temperature[0])
    else:
        testMsg['temperature'] = None
    if len(humidity) >= 1:
        testMsg['humidity'] = str(humidity[1])
    else:
        testMsg['humidity'] = None
    testMsg['driverName'] = str(clienID)
    testMsg['wifiInfo'] = str(wlan.wifiInfo()[0])

def getDHTInfo(f):
    global temperature
    global humidity
    dhtRead=dht.DHT11(Pin(12))
    dhtRead.measure()
    temperature.append(dhtRead.temperature())
    humidity.append(dhtRead.humidity())
    

def led1Twinkle(f):
    global led0
    led0.off()
    led1 = Pin(4, Pin.OUT)
    led1.on()
    time.sleep(0.25)
    led1.off()

def subCD(topic,msg):
    global dht0
    global flage
    global light0
    global light1
    global cpufreq
    global relLight0
    if findText(clienID,msg):
        if findText('set',msg):
            if findText('light0',msg):
                if findText('on',msg):
                    light0 = 'on'
                    relLight0.on()
                elif findText('off',msg):
                    light0 = 'off'
                    relLight0.off()
                else:
                    print('LIGHT0_ERROR')

            elif findText('light1',msg):
                if findText('on',msg):
                    light1 = 'on'
                elif findText('off',msg):
                    light1 = 'off'
                else:
                    print('LIGHT1_ERROR')
            
            elif findText('cpufreq',msg):
                if findText('high',msg):
                    cpu.cpuFrep(1)
                elif findText('low',msg):
                    cpu.cpuFrep(0)
                else:
                    print('CPUFREQ_ERROR')

            else:
                print('SET_ERROR')
        elif findText('getInfo',msg):
            flage = True
            getInfo()