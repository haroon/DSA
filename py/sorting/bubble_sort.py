from util.util import get_random_int_list, make_comparator



def naive_bubble_sort(lst, ascending=True):
    """Naive implementation of the bubble sort algorithm.

    Repeatedly passes over a list. In each pass, compares two adjacent list items and swap them
    if not in correct order. If no swap occurs during a pass, the list has been sorted. Break.

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
            if compare(lst[i - 1], lst[i]):
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                swapped = True
        if not swapped:
            break

    return lst

def optimized_bubble_sort(lst, ascending=True):
    """Optimized implementation of bubble sort.

    Takes into account fact that with after every pass, n largest items (or smallest, based on
    ascending order) are in correct order which means with each pass, we can ignore last n elements
    sorted from the last comparison pass.

    Example:
        sorted_lst = optimized_bubble_sort(get_random_int_list())

    Attributes:
        lst (list[int]): List on integers.
        ascending (bool): Sort order.

    Returns:
    """

    compare = make_comparator(ascending)
    comp_count = len(lst)
    while True:
        new_count = 0
        for i in range(1, comp_count):
            if compare(lst[i - 1], lst[i]):
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                new_count = i

        comp_count = new_count  # in next pass, compare just before the last swapped element.
        if comp_count == 0:
            break

    return lst
