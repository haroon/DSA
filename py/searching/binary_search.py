def binary_search(haystack, needle):
    """Implementation of binary search algorithm.
    
    Performs binary search on a sorted list and returns the index of item in the list.

    Example:
        lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        index = binary_search(lst, 21)  # index == -1
        index = binary_search(lst, 3)  # index == 3 

    Attributes:
        haystack (list): A sorted list.
        needle: Item to search.

    Returns:
        Index of the item to be found or -1 if item does not exist in the list.
    """
    lb = 0
    ub = len(haystack) - 1
    while ub >= lb:
        mid = (ub + lb) // 2
        if haystack[mid] < needle:
            lb = mid + 1
        elif haystack[mid] > needle:
            ub = mid - 1
        else:
            return mid
    return -1
