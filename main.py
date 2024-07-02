#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Button
import motor_control
import file_operations
import homing
from run_constantly import run_motors, stop_motors
from spirograph import run_spirograph, stop_motors as stop_spirograph_motors, read_speeds_from_file
import time

# Initialize EV3 brick
ev3 = EV3Brick()

# Main program
ev3.speaker.beep()
homing.center_motors()
homing.reset_motor_positions()
ev3.speaker.beep()

# Specify the file name
file_name = "erase.thr"

PLATE_RATIO = 60 / 12

# Move through the list of coordinates
current_theta = 0
current_rho = 1

# User selection for mode
print("Select mode:")
print("1: Follow coordinates")
print("2: Run motors constantly")
print("3: Spirograph mode")

# Wait for button press
while True:
    buttons = ev3.buttons.pressed()
    if Button.LEFT in buttons:
        mode = 1
        break
    elif Button.RIGHT in buttons:
        mode = 2
        break
    elif Button.UP in buttons:
        mode = 3
        break

if mode == 1:
    # Read coordinates from file
    coordinates = file_operations.read_coordinates_from_file(file_name)
    print("Starting movement based on coordinates...")
    for theta, rho in coordinates:
        current_theta, current_rho = motor_control.move_motors(current_theta, current_rho, theta, rho)
    print("Finished movement based on coordinates.")
elif mode == 2:
    print("Running motors constantly...")
    speed_d = 120  # Speed for motor D (plate)
    speed_c = 10  # Speed for motor C (arm)
    run_motors(speed_d, speed_c)
    time.sleep(0.5)
    print("Press any button to stop motors.")
    while not ev3.buttons.pressed():
        pass
    stop_motors()
    print("Stopped motors.")
elif mode == 3:
    print("Running spirograph mode...")
    speeds_file_name = "speeds.txt"
    speeds = read_speeds_from_file(speeds_file_name)
    run_spirograph(speeds, PLATE_RATIO)
    time.sleep(0.5)
    print("Press any button to stop spirograph.")
    while not ev3.buttons.pressed():
        pass
    stop_spirograph_motors()
    print("Stopped spirograph mode.")

# Optionally beep to indicate the end of the movement
ev3.speaker.beep()
