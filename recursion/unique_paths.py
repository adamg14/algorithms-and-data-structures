def unique_paths(rows, columns, memo=None):
    if memo is None:
        memo = {}
    if rows == 1 or columns == 1:
        return 1
    else:
        if not memo.get((rows, columns)):
            memo[(rows, columns)] = unique_paths(rows - 1, columns, memo) + unique_paths(rows - 1, columns, memo)
        else:
            memo.get((rows, columns))
    return memo[(rows, columns)]


