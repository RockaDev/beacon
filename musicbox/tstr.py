import RPi.GPIO as GPIO
import keyboard,time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
def hello(channel):keyboard.send("down")
def hellos(channel):print("sss")
GPIO.add_event_detect(4,GPIO.FALLING,callback=hello,bouncetime=10)
GPIO.add_event_detect(17,GPIO.FALLING,callback=hellos,bouncetime=10)

while 1:
    time.sleep(1)