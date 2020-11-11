```
>>>import torch
>>> x = torch.Tensor(1)
>>> print(f"{x:0.5f}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/sonwang/anaconda3/lib/python3.7/site-packages/torch/tensor.py", line 419, in __format__
    return object.__format__(self, format_spec)
TypeError: unsupported format string passed to Tensor.__format__
>>> x.shape
torch.Size([1])
>>> print(f"{x.item():0.5f}")
0.00000
>>> x
tensor([1.3272e-09])
--------------------------------
>>> x = torch.tensor(1)
>>> print(f"{x:0.5f}")
1.00000
>>> x.shape
torch.Size([])
```

To Summarize:
1. torch.Tensor is data type, torch.Tensor(1,2) is generating tensors with dimension of 1x2
2. torch.tensor(data) is creating torch.Tensor() object.

https://stackoverflow.com/questions/51911749/what-is-the-difference-between-torch-tensor-and-torch-tensor


In PyTorch `torch.Tensor` is the main tensor class. So all tensors are just instances of `torch.Tensor`.

When you call `torch.Tensor()` you will get an empty tensor without any data.

In contrast `torch.tensor` is a function which returns a tensor. In the documentation it says:

```torch.tensor(data, dtype=None, device=None, requires_grad=False) → Tensor```

Constructs a tensor with data.

This also also explains why it is no problem creating an empty tensor instance of `torch.Tensor` without `data` by calling:
```tensor_without_data = torch.Tensor()```
But on the other side:

```tensor_without_data = torch.tensor()```
Will lead to an error:

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-12-ebc3ceaa76d2> in <module>()
----> 1 torch.tensor()

TypeError: `tensor()` missing 1 required positional arguments: "data"
But in general there is no reason to choose `torch.Tensor` over `torch.tensor`. Also `torch.Tensor` lacks a docstring.
Similar behaviour for creating a tensor without data like with: torch.Tensor() can be achieved using:

`torch.tensor(())`
Output:
`tensor([])`
