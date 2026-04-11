def path_finder(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    else:
        return path_finder(rows - 1, columns) + path_finder(rows, columns - 1)
    

print(path_finder(3, 3))
print(path_finder(2, 2))

