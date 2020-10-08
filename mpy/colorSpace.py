class colorSpaceChanged(num1,num2,num3):
    def __main__(self):
        if num1 in range(0,256) and num2 in range(0,256) and num3 in range(0,256):
            RGB2YUV(num1,num2,num3)
        elif num1 in range(16,236) and num2 in range(16,239) and num3 in range(16,239):
            YUV2RGB(num1,num2,num3)
        else:
            print("AUTO CHOICE INPUT TYPE FAILED")

    def RGB2YUV(r,g,b):
        y = ((66*r + 129*g + 25*b + 128)>>8)+16
        u = ((-38*r - 74*g + 112*b + 128)>>8)+128
        v = ((112*r - 94*g - 18*b + 128)>>8)+128
        return(y,u,v)

    def clip(num):
        if num <= 0:
            return(0)
        elif num >= 255:
            return(255)
        else:
            return(num)
    
    def YUV2RGB(y,u,v):
        C = y-16
        D = u-128
        E = v-128
        r = clip(( 298*C + 409*E + 128)>>8)
        g = clip(( 298*C - 100*D - 208*E + 128)>>8)
        b = clip(( 298*C + 516*D + 128)>>8)
        return(r,g,b)
