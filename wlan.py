from network import WLAN, STA_IF
from utime import sleep

def wlanConnect(ssid, password):
   
    wlan = WLAN(STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        sleep(0.4)
    
    print(f"Connected to {ssid}")
    return wlan