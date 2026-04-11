def intersection(array_1, array_2):
    # calculating the intersection of two arrays
    # function has time complexity of O(N)
    hash_table = {}
    intersection = []
     
    for element in array_1:
        hash_table[element] = True
    
    for element in array_2:
        print(element)
        if hash_table.get(element, False):
            intersection.append(element)

    return intersection

print(intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))