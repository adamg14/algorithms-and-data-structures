def selection_sort(array):
    for i in range(len(array)):
        print(array)
        lowest_number_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                lowest_number_index = j
            else:
                continue
        if lowest_number_index != i:
            array[i], array[lowest_number_index] = array[lowest_number_index], array[i]

    
    return array



print(selection_sort([4, 3, 2, 1]))