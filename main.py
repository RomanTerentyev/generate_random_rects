import numpy as np
import cv2
import random

height = random.randint(500, 1000)
width = random.randint(500, 1000)
num_polygons = random.randint(2, 1000)

img = np.zeros((height, width, 3), dtype='uint8')
polygons = [[(0, 0), (width, height)]]

while len(polygons) < num_polygons:
    #cur_poly_index = random.randint(0, len(polygons) - 1)
    cur_poly_index = 0
    max_area = 0
    for i in range(len(polygons) - 1):
        polygon = polygons[i]
        area = (polygon[1][0] - polygon[0][0]) * (polygon[1][1] - polygon[0][1])
        if area > max_area:
            max_area = area
            cur_poly_index = i
    x0, y0 = polygons[cur_poly_index][0]
    w, h = polygons[cur_poly_index][1]
    #split = random.choice(['hor', 'ver'])
    split = 'ver' if w - x0 > h - y0 else 'hor'
    if split == 'hor':
        y = random.randint(y0, h)
        new_polygons = [[(x0, y0), (w, y)],
                        [(x0, y), (w, h)]]
    elif split == 'ver':
        x = random.randint(x0, w)
        new_polygons = [[(x0, y0), (x, h)],
                        [(x, y0), (w, h)]]        
    polygons.extend(new_polygons)
    del polygons[cur_poly_index]

for polygon in polygons:
    color = [random.randint(0, 256) for _ in range(3)]
    img = cv2.rectangle(img, polygon[0], polygon[1], color, -1)
    
cv2.imwrite('random.png', img)
