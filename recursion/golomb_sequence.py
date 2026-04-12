def golomb_sequence(n, memo={}):
    if n == 1:
        return n
    else:
        if not memo.get(n):
            memo[n] = 1 + golomb_sequence(n - golomb_sequence(n - 1, memo), memo)
        else:
            return memo.get(n)
    return memo[n]

print(golomb_sequence(6))