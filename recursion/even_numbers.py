def even_numbers(numbers):
    if len(numbers) == 0:
        return 0
    else:
        if numbers[0] % 2:
            return 1 + even_numbers(numbers[1:])
        else:
            return even_numbers(numbers[1:])

print(even_numbers([2, 2, 3]))