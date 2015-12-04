import Adafruit_BBIO.GPIO as GPIO
import time

password = [1,0,1,0]

def main():
    GPIO.setup("P8_14", GPIO.IN)

    while True:
        # read digital
        if not GPIO.input("P8_14"):
            print "Knock!"
            time.sleep(.1)

if __name__ == "__main__":
    main()
