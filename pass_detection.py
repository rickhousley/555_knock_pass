import Adafruit_BBIO.GPIO as GPIO
from time import time

password = [1,0,1,1]

def main():
    # Setup GPIO as input
    GPIO.setup("P8_14", GPIO.IN)

    # Wait for knock to start password
    while True:
        if not GPIO.input("P8_14"):
            print "Starting Password Check"
            if poll_for_knock(2):
                print "1"


def poll_for_knock(timeout):
    time = now()
    timout = now() + timeout

    if (now() > timeout):
        if not GPIO.input("P8_14"):
            return True
    return False





if __name__ == "__main__":
    main()
