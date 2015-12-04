import Adafruit_BBIO.GPIO as GPIO
import time

password = [1,0,1,1]

def main():
    # Setup GPIO as input
    GPIO.setup("P8_14", GPIO.IN)

    # Wait for knock to start password
    while True:
        if not GPIO.input("P8_14"):
            print "Starting Password Check"
            time.sleep(0.1) # Wait for bounces
            if poll_for_knock(10):
                print "1"


def poll_for_knock(timeout):
    death_time = time.time() + timeout
    while (time.time() < death_time):
        if not GPIO.input("P8_14"):
            return True
    print "timed out"
    return False





if __name__ == "__main__":
    main()
