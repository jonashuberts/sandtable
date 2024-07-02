import time
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop

# Initialize motors
motor_d_plate = Motor(Port.D)
motor_c_arm = Motor(Port.C)

# Define the conversion factors
PLATE_RATIO = 60 / 12  # Gear ratio

def read_speeds_from_file(filename):
    speeds = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('#') or line.strip() == '':
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    speed_d = int(parts[0])
                    speed_c = int(parts[1])
                    duration = int(parts[2])
                    speeds.append((speed_d, speed_c, duration))
    except FileNotFoundError:
        print("Error: File not found.")
    return speeds

def erase_drawing():
    motor_d_plate.run(speed=94*2)
    motor_c_arm.run(speed=19*2)
    time.sleep(440)
    time.sleep(440)
    motor_d_plate.stop(stop_type=Stop.BRAKE)
    motor_c_arm.stop(stop_type=Stop.BRAKE)

def run_spirograph(speeds, gear_ratio):
    while True:
        for speed_d, speed_c, duration in speeds:
            motor_d_plate.run(speed=speed_d)
            motor_c_arm.run(speed=speed_c)
            time.sleep(duration)
            motor_d_plate.stop(stop_type=Stop.BRAKE)
            motor_c_arm.stop(stop_type=Stop.BRAKE)
            erase_drawing()


def stop_motors():
    motor_d_plate.stop(stop_type=Stop.BRAKE)
    motor_c_arm.stop(stop_type=Stop.BRAKE)
