def every_other(low, high):
    # base case (terminates the recursion)
    if low > high:
        return
    else:
        print(low)
        every_other(low + 2, high)

print(every_other(0, 10))