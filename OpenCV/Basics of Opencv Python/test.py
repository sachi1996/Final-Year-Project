import cv2
import numpy as np
import matplotlib.pyplot as plt

rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)

arr[0][] = 'a'

cv2.waitKey(0)
cv2.destroyAllWindows()
