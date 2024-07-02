#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Button
from pybricks.tools import wait

# Initialize EV3 brick and motors
ev3 = EV3Brick()
motor_d_plate = Motor(Port.D)
motor_c_arm = Motor(Port.C)

# Function to center the motors using button control
def center_motors():
    speed = -100  # Speed for manual control
    ev3.speaker.beep()

    while True:
        # Get the pressed buttons
        buttons = ev3.buttons.pressed()
        
        # Control motor D with left and right buttons
        if Button.LEFT in buttons:
            motor_d_plate.run(speed)
        elif Button.RIGHT in buttons:
            motor_d_plate.run(-speed)
        else:
            motor_d_plate.stop(Stop.HOLD)
        
        # Control motor C with up and down buttons
        if Button.UP in buttons:
            motor_c_arm.run(speed)
        elif Button.DOWN in buttons:
            motor_c_arm.run(-speed)
        else:
            motor_c_arm.stop(Stop.HOLD)
        
        # Check if the OK button is pressed
        if Button.CENTER in buttons:
            motor_d_plate.stop(Stop.HOLD)
            motor_c_arm.stop(Stop.HOLD)
            ev3.speaker.beep()
            break
        
        wait(10)

# Function to reset motor angles to zero position
def reset_motor_positions():
    motor_d_plate.reset_angle(0)
    motor_c_arm.reset_angle(0)
