from machine import Pin
from utime import sleep
from wlan import wlanConnect
from constants import SERVER_HOSTNAME, USER, PASSWORD
from MQTT_helper_functions import getMQTTClient, handleSubscribe

def handleReceivingMessage(topic, response):
    # Perform desired actions based on the subscribed topic and response
    print("Received message on topic:", topic)
    print("Response:", response)

led_onboard = Pin("LED", Pin.OUT)
led_onboard.off()

ssid = input("Enter ssid of wifi\n")
password = input("Enter password of wifi\n")

wlan = wlanConnect(ssid, password)
userInput = -1

if wlan.isconnected():
    led_onboard.on()
    
    client = getMQTTClient(
            "shahzaib10",
            SERVER_HOSTNAME,
            0,
            USER,
            PASSWORD,
            7200,
            True,
            SERVER_HOSTNAME
            )
    print("Successfully initialized a MQTT client")
    
    client.set_callback(handleReceivingMessage)
    handleSubscribe('Topic', client)

    while True:
       sleep(5)
       client.check_msg()
    
    userInput = input(f"Press 0 to disconnect from {ssid}\n")

if int(userInput) == 0:
    led_onboard.off()
    wlan.disconnect()
