import tensorflow as tf

inputs = tf.constant([1.0,2.0,3.0])

weights = tf.constant([0.5,-0.2,0.8])

bias = tf.constant(0.1)

weighted_sum = tf.reduce_sum(inputs * weights) +  bias

print("inputs :",inputs.numpy())   # 1.0,2.0,3.0

print("Weights :",weights.numpy())  # 0.5

print("Bias is :",bias.numpy())

print("weighted sum :",weighted_sum.numpy())

output  = tf.sigmoid(weighted_sum)

print("output is :",output.numpy())

