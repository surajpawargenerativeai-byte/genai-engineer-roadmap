import torch
from torch import nn

class CreditNet(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x
    

def main():
    model = CreditNet()

    x = torch.tensor([
        [50000.0, 29.0, 10000.0, 1.0],
        [70000.0, 31.0, 7000.0, 0.0]
    ])

    output = model(x)

    print("Input:")
    print(x)
    print("Input shape:", x.shape)

    print("\nOutput:")
    print(output)
    print("Output shape:", output.shape)

if __name__ == "__main__":
    main()