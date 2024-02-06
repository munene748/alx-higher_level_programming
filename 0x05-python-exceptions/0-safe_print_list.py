#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.

    """
    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass

    print()  # Print a new line after printing the elements
    return printed_elements


if __name__ == "__main__":
    # Test the safe_print_list function
    my_list = [1, 2, 3, 4, 5]
    nb_print = safe_print_list(my_list, 2)
    print("nb_print:", nb_print)

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print:", nb_print)

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print:", nb_print)
