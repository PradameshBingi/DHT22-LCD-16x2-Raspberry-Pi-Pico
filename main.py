import machine
import utime
from machine import Pin
import network
import time
import json
from umqtt import MQTTClient

# Pin configuration for the 7-segment display
# These variables must be defined in the global scope so any function can use them.
segments = [
    machine.Pin(0, machine.Pin.OUT),
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(3, machine.Pin.OUT),
    machine.Pin(4, machine.Pin.OUT),
    machine.Pin(5, machine.Pin.OUT),
    machine.Pin(6, machine.Pin.OUT)
]

# Mapping of digits to 7-segment pin states
number_map = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9 
]

# WiFi settings
ssid = "mqtt_sd"
password = "12345"

# MQTT server parameters
MQTT_CLIENT_ID = "7-Segment"
MQTT_HOST = "broker.emqx.io"
MQTT_TOPIC = "input"


# Function to display a specific number on the 7-segment display
# It can now use the global variables `segments` and `number_map`
def display_number(number):
    try:
        print("Displaying Number: ",number)
        segments_values = number_map[number]
        for i in range(len(segments)):
            segments[i].value(segments_values[i])
    except IndexError:
        print("Error: Number is out of the 0-9 range.")


def mqtt_message(topic, message):
    print("-------------------")
    print("topic:", topic)
    print("message:", message)
    try:
        msg = json.loads(message)
        ipnumber = int(msg)  # Ensure the input is an integer
        print("Input given number: ", ipnumber)
        display_number(ipnumber)
        utime.sleep_ms(100)
    except Exception as e:
        print("Error processing MQTT message:", e)
    print("-------------------")


# Connecting to WIFI
print("Connecting to WiFi..")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(0.3)
    print(".", end="")
print("\nWifi Connected")

# Connecting to MQTT Broker
print("Connecting to MQTT Host")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_HOST)
client.set_callback(mqtt_message)
client.connect()
client.subscribe(MQTT_TOPIC)
print("MQTT HOST Connected...")

last_ping = 0

while True:
    client.check_msg()

    if time.ticks_ms() - last_ping > 10000:
        client.ping()
        last_ping = time.ticks_ms()
    
    time.sleep(0.1)

