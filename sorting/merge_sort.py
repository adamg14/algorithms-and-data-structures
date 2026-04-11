def merge_sort(array_1, array_2):
    new_array = []
    array_1_pointer = 0
    array_2_pointer = 0
    while array_1_pointer < len(array_1) or array_2_pointer < len(array_2):

        if array_1_pointer > len(array_1):
            new_array.append(array_2[array_2_pointer])
            array_2_pointer += 1
        elif array_2_pointer > len(array_2):
            new_array.append(array_1[array_1_pointer])
            array_1_pointer += 1
        else:
            if array_1[array_1_pointer] > array_2[array_2_pointer]:
                new_array.append(array_2[array_2_pointer])
                array_2_pointer += 1
            elif array_1[array_1_pointer] < array_2[array_2_pointer]:
                new_array.append(array_1[array_1_pointer])
                array_1_pointer += 1
            else:
                new_array.append(array_1[array_1_pointer])
                new_array.append(array_2[array_2_pointer])
                array_1_pointer += 1
                array_2_pointer += 1
    
    return new_array


print(merge_sort([1, 2, 3, 4], [1, 2, 3, 4]))