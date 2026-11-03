import tensorflow as tf

tensor1 = tf.constant([10,20,30])

tensor2 = tf.constant([1,2,3])

addition  = tf.add(tensor1,tensor2)

print("Addition is :",addition)  # 11 22 33

subtraction  = tf.subtract(tensor1,tensor2)

print("subtraction is :",subtraction)  # 9 18 27

multiplication  = tf.multiply(tensor1,tensor2)

print("multiplication is :",multiplication)  # 10 40 90

divition  = tf.divide(tensor1,tensor2)

print("divition is :",divition)  # 10.0, 10.0 , 10.0

square = tf.square(tensor1)

print("square :",square)  # 100 ,400, 900

sum = tf.reduce_sum(tensor1)
print( "reduced sum:",sum)# 60

mean = tf.reduce_mean(tensor1)
print(" mean  is :",mean)   # 20






