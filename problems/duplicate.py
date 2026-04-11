def duplicate(array):
    hash_table = {}
    for element in array:
        if hash_table.get(element):
            return element
        else:
            hash_table[element] = True
        

print(duplicate(["a", "b", "c", "d", "c", "e"]))