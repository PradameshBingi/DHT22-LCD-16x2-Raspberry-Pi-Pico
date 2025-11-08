# 🌡️ DHT22 → LCD 16x2 (Raspberry Pi Pico)

### 🧑‍💻 Author: [**Pradamesh Bingi**](https://github.com/PradameshBingi)

---

## 🧠 Project Overview

This project reads temperature and humidity from a **DHT22** sensor connected to a Raspberry Pi Pico and displays the measurements in real time on a **16×2 HD44780-compatible LCD**.

The program continuously measures the environment and updates the LCD so the displayed values are always current.
<p align="center"> <img alt="Raspberry Pi Pico + Servo + Buttons" src="https://img.shields.io/badge/Platform-RP2040_Pico-blue"> <img alt="Language: MicroPython" src="https://img.shields.io/badge/MicroPython-1.24.1-ffcc00"> <img alt="Simulated on Wokwi" src="https://img.shields.io/badge/Simulator-Wokwi-brightgreen"> </p>


---

## Live Simulation
WokWI Simulation https://wokwi.com/projects/446597260086069249

---

## ⚙️ Features

- 🌡️ Reads temperature (°C) from DHT22  
- 💧 Reads relative humidity (%) from DHT22  
- 🖥️ Displays temperature and humidity simultaneously on a 16×2 LCD  
- 🔁 Runs in a continuous loop with updated readings every second  
- 🧩 Simple error handling: displays "Sensor Error" on LCD when reading fails

---

## 🧩 Hardware Setup

### 🪴 Components
- Raspberry Pi Pico  
- DHT22 sensor  
- 16×2 HD44780-compatible LCD (driven in 4-bit mode)  
- 220Ω resistor (for LCD backlight/LED)  
- Jumper wires

---

## ⚡ Pin Configuration

| LCD Pin | Pico GPIO |
| :-----: | :-------: |
| D7 | GP7 |
| D6 | GP8 |
| D5 | GP9 |
| D4 | GP10 |
| E  | GP11 |
| RS | GP12 |
| VDD | VSYS |
| VSS | GND |
| RW | GND |
| K (Backlight GND) | GND |
| A (Backlight +) | via 220Ω resistor to VSYS |

| DHT22 Pin | Pico |
| :-------: | :--: |
| VCC | 3V3 |
| GND | GND |
| DATA (SDA) | GP15 |

---

## 🧱 Wokwi Circuit Configuration (excerpt)

```json
    {
      "type": "wokwi-pi-pico",
      "id": "pico",
      "attrs": { "env": "micropython-20241129-v1.24.1" }
    }
```
## Connections used in Wokwi:

pico:GP7 → lcd:D7

pico:GP8 → lcd:D6

pico:GP9 → lcd:D5

pico:GP10 → lcd:D4

pico:GP11 → lcd:E

lcd:RS → pico:GP12

pico:VSYS → lcd:VDD and resistor → lcd:A

pico:3V3 → dht:VCC

pico:GND → lcd:VSS, lcd:RW, lcd:K, dht:GND

dht:SDA → pico:GP15

---

## 🧠 Code Functionality

### Initialization & Setup

DHT22 object is instantiated on pin GP15 (in the code provided it uses Pin(15).

GpioLcd object is created with:

rs_pin=Pin(12), enable_pin=Pin(11), data pins d4_pin=Pin(10), d5_pin=Pin(9), d6_pin=Pin(8), d7_pin=Pin(7)

num_lines=2, num_columns=16

### Startup Messages

Prints a short greeting to the REPL and scrolls two intro messages on the LCD with small delays.

### Main Loop

Continuously:

- Calls dht.measure()
- Reads `temp = dht.temperature()` and `hum = dht.humidity()`
- Clears LCD and writes:
  - First line: `Temp: {temp:.1f}C`
  - Second line: `Hum: {hum:.1f}%`
- Prints the same values to serial output (REPL).
- If any exception occurs while reading the sensor, writes `Sensor Error` to the LCD and logs the exception to serial.
- Sleeps 1 second, then clears the LCD.

---

## 🧰 Supporting Libraries & Files (included in project)

- **GpioLcd** — HAL implementation for HD44780 16×2 using GPIO pins (implements init, write, backlight, and low-level pulsing)  
- **LcdApi** — Generic HD44780 API used by GpioLcd (command constants, putstr/putchar, custom chars, etc.)

---

## 📦 Dependencies

| Module | Description |
| :-----: | :--------- |
| `machine` | Pin and hardware control |
| `time / utime` | Sleep and microsecond delays |
| `dht` | DHT22 sensor driver |
| `gpio_lcd` | GpioLcd HAL class for HD44780 LCD |
| `lcd_api` | HD44780 API base class |

---

## 🧠 How It Works (Step-by-Step)

- The program initializes the DHT22 sensor and LCD.
- Intro messages are displayed on the LCD.
- In an infinite loop:
  - The DHT22 is polled for temperature and humidity.
  - Values are formatted and shown on the two LCD lines.
  - Values are printed to the REPL.
  - On read failure, "Sensor Error" is displayed.
- The loop pauses 1 second between iterations.

---

## 🖥️ Example Output (serial & LCD)

- Serial/REPL: `Temp: 25.3C Hum: 47.8%`  
- LCD Line 1: `Temp: 25.3C`  
- LCD Line 2: `Hum: 47.8%`

---

## 🧑‍🔧 Developed Using

- 🐍 MicroPython  
- ⚡ Raspberry Pi Pico  
- 🧩 Wokwi Simulator (for wiring reference)

---

## ✨ Notes

- LCD is driven in **4-bit mode** using D4–D7.  
- The backlight anode is connected to VSYS via a 220Ω resistor; common grounds are required.

---

## 🏁 End of Project

### Made with ❤️ by [**Pradamesh Bingi**](https://github.com/PradameshBingi)
