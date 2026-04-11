def insertion_sort(array):
    for i in range(1, len(array)):
        temp_value = array[i]

        position = i - 1
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                array[position] = temp_value
                position -= 1
            else:
                break
    
    return array


print(insertion_sort([1, 2, 3, 4]))
print(insertion_sort([8, 4, 2, 3]))