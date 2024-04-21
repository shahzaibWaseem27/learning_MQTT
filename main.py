from machine import Pin
from wlan import wlanConnect

led_onboard = Pin("LED", Pin.OUT)
led_onboard.off()

ssid = input("Enter ssid of wifi\n")
password = input("Enter password of wifi\n")

wlan = wlanConnect(ssid, password)
userInput = -1

if wlan.isconnected():
    led_onboard.on()
    userInput = input(f"Press 0 to disconnect from {ssid}\n")

if int(userInput) == 0:
    wlan.disconnect()
