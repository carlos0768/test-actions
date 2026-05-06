from src.module import add, greet, is_even


def test_add_returns_sum():
    assert add(2, 3) == 5
    assert add(-1, 1) == 1


def test_is_even_checks_even_numbers():
    assert is_even(4) is True
    assert is_even(7) is False


def test_greet_returns_message_with_name():
    assert greet("Carlo") == "Hello, Carlo!"


def test_greet_uses_guest_for_blank_name():
    assert greet("   ") == "Hello, guest!"
