from machine import Pin
import time
def highPin(pin):
    Pin(pin,Pin.OUT).on()
def lowPin(pin):
    Pin(pin,Pin.OUT).off()
def readPin(pin):
    return(Pin(pin,Pin.IN).value())
def keyTimeOut(setIO,readIO):
    pass
gpioList = ['16 0', '16 5', '16 12', '16 13', '16 4', '16 12' , '14 5',  '14 4', '14 13', '12 0', '12 5', '12 4', '13 0', '13 5', '4 0', '4 5', '5 0']
while True:
    for i in range(len(gpioList)):
        io = gpioList[i].split(' ')
        setIO,readIO = int(io[0]),int(io[1])
        if readIO == 0:
            lowPin(setIO)
            highPin(readIO)
            if readPin(readIO) == 0:
                time.sleep_ms(100)
                highPin(readIO)
                if readPin(readIO) == 0:
                    print(setIO,readIO)
            highPin(readIO)
            highPin(setIO)
        else:
            highPin(setIO)
            lowPin(readIO)
            if readPin(readIO) == 1:
                time.sleep_ms(10)
                lowPin(readIO)
                if readPin(readIO) == 1:
                    print(setIO,readIO)
            lowPin(readIO)
            lowPin(setIO)