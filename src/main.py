from utils import greet, square, is_even, safe_divide


def main() -> None:
    print(greet("Suraj"))
    print(f"Square of 6: {square(6)}")
    print(f"Is 10 even? {is_even(10)}")
    print(f"10 / 2 = {safe_divide(10, 2)}")


if __name__ == "__main__":
    main()