#rgb.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT) 
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT) 
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT) 
GPIO.setup(10, GPIO.OUT) 
GPIO.setup(11, GPIO.OUT) 



while True:
    
    #Kirmizi
    GPIO.output(4, True)
    time.sleep(1/10)
    GPIO.output(4, False)
    
    GPIO.output(5, True)
    time.sleep(1/10)
    GPIO.output(5, False)
    
    GPIO.output(6, True)
    time.sleep(1/10)
    GPIO.output(6, False)
    
    GPIO.output(7, True)
    time.sleep(1/10)
    GPIO.output(7, False)
    
    GPIO.output(8, True)
    time.sleep(1/10)
    GPIO.output(8, False)
    
    GPIO.output(9, True)
    time.sleep(1/10)
    GPIO.output(9, False)
    
    GPIO.output(10, True)
    time.sleep(1/10)
    GPIO.output(10, False)
    
    GPIO.output(11, True)
    time.sleep(1/10)
    GPIO.output(11, False)
    
    GPIO.output(11, True)
    time.sleep(1/10)
    GPIO.output(11, False)
    
    GPIO.output(10, True)
    time.sleep(1/10)
    GPIO.output(10, False)
    
    GPIO.output(9, True)
    time.sleep(1/10)
    GPIO.output(9, False)
    
    GPIO.output(8, True)
    time.sleep(1/10)
    GPIO.output(8, False)
    
    GPIO.output(7, True)
    time.sleep(1/10)
    GPIO.output(7, False)
    
    GPIO.output(6, True)
    time.sleep(1/10)
    GPIO.output(6, False)
    
    GPIO.output(5, True)
    time.sleep(1/10)
    GPIO.output(5, False)
    
    GPIO.output(4, True)
    time.sleep(1/10)
    GPIO.output(4, False)
    
    

    
    

    

