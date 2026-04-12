# implementation of memoization in recursion to remove unecessary calls
def fibbonaci_sequence(n, memo={}):
    if n == 0 or n == 1:
        return n
    else:
        if not memo.get(n):
            memo[n] = fibbonaci_sequence(n - 1, memo) + fibbonaci_sequence(n - 2, memo)
        else:
            return memo.get(n)
        return memo[n]
    

print(fibbonaci_sequence(6))