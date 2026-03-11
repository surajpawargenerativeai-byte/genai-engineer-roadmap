def greet(name: str) -> str:
    """Return a greeting for a given name."""
    return f"Hello, {name}"

def square(x: int) -> int:
    """Return the square of an integer."""
    return x * x

def is_even(x: int) -> bool:
    """Return True if x is even, else False."""
    return x % 2 == 0

def safe_divide(a: float, b: float) -> float:
    """Safely divide a by b."""
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b