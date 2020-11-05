>>> import torch
>>> x = torch.Tensor([0])
>>> x
tensor([0.])
>>> type(x)
<class 'torch.Tensor'>
>>> y = torch.Tensor([1])
>>> f" {x:0.5f} (best {y:0.5f}),"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sonwang/anaconda3/lib/python3.7/site-packages/torch/tensor.py", line 419, in __format__
    return object.__format__(self, format_spec)
TypeError: unsupported format string passed to Tensor.__format__
>>> f" {x.item():0.5f} (best {y.item():0.5f}),"
' 0.00000 (best 1.00000),'