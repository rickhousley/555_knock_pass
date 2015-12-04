import Adafruit_BBIO.GPIO as GPIO
import time

password = []
entered_password = []

knock_speed = 1

def main():
    # Setup GPIO as input for digital mic
    GPIO.setup("P8_14", GPIO.IN)

    password = update_password()
    print password

    # Wait for knock to start password
    while True:
        if not GPIO.input("P8_14"):
            print "Starting Password Check"
            time.sleep(knock_speed) # Wait for bounces

            # Fill password
            for i in range(0,len(password)):
                entered_password.append(poll_for_knock(knock_speed))

            print entered_password

            # Compare password to set password
            if entered_password == password:
                print "Password Correct!"

                # It should unlock here

                # Check for password update
                password = update_password()


            del entered_password[:]

def update_password():
    file = open('secret.pass', 'r')
    passw = map(int, list(file.read().split()))
    return passw

def poll_for_knock(timeout):
    death_time = time.time() + timeout
    while (time.time() < death_time):
        if not GPIO.input("P8_14"):
            time.sleep(0.1) # Wait for bounces
            return True
    return False

if __name__ == "__main__":
    main()
