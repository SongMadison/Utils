import torch
# unif(0,1)
torch.rand(3,4)


#bmm: batch matrix-matrix product, doesn't broadcast
# Norm(0,1)
input = torch.randn(10, 3, 4)
mat2 = torch.randn(10, 4, 5)
res = torch.bmm(input, mat2)
res.size()
#torch.Size([10, 3, 5])

#torch.matmul(input, other, *, out=None) → Tensor