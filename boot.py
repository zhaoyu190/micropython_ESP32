import network
import webrepl 
import time
ssid='HUAWEI-8TCQMZ'
password='13948523935zxc'
wlan=network.WLAN(network.STA_IF)                     #create a wlan object
wlan.active(True)                                     #Activate the network interface
wlan.connect(ssid,password) 
time.sleep(3)
if(wlan.isconnected()):
    webrepl.start()
    print("webrepl working")

