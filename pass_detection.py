import Adafruit_BBIO.GPIO as GPIO
import time

password = [1,0,1,1]
entered_password = []

def main():
    # Setup GPIO as input for digital mic
    GPIO.setup("P8_14", GPIO.IN)

    # Wait for knock to start password
    while True:
        if not GPIO.input("P8_14"):
            print "Starting Password Check"
            time.sleep(0.1) # Wait for bounces

        # Fill password
        for i in range(0,4):
            entered_password.append(poll_for_knock(1))
            time.sleep(0.1) # Wait for bounces

        print entered_password

        # Compare password to set password
        if entered_password == password:
            print "Password Correct!"
        else:
            print "nope, ignoring"

        entered_password.clear()

def poll_for_knock(timeout):
    death_time = time.time() + timeout
    while (time.time() < death_time):
        if not GPIO.input("P8_14"):
            return True
    print "timed out"
    return False





if __name__ == "__main__":
    main()
