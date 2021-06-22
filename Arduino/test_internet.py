#!/usr/bin/python3

import socket, requests
import time, pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')
led = board.get_pin('d:10:o')
led_g = board.get_pin('d:11:o')


def isConnected():
    url='http://www.google.com/'
    timeout=10
    try:
        _ = requests.get(url, timeout=timeout)
        #print("internet Active")
        return True
    except Exception as e:
        print(e)
        #print("No Internet")
    return False

while True:
    if isConnected():
        led_g.write(1)
        led.write(0)
    else:
        led_g.write(0)
        led.write(1)
    time.sleep(0.5)
    led_g.write(0)
    time.sleep(0.2)