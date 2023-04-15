import numpy as np

def scale_polygon():
    num_sides = int(input("Enter number of sides: "))
    coords = []
    for i in range(num_sides):
        x, y = map(int, input("Enter coordinate {} (x,y): ".format(i + 1)).split(","))
        coords.append((x, y))
    x_scale = float(input("Enter x scaling factor: "))
    y_scale = float(input("Enter y scaling factor: "))

    if x_scale == y_scale:
        print("Uniform scaling")
    else:
        print("Differential scaling")

    polygon = np.array(coords)

    scaling_matrix = np.array([[x_scale, 0], [0, y_scale]])

    scaled_polygon = np.matmul(polygon, scaling_matrix)

    print("Scaled Polygon Coordinates:")

    for i in range(num_sides):
        print("({}, {})".format(scaled_polygon[i][0], scaled_polygon[i][1]))


scale_polygon()

