import numpy as np

def Relu(z):
    return max(0,z)

def Marvellous_neuron_forward(inputs, weight,bias):
    pass

def main():
    print("marvellous nural network")

    input = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    Marvellous_neuron_forward(input,weights,bias)
    
    print("inputs are (I):",input)

    print("Weight are: (W)",weights)

    print("bias is (b)",bias)
    z = 0

    for i in range(len(input)):
        z = z +(input[i] * weights[i])

    z = z + bias

    #z = sum(w * x for w , x in zip(weights,input)) + bias

    print("Wighted sum:",z)

    y = Relu(z)

    return y








if __name__ == "__main__":
    main()