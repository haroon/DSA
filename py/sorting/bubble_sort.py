from py.util.util import get_random_int_list, make_comparator



def naive_bubble_sort(lst, ascending=True):
    """Naive implementation of the bubble sort algorithm.

    Repeatedly iterate through a list. In each iteration, compares two adjacent list items and swap
    them if not in correct order. If in a iteration no swap occurs, the list has been sorted. Break.

    Example:
        sorted_lst = naive_bubble_sort(get_random_int_list())

    Attributes:
        lst (list[int]): List on integers.
        ascending (bool): Sort order.

    Returns:
        List of sorted integers.
    """
    # lst_size = len(lst)
    compare = make_comparator(ascending)
    while True:
        swapped = False
        for i in range(1, len(lst)):
            # if lst[i - 1] > lst[i]:
            if compare(lst[i - 1], lst[i]):
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                swapped = True
        if not swapped:
            break

    return lst
