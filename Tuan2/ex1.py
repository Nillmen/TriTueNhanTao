import numpy as np

arr = np.array([-2, 6, 3, 10, 15, 48])

arr1 = arr[2:5:2]
arr2 = arr[1::2]
arr3 = arr[3:]
arr4 = arr[:2:-1]
print(arr1)
print(arr2)
print(arr3)
print(arr4)