def total_number(array):
    if len(array) == 1:
        return len(array[0])
    else:
        return len(array[0]) + total_number(array[1:])

print(total_number(["ab", "c", "def", "ghji"]))

