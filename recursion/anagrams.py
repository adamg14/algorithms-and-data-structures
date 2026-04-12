def anograms(string):
    if len(string) == 1:
        return [string]
    
    collections = []

    substring = anograms(string[1:])

    for sub in substring:
        for index in range(len(sub) + 1):
            new_string = sub[:index] + string[0] + sub[index:]
            collections.append(new_string)
    return collections


print(anograms("abc"))