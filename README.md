# esp12SmartSocket

# 基于ESP12f的智能声控开关

### 本仓库为[基于ESP12f的智能声控开关](https://oshwhub.com/an_ye/ji-yuesp8266-di-zhi-neng-kai-guan)的软件部分


+ mpy目录为esp8266使用的microopython，使用前需配置webrepl `import webrepl_setup`，再将该目录内所有文件上传至单片机即可
+ micropython的固件放在mpy目录内，使用esptool.py烧录
+ start.sh运行需要root权限 `sudo chmod +x start.sh`
+ 运行start.sh即可启动所有服务，所需的依赖：
    + docker
    + python3
    + mariadb
    + python-pymysql
    + python-django
    + python-paho-mqtt
## 功能介绍
单片机部分使用micropython编写，server端使用python+django框架编写

全部代码在 arch linux (2020/8/15) 下正常运行，启动脚本会尽可能提高兼容性
