from neura.layers import DenseLayer
from neura.optimizers import SGD, MomentumSGD
from neura.activation_functions import Sigmoid,LeakyReLU
from neura.network import Network
from neura.loss_functions import MSE, BinaryCrossEntropy
import numpy as np


def main():
    l1 = DenseLayer(1,50,Sigmoid())
    l2 = DenseLayer(50,50, Sigmoid())
    l3 = DenseLayer(50,1,LeakyReLU())

    n = Network(MSE(), MomentumSGD(0.000001, 0.9))
    n.add_layer(l1)
    n.add_layer(l2)
    n.add_layer(l3)

     
    func = lambda x : x**2


    inp = np.linspace(0,10,10000).astype(np.float64)
    inp = np.reshape(inp,(-1,1))
    out = func(inp)

    
    n.fit(inp,out,epochs = 700,batch_size = 32) 

    import matplotlib.pyplot as plt
    plt.plot(func(inp))
    plt.plot(n.predict(inp))
    plt.show()






if __name__ == "__main__":
    main()
