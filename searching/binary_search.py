def binary_search(sorted_array, search_element):
    # extract check for sorted array
    # (the assumption for binary search is that the array is sored)
    if sorted_array != sorted(sorted_array):
        return False
    else:
        low_index = 0
        high_index = len(sorted_array) - 1

        while low_index <= high_index:
            mid_index = low_index + (high_index - low_index) // 2
            if search_element == sorted_array[mid_index]:
                return mid_index
            elif search_element > sorted_array[mid_index]:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
        
        return False
    

print(binary_search([1, 2, 3], 3))
print(binary_search([1, 2, 3, 4], 2))
print(binary_search([1, 2, 3, 4], 3))
print(binary_search([1, 2, 3, 4], 5))