import numpy as np

def Sigmoid():
     pass

def Marvellous_neuron_forward(inputs, weight,bias):
    Marvellous_neuron_forward(input,weight,bias)
        
    print("inputs are (I):",input)
    
    print("Weight are: (W)",weight)
    
    print("bias is (b)",bias)
    z = 0
    
    for i in range(len(input)):
            
            z = z +(input[i] * weight[i])
    
            z = z + bias
    
        #z = sum(w * x for w , x in zip(weights,input)) + bias
    
            print("Wighted sum:",z)
    
            y = Sigmoid(z)
    
    return y
    

def main():
    print("marvellous nural network")

    input = [1.0,2.0,3.0]
    weights = [0.6,0.4,-0.2]
    bias = 0.5

    








if __name__ == "__main__":
    main()