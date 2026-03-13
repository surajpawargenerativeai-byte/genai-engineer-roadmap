import torch

a = torch.tensor([[1, 2, 3], [4, 5, 6]])
row = torch.tensor([10, 20, 30])
col = torch.tensor([100, 200]).reshape(2, 1)

print("Original matrix:")
print(a)

print("\nMatrix + row vector:")
print(a + row)

print("\nMatrix + column vector:")
print(a + col)