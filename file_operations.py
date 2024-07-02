# Function to read coordinates from file
def read_coordinates_from_file(filename):
    coordinates = []
    try:
        print("Reading coordinates from file " + filename)
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('#') or line.strip() == '':
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    theta = float(parts[0])
                    rho = float(parts[1])
                    coordinates.append((theta, rho))
        print("Finished reading " + str(len(coordinates)) + " coordinates.")
    except FileNotFoundError:
        print("Error: File not found.")
    
    return coordinates
