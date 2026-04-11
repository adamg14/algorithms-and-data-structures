# Finding the greatest number in an array in O(N) time
def greatest_number(array):
    greatest_number = array[0]
    for i in range(1, len(array)):
        if array[i] > greatest_number:
            greatest_number = array[i]
        else:
            continue
    return greatest_number


print(greatest_number([1, 2, 3, 4]))
print(greatest_number([2, 4, 3, 1]))
