def non_duplicate(string):
    hash_table = {}
    for letter in string:
        hash_table[letter] = hash_table.get(letter, 0) + 1
    
    for key, element in hash_table.items():
        if element == 1:
            return key
        

print(non_duplicate("minimum"))