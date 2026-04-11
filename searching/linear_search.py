def linear_search(array, search_element):
    for index, element in enumerate(array):
        if element == search_element:
            return index
        else:
            continue
    
    return False


print(linear_search([1, 2, 3], 2))
print(linear_search([1, 2, 3], 4))