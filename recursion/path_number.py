def path_numbers(n):
    # can take 1, 2 or 3 steps
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return path_numbers(n - 1) + path_numbers(n - 2) + path_numbers(n - 3)
    
print(path_numbers(5))