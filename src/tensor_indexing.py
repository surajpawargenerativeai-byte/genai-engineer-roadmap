import torch

def main():
    x = torch.tensor([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])

    print("Starting my GenAI engineer roadmap.")
    print("\nMatrix:")
    print(x)

    print("\nFirst row:")
    print(x[0])

    print("\nSecond column:")
    print(x[:, 1])

    print("\nTop-left 2x2 block:")
    print(x[0:2, 0:2])

if __name__ == "__main__":
    main()