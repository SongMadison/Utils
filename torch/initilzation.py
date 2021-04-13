import torch
from torch import nn
import tensor

# random init
w1 = torch.randn(784, 50) 
b1 = torch.randn(50)

def linear(x, w, b):
    return x.matmul(w) + b

t1 = linear(x, w1, b1)
print(t1.mean(), t1.std())
############# output ##############
tensor(3.5744) tensor(28.4110)



#torch.nn.init.uniform_(tensor, a=0.0, b=1.0)

w = torch.empty(3, 5)
nn.init.uniform_(w)
