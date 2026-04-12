from abstract_data_types.stack import Stack

def reverse_string(string):
    reverse_stack = Stack()

    for char in string:
        reverse_stack.push(char)
    
    reverse_string = ""
    while not reverse_stack.is_empty():
        reverse_string += reverse_stack.pop()
    
    return reverse_string

print(reverse_string("abc"))