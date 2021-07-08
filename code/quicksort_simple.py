import random
compare_count = 0


def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]

    compare = 0
    for j in range(start, end):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        # Increment compare count
        compare = compare + 1

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1, compare


def quicksort_runner(arr, start, end):
    """[summary]

    Args:
        arr (list): [Array to be sorted]
        start (int): [start index]
        end (int): [end index]

    Returns:
        [int]: [# Comparisions for sorting array between start & end]
    """
    global compare_count
    compare = 0

    if start < end:
        # Compare once
        pivot_index = random.randint(start, end)
        arr[pivot_index], arr[start] = arr[start], arr[pivot_index]
        compare_count += 1

        pivot_index, compare = partition(arr, start, end)

        # Divide and conquer !
        quicksort_runner(arr, start, pivot_index - 1)
        quicksort_runner(arr, pivot_index + 1, end)
    else:
        return None

    compare_count += compare

if __name__ == "__main__":
    arr = [9, 6, 4, 3, 4, 5, 6, 7, 8, 6, 90, 1, 2, 3, 5, 67, 4, 2, 2, 54, 6]
    val = quicksort_runner(arr, 0, len(arr) - 1)
    print(val)
