def add_until_100(array, memo=None):
    if memo is None:
        memo = {}
    key = tuple(array)

    if key in memo:
        return memo[key]
    
    if len(array) == 0:
        return 0
    
    if array[0] + add_until_100(array[1:], memo) > 100:
        result =  add_until_100(array[1:], memo)
    else:
        result = array[0] + add_until_100(array[1:], memo)
    
    memo[key] = result
    return result

print(add_until_100([20, 20, 20, 20, 20]))
print(add_until_100([20, 20, 20, 20, 20, 20]))
