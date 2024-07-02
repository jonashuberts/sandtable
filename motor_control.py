from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
import math
import time

# Initialize motors
motor_d_plate = Motor(Port.D)
motor_c_arm = Motor(Port.C)

# Define the conversion factors
PLATE_RATIO = 60 / 12
MOTOR_UNITS_PER_ROTATION = 360  # Degrees per full rotation

# Function to convert theta and rho to motor positions
def polar_to_motor_angles(theta, rho):
    alpha = math.acos(rho)
    m1 = theta + alpha
    m2 = -theta - 3 * alpha  # Adjusted to move in the opposite direction
    return m1, m2

# Function to convert angles in radians to motor degrees
def radians_to_degrees(radians):
    return radians * MOTOR_UNITS_PER_ROTATION / (2 * math.pi)

# Function to move motors to desired angles using run_angle
def move_motors(current_theta, current_rho, target_theta, target_rho):
    current_m1, current_m2 = polar_to_motor_angles(current_theta, current_rho)
    target_m1, target_m2 = polar_to_motor_angles(target_theta, target_rho)
    
    current_m1_degrees = radians_to_degrees(current_m1)
    current_m2_degrees = radians_to_degrees(current_m2)
    
    target_m1_degrees = radians_to_degrees(target_m1)
    target_m2_degrees = radians_to_degrees(target_m2)
    
    delta_m1_degrees = target_m1_degrees - current_m1_degrees
    delta_m2_degrees = target_m2_degrees - current_m2_degrees

    # Move motor D (plate) with gear ratio
    motor_d_plate.run_angle(speed=500, rotation_angle=delta_m1_degrees * PLATE_RATIO * -1, then=Stop.BRAKE, wait=True)

    # Move motor C (arm)
    motor_c_arm.run_angle(speed=100, rotation_angle=delta_m2_degrees, then=Stop.BRAKE, wait=True)

    # Update current position
    return target_theta, target_rho
