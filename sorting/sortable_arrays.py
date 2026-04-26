# quick sort implementation
def partition(array, low, high):
    # pivot is set to the last element in the array
    pivot = high
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)

array = [0, 5, 2, 1, 6, 3]
quick_sort(array, 0, len(array) - 1)
print(array)