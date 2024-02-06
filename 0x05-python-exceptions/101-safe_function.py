#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: The function to execute.
        *args: Variable length argument list to pas.
    Returns:
        Result of function if executed successfully, Else none.

    """
    try:
        return fct(*args)
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None


if __name__ == "__main__":
    # Test the safe_function function
    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div:", result)

    result = safe_function(my_div, 10, 0)
    print("result of my_div:", result)

    def print_list(my_list, len):
        i = 0
        while i < len:
            print(my_list[i])
            i += 1
        return len

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list:", result)
