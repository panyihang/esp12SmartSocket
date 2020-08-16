from django.shortcuts import render
import mqttClien
import time
import pymysql

connect = pymysql.Connect(
host        =   'localhost',
port        =   3306,
user        =   'root',
passwd      =   'panyihang233',
db          =   'testDB',
charset     =   'utf8',
cursorclass = pymysql.cursors.DictCursor
)
driverNmaeList = []


context   = {}
context['temperature'] = None
context['humidity'] = None
context['light0'] = 'on'
context['light1'] = 'on'

def test(request):
    global driverNmaeList
    global context
    global connect
    cursor = connect.cursor()
    cursor.execute('select * from trade')
    data = cursor.fetchall()[-5:-1]
    for driverName in range(len(data)):
        driverNmaeList.append((data[driverName])['driverName'])
    driverNmaeList = list(set(driverNmaeList))
    driverNmaeList.sort()
    context['driverNameList'] = driverNmaeList

    if request.method == "POST":
        driverNameGet = str(request.POST.get("driverName"))
        for i in range(len(data)):
            if str((data[i])['driverName']) == driverNameGet:
                context['temperature'] = str((data[driverName])['temperature'])
                context['humidity'] = str((data[driverName])['humidity'])
        if (request.POST.get("light0ON")) != None:
            context['light0'] = 'on'
            mqttClien.main(driverNameGet,'set light0 on')
            time.sleep(0.75)
        elif (request.POST.get("light0OFF")) != None:
            context['light0'] = 'off'
            mqttClien.main(driverNameGet,'set light0 off')
            time.sleep(0.75)
        elif (request.POST.get("light1ON")) != None:
            context['light1'] = 'on'
            mqttClien.main(driverNameGet,'set light1 on')
            time.sleep(0.75)
        elif (request.POST.get("light1OFF")) != None:
            context['light1'] = 'off'
            mqttClien.main(driverNameGet,'set light1 off')
            time.sleep(0.75)
            
    return render(request, 'test.html', context)

    context={}
    driverNmaeList=[]