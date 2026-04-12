def sum(low, high):
    if low == high:
        return low
    else:
        return high + sum(low, high - 1)

print(sum(1, 10))