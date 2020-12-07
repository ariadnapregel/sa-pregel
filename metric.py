import math
#load txt file

def metric(DifodoFilePath):
    with open(DifodoFilePath) as f:
        lines = f.readlines()

    #speicher Distancia y winkelgeschw como referencia
    omega = 3 #deg/s
    r = 1.9 #m

    #coger un timestamp - eescoger file
    matrix_out = []
    column = []
    max_diff = 3 #TBD

    first_pose = lines[1].split()
    second_pose = lines[2].split()

    delta_t = second_pose[0] - first_pose[0]
    angle = delta_t * omega

    x_ref = math.sin(angle)
    z_ref = r - math.cos(angle)
    y_ref = 0

    #from difodo
    x = float(second_pose[1])
    y = float(second_pose[2])
    z = float(second_pose[3])

    #euclidean distance
    d = math.sqrt((x - x_ref) ** 2 + (y - y_ref) ** 2 + (z - z_ref) ** 2)

    # condition: distance > als maximum: label = not good
    column.append(second_pose[0])
    if d > max_diff:
        column.append('0')
    else:
        column.append('1')
    matrix_out.append(column)

    return matrix_out

if __name__ == '__main__':
    #shape_img = (720, 1280)
    metric(DifodoFilePath='trajectoryDIFODO.txt')

#berechnen Soll-Koordinaten (por referenzkoordinaten, Winkelgeschwindigkeit, timestamp)

#comparar con ist-Koordinaten en el timestamp


#condition > als tbd : crear label no good si good
