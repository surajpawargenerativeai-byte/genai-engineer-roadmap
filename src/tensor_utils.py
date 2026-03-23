import torch


def describe_tensor(x: torch.Tensor) -> None:
    print("Tensor:")
    print(x)
    print("Shape:", x.shape)
    print("Dimensions:", x.ndim)
    print("Dtype:", x.dtype)
    print("-" * 30)


def main() -> None:
    scalar = torch.tensor(5)
    vector = torch.tensor([1, 2, 3])
    matrix = torch.tensor([[1, 2], [3, 4]])

    describe_tensor(scalar)
    describe_tensor(vector)
    describe_tensor(matrix)


if __name__ == "__main__":
    main()