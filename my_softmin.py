import torch
from torch import nn
m = nn.Softmin()
x = torch.randn(2, 3)
y = m(x)
print(x)
print(y)