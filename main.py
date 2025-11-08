from machine import Pin
from time import sleep
from dht import DHT22
from gpio_lcd import GpioLcd

# DHT22 data connected to GP16 (change if needed)
dht = DHT22(Pin(15))

# LCD connected as per your wiring
lcd = GpioLcd(rs_pin=Pin(12), enable_pin=Pin(11), d4_pin=Pin(10),
              d5_pin=Pin(9), d6_pin=Pin(8), d7_pin=Pin(7),
              num_lines=2, num_columns=16)
print("Hii...\nThis is Pradamesh\n")
print("WAIT... Sensing the Temparature and Humidity")

message1 = "Hii....\nI am Pradamesh"

lcd.clear()
for char in message1:
    lcd.putstr(char)
    sleep(0.1)
sleep(.7)
        
message2 = "My Project  'DHT22 To LCD 16x2'"

lcd.clear()
for char in message2:
    lcd.putstr(char)
    sleep(0.1)
sleep(.7)


while True:
    try:
        dht.measure()
        temp = dht.temperature()
        hum = dht.humidity()

        lcd.clear()
        lcd.putstr("Temp: {:.1f}C".format(temp))
        lcd.move_to(0, 1)  # Move cursor to the beginning of second line
        lcd.putstr("Hum: {:.1f}%".format(hum))


        print("Temp: {:.1f}C Hum: {:.1f}%".format(temp, hum))
    except Exception as e:
        lcd.clear()
        lcd.putstr("Sensor Error")
        print("Error reading DHT22:", e)

    sleep(1)
    lcd.clear()
