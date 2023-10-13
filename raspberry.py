import time
import RPi.GPIO as GPIO

#General GPIO Setup
GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
GPIO.setup(20, GPIO.OUT) #sets GPIO pin 20 as an output
GPIO.setup(21, GPIO.OUT) #sets GPIO pin 21 as an output

try:
    #General GPIO Setup
    GPIO.setmode(GPIO.BCM) #sets how we reference GPIO pins
    GPIO.setup(20, GPIO.OUT) #sets GPIO pin 20 as an output
    GPIO.setup(21, GPIO.OUT) #sets GPIO pin 21 as an output
    
    GPIO.output(20,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(20,GPIO.LOW)
    time.sleep(2)
    
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(21,GPIO.LOW)
    time.sleep(2)
    GPIO.cleanup()
    
except KeyboardInterrupt: #stops try if (ctrl + c) is pressed
    pass


6.2 final code

import RPi.GPIO as GPIO
import lcd_i2c
import time

#General GPIO Setup
print("Setup") 
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT) #direction A
GPIO.setup(21, GPIO.OUT) #direction B
GPIO.setup(23, GPIO.OUT) #Sets GPIO the pin 23 as outut


#Demonstration of user input and Error Handling
try:
    while True: #Continuously running loop
        lcd_i2c.lcd_init()
        lcd_i2c.printer('Hello', ' ')
        time.sleep(2)
        duty_cycle = 0
        userinput1 = input("Enter Desired Direction:") #This prompts the user to provide an input and assigns it to the variable string
        if userinput1 == "A": #evaluates if the user entered a string of "a"
             lcd_i2c.printer('Direction', 'A')
            GPIO.output(23, GPIO.HIGH)
            direction_A = GPIO.PWM(20, 500)
            while duty_cycle<=18:
                direction_A.ChangeDutyCycle(duty_cycle)
                direction_A.start(duty_cycle)
                time.sleep(5)
                duty_cycle+=1
            direction_A.stop()
            GPIO.output(23, GPIO.LOW)
            time.sleep(3)
        elif userinput1 == "B": #evaluates if the user entered a string of "b"
            print ("Failure") #Prints to the user
            lcd_i2c.printer('Direction', 'B')
            GPIO.output(23, GPIO.HIGH)
            direction_B = GPIO.PWM(21, 500)
            while duty_cycle<=18:
                direction_B.ChangeDutyCycle(duty_cycle)
                direction_B.start(duty_cycle)
                time.sleep(5)
                duty_cycle+=1
            GPIO.output(23, GPIO.LOW)
            direction_B.stop()
            time.sleep(3)
        elif userinput1 == "stop": #evaluates if the user entered a string of "stop"
            break #This breaks out of the loop if the user entered stop, effectively stopping the program
        else:
            print ("Invalid Input, please try again.") #Prints to the user
        lcd_i2c.printer('Goodbye', ' ')
        time.sleep(2)

            
        GPIO.cleanup()
        lcd_i2c.cleanup()
            
except KeyboardInterrupt:
    pass

