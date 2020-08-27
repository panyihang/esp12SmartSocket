import time
import neopixel, machine
ledNum = 4


rgbMAX = 255
rgbRange = 10

np = neopixel.NeoPixel(machine.Pin(15), ledNum)
r,g,b=0,0,0
flage = True
rgbFlage = True
rgbList = []

def writeLED(r,g,b):
    global rgbList
    rgbList.append(str(r)+' '+str(g)+' '+str(b))
    if len(rgbList) >= ledNum+1:
        rgbList = rgbList[1:ledNum+1]
        print(rgbList)
        for led in range(ledNum):
            ledRGB = str(rgbList[led]).split(' ')
            np[led] = (int(ledRGB[0]),int(ledRGB[1]),int(ledRGB[2]))
        np.write()

def clip(num):
    if num <= 0:
        return(0)
    elif num >= 255:
        return(255)
    else:
        return(num)

def RGB2YUV(r,g,b):
    y = ((66*r + 129*g + 25*b + 128)>>8)+16
    u = ((-38*r - 74*g + 112*b +128)>>8)+128
    v = ((112*r - 94*g - 18*b +128)>>8)+128
    return(y,u,v)

def YUV2RGB(y,u,v):
    C = y-16
    D = u-128
    E = v-128
    r = clip(( 298*C + 409*E + 128)>>8)
    g = clip(( 298*C - 100*D - 208*E + 128)>>8)
    b = clip(( 298*C + 516*D + 128)>>8)
    return(r,g,b)
    

while True:
    if flage:
        r = rgbMAX
        b = 0
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(r,i,b)
        g = rgbMAX
        b = 0
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(rgbMAX-i,g,b)
        r = 0
        g = rgbMAX
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(r,g,i)
        b = rgbMAX
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(r,g,rgbMAX-i)
        b = 0
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(i,g,b)
        r = rgbMAX
        for i in range(0,rgbMAX+1,rgbRange):
            writeLED(r,rgbMAX-i,b)
        g = 0
        if rgbFlage:
            rgbRange += 15
            if rgbRange > 250:
                rgbFlage = False
        else:
            rgbRange -= 15
            if rgbRange < 15:
                rgbFlage = True