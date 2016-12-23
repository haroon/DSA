from ..util.util import get_random_int_list


def naive_bubble_sort(lst):
    """Naive implementation of the bubble sort algorithm.

    Example:
        sorted_lst = naive_bubble_sort(get_random_int_list())

    Attributes:
        lst (list[int]): List on integers.

    Returns:
        List of sorted integers.
    """
    # lst_size = len(lst)
    for i in range(1, len(lst) - 1):
        if lst[i - 1] > lst[i]:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]