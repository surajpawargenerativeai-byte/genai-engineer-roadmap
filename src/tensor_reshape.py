import torch

x = torch.arange(12)
print("Original:")
print(x)
print("Shape:", x.shape)

x_reshaped = x.reshape(3, 4)
print("\nReshaped to 3x4:")
print(x_reshaped)
print("Shape:", x_reshaped.shape)

flat = x_reshaped.reshape(-1)
print("\nFlattened:")
print(flat)
print("Shape:", flat.shape)