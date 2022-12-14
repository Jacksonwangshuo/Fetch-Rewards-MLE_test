import numpy as np

def image_pixel_coordinate(dim, corner_points):

    if dim[0] * dim[1] <= 0 or not isinstance(dim[0], int) or not isinstance(dim[1], int):
        raise ValueError('Image dimensions should be positive integer!')
    if len(corner_points) != 4:
        raise ValueError('Please enter 4 corner points!')

    corner_points.sort(key=lambda x: (x[0], x[1]))

    x_start, x_end = corner_points[0][0], corner_points[-1][0]
    y_start, y_end = corner_points[-1][1], corner_points[0][1]
    x = list(np.linspace(x_start, x_end, num=dim[1], endpoint=True))
    y = list(np.linspace(y_start, y_end, num=dim[0], endpoint=True))

    xv, yv = np.meshgrid(x, y)

    res = []
    for i in range(len(xv)):
        res.append([list(a) for a in zip(xv[i], yv[i])])

    return res