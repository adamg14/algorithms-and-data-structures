def bubble_sort(array):
    # initially the whole array is unsorted
    unsorted_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # if we have a walkthrough we a swap
                sorted = False
        unsorted_index -= 1
    
    return array


print(bubble_sort([4, 2, 7, 1, 3]))