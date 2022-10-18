from PIL import Image
import numpy as np
import math

matrix = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]

def Average(coordX, coordY):
    sum = 0
    xx = 0
    yy = 0

    for x in [coordX-1, coordX, coordX+1]:
        for y in [coordY-1, coordY, coordY+1]:

            if (y < 0 or y > 99) or (x < 0 or x > 99):
                sum += 126 * matrix[xx][yy]
                yy = yy + 1
            else:
                sum += array[x][y] * matrix[xx][yy]
                yy = yy + 1

        xx = xx + 1
        yy = 0

    return int(sum)

image = Image.open("gray18.png")
array = np.asarray(image)
result = np.zeros(shape=(100, 100), dtype="uint8")

for i in range(100):
    for j in range(100):
        result[i][j] = math.fabs(int(Average(i, j)) - int(array[i][j]))

image = Image.fromarray(result)
image.save("new_image.png")