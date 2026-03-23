import torch


def describe_split(name: str, X: torch.Tensor, y: torch.Tensor) -> None:
    print(f"{name} features shape: {X.shape}")
    print(f"{name} labels shape: {y.shape}")
    print("-" * 30)


def describe_batch(batch_X: torch.Tensor, batch_y: torch.Tensor) -> None:
    print("Batch features:")
    print(batch_X)
    print("Batch features shape:", batch_X.shape)
    print("\nBatch labels:")
    print(batch_y)
    print("Batch labels shape:", batch_y.shape)
    print("-" * 30)