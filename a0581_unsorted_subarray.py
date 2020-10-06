def unsorted_subarray(array):
    #
    """
    """
    start, end = None, None
    current_min, current_max = None, None

    # Iterate through items
    for i in range(len(array) - 1):
        # Compare adjacent items and fill values if unsorted
        if start is None and end is None and array[i] > array[i + 1]:
            start = i
            end = i + 1
            current_min = array[i]
            current_max = array[i + 1]

        # If next item is smaller than current_min, need to sort to that point
        if current_min and array[i + 1] < current_min:
            end = i + 1
            current_min = array[i + 1]

        # If next item is smaller than current_max, need to sort to that point
        if current_max and array[i + 1] < current_max:
            end = i + 1

        # If next item is larger than current_max, update current_max
        if current_max and array[i + 1] > current_max:
            current_max = array[i + 1]

    return end - start + 1


if __name__ == "__main__":
    print(unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))
