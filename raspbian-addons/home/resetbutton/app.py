import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Reset Button Pressed')
        
        # reset wifi
        call(["cp", "/etc/wpa_supplicant/wpa_supplicant.conf.reset", "/etc/wpa_supplicant/wpa_supplicant.conf"])

        # reset weather config
        call(["cp", "/home/weather/config.json.reset", "/home/weather/config.json"])

        # reboot
        call(["reboot"])

        time.sleep(0.2)