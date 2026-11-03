import numpy as np
#---------------------------------------------------
# step  1  create  6 x 6 image
#---------------------------------------------------

image = np.array([
    [0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0],
    [0 ,0 ,0 ,0 ,0 ,0],
    [255 ,255 ,255 ,255 ,255 ,255],
    [255 ,255 ,255 ,255 ,255 ,255],
    [255 ,255 ,255 ,255 ,255 ,255],
])

print("\n original 6x6 image")
print(image)

#---------------------------------------------------
# step  2  : 3x3 kernal for horizontal Edge Detection
#---------------------------------------------------

kernel = np.array([
    [-1,-1,-1],
    [ 0 ,0 ,0],
    [ 1, 1, 1],
])

print("\n 3x3 Kernel")
print(kernel)

#---------------------------------------------------
# step  3  : convolution operation
# output size  = (6-3+1) X  (6-3+1) = 4x4
#---------------------------------------------------

feature_map = np.zeros((4,4))

for i in range(4):
    for j in range(4):
        # Extract  3x3 region
        region = image[i: i+3,j: j+3]

        # multiply and sum
        result = np.sum(region * kernel)

        # store result
        feature_map[i][j] = result

#---------------------------------------------------
# step  4  : show feature map
#---------------------------------------------------

print("\n Feature map (Detected Edge)")
print(feature_map)








