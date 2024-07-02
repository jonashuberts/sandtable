# EV3 Sand Plotter (Sand3r)

This project is an implementation of a sand polar plotter using LEGO Mindstorms EV3. The plotter reads coordinates from a file and moves the motors to draw the corresponding pattern. It supports three modes of operation: moving to specific coordinates, running motors constantly, and running a spirograph pattern.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Homing](#homing)
  - [Move to Coordinates](#move-to-coordinates)
  - [Run Motors Constantly](#run-motors-constantly)
  - [Spirograph Mode](#spirograph-mode)
- [File Formats](#file-formats)
  - [Coordinates File](#coordinates-file)
  - [Speeds File](#speeds-file)

## Getting Started

These instructions will guide you through setting up and running the EV3 Polar Plotter on your LEGO Mindstorms EV3.

## Prerequisites

- LEGO Mindstorms EV3 Brick
- Python environment with PyBricks library (VS Code extension recommended)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ev3-polar-plotter.git
cd ev3-polar-plotter
```

2. Ensure that you have the required files:

- `main.py`: Main program file
- `motor_control.py`: Contains motor control functions
- `file_operations.py`: Contains file reading functions
- `homing.py`: Contains homing functions
- `run_constantly.py`: Contains the function to run motors constantly
- `spirograph.py`: Contains the spirograph mode implementation
- `charletslabyrinth.thr`: Example coordinates file
- `speeds.txt`: Example speeds file

## Usage

### Homing

Before starting any plotting, the motors need to be homed to their initial positions. The homing functions are included in `homing.py`.

### Move to Coordinates

The main program can read coordinates from a file and move the motors accordingly. Coordinates should be provided in a `.thr` file. Uncomment the relevant lines in `main.py` to use this mode.

### Run Motors Constantly

To run the motors constantly at specified speeds, use the `run_constantly` function from `run_constantly.py`. Uncomment the relevant lines in `main.py` to use this mode.

### Spirograph Mode

The spirograph mode runs the motors with specific speeds for a certain time and then switches to the next motor speed. The speeds are read from `speeds.txt`. Uncomment the relevant lines in `main.py` to use this mode.

## File Formats

### Coordinates File

The coordinates file should be a `.thr` file containing theta and rho values for each point. Each line should have two values separated by a space:

```
<theta> <rho>
```

Example (`charletslabyrinth.thr`):

```
0.00000 0.00000
1.52827 0.00059
1.47634 0.00119
1.42295 0.00178
1.37546 0.00238
```

### Speeds File

The speeds file should contain pairs of motor speeds, one pair per line. Each line represents a set of speeds for the plate motor (motor D) and the arm motor (motor C) and the duration how long the movement should last.:

```
<speed_d> <speed_c> <duration>
```

Example (`speeds.txt`):

```
100 85 73
120 10 280
100 38 186
150 50 37
```
