#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer followed by a new line.

    Args:
        value: The value to print.

    Returns:
        bool: True if value has been correctly printed,
              False otherwise.

    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False


if __name__ == "__main__":
    # Test the safe_print_integer_err function
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
