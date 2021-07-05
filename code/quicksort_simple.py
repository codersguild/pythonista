compare_count = 0

def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]
    # pivot = arr[random.randint(start, end)] # For randomized QuickSort
    
    compare = 0
    for j in range(start, end):
        if arr[j] <= pivot:
            compare = compare + 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1, compare


def quicksort_runner(arr, start, end):
    compare = 0
    if len(arr) == 1:
        return arr
    if start < end:
        pivot_index, compare = partition(arr, start, end)

        # Divide and conquer !
        quicksort_runner(arr, start, pivot_index - 1)
        quicksort_runner(arr, pivot_index + 1, end)

    global compare_count
    compare_count = compare + compare_count
    return compare_count

if __name__ == "__main__":
    arr = [9, 6, 4, 3, 4, 5, 6, 7, 8, 6, 90, 1, 2, 3, 5, 67, 4, 2, 2, 54, 6]
    val = quicksort_runner(arr, 0, len(arr) - 1)
    print(val)
