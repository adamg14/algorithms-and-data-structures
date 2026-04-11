def x_index(input_string, counter = 0):
    if len(input_string) == 0:
        return False
    else:
        if input_string[0].lower() == "x":
            return counter
        else:
            return x_index(input_string[1:], counter + 1)

print(x_index("x"))
print(x_index("abcxd"))
print(x_index("abcdx"))
