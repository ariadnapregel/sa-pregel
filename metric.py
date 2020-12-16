import math
from scipy.spatial.transform import Rotation as R
import numpy as np

#load txt file

def metric(DifodoFilePath):
    with open(DifodoFilePath) as f:
        lines = f.readlines()

    #speicher Distancia y winkelgeschw como referencia
    omega = 3 #deg/s
    r = 1.9 #m

    #coger un timestamp - escoger file
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

    #Rotationen - Drehachse = y_achse, vector [0,1,0]
    rotaxis_ref = np.array([0, 1, 0])

    #from difodo
    x = float(second_pose[1])
    y = float(second_pose[2])
    z = float(second_pose[3])

    #formel from quaternion zu drehachse
    #1 quaternions
    qx = float(second_pose[4])
    qy = float(second_pose[5])
    qz = float(second_pose[6])
    qw = float(second_pose[7])

    r = R.from_quat([qx, qy, qz, qw])
    axis = r.as_rotvec()
    rotaxis = axis/np.sqrt(np.sum(axis**2))


    #euclidean distance
    d = math.sqrt((x - x_ref) ** 2 + (y - y_ref) ** 2 + (z - z_ref) ** 2) + (1-np.dot(rotaxis, rotaxis_ref))

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
