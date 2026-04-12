def count_x(string):
    if len(string) == 1:
        if string[0].lower() == "x":
            return 1
        else:
            return 0
    else:
        if string[0].lower() == "x":
            return 1 + count_x(string[1:])
        else:
            return 0 + count_x(string[1:])