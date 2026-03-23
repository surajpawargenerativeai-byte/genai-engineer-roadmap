import torch
from torch import nn


class CreditNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(4, 2)

    def forward(self, x):
        return self.linear(x)


def main():
    model = CreditNet()
    print(model)

    for name, param in model.named_parameters():
        print(f"\n{name}")
        print(param)
        print("Shape:", param.shape)

    x = torch.tensor([
        [50000.0, 29.0, 10000.0, 1.0],
        [70000.0, 31.0, 7000.0, 0.0]
    ])

    output = model(x)

    print("\nOutput:")
    print(output)
    print("Output shape:", output.shape)


if __name__ == "__main__":
    main()