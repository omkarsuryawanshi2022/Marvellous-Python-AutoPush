import tensorflow as tf

# scallar tensor (0D tensor)
scallar_tensor = tf.constant(11)
print("Scallar tenar:",scallar_tensor)

# 1D tensar (vecter)
vecter_tensor = tf.constant([11,21,51,101])

print("vecter_tensor is :",vecter_tensor)

# 2D tensor(matrix)
matrix_tensor = tf.constant([[10,20,30], [40,50,60]])

print("matrix tensor is :",matrix_tensor)

# 3D Tensor

tensor_3rd = tf.constant([
    [[1,2] , [3,4]],
    [[5,5] , [6,6]],
    [[7,8] , [9,10]],
])

print("3D tensor :",tensor_3rd)

