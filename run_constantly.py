# run_constantly.py
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Initialize motors
motor_d_plate = Motor(Port.D)
motor_c_arm = Motor(Port.C)

# Function to run motors at specified speeds
def run_motors(speed_d, speed_c):
    motor_d_plate.run(speed_d)
    motor_c_arm.run(speed_c)

# Function to stop motors
def stop_motors():
    motor_d_plate.stop()
    motor_c_arm.stop()
