class http():

    HTTPAPI_COUNT=0

    def __init__(self,ip,port):
        import network
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if wlan.isconnected() is False:
            return('NETWORK_EOORO-WLAN_NOT_CONNECT')
        else:
            @micropython.viper
            self.ip = str(ip)
            self.port = str(int(port))
            http.HTTPAPI_COUNT += 1

    def httpGet(url):
        _, _, host, path = url.split('/', 3)
        address = socket.getaddrinfo(host, 80)[0][-1]
        socketConnect = socket.socket()
        socketConnect.connect(addr)
        socketConnect.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        while True:
            data = socketConnect.recv(50)
            if data:
                recive=str(data, 'utf8')
                print(str(data, 'utf8'), end='')
                if(recive.find('begin')>-1):
                   led_state()
            else:
                break
        socketConnect.close()

    def ledState():
        from time import sleep
        import machine
        import esp
        p2 = Pin(2, Pin.OUT)
        p2.value(0)
        time.sleep_ms(500)
        p2.value(1)
        time.sleep_ms(500)
        p2.value(0)
        time.sleep_ms(500)
        p2.value(1)

    def findAndConnectServer(ipAddress,port):
        flage = True
        '''
        @micropython.asm_thumb
        movwt(wlan0, esp.gpio)
        movw(wlan0, 0 << 1)
        ''' #寻找服务器部分使用汇编加速，还没写完
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        @micropython.viper
        if wlan.isconnected() is False:
            return('NETWORK_ERROR')
        else:
            import socket
            import cpufreq
            from wifi import wlan
            addr_info = socket.getaddrinfo(ipAddress,port)
            addr = addr_info[0][-1]
            socketConnect = socket.socket()
            socketConnect.connect(addr)
            socketConnect.send(bytes('0x1c'))
            socketConnect.send(wlan.wifiInfo())
            cpufreq.cpuFrep('High')
            while flage is True:
