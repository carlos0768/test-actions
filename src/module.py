def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of two numbers."""
    return a + b


def is_even(number: int) -> bool:
    """Return True when number is even."""
    return number % 2 == 0


def greet(name: str) -> str:
    """Return a friendly greeting."""
    cleaned_name = name.strip()
    if not cleaned_name:
        return "Hello, guest!"
    return f"Hello, {cleaned_name}!"

print("Hello world")
print("Hello world")
