def missing_element(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    hash_table = {}
    for letter in string:
        hash_table[letter] = True

    for letter in alphabet:
        if hash_table.get(letter):
            continue
        else:
            return letter

print(missing_element("the quick brown box jumps over the lazy fox"))