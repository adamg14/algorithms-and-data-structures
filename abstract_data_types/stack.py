class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack) == 0:
            return "stack is currently empty"
        else:
            return self.stack.pop()
    
    def read(self):
        if len(self.stack) == 0:
            return "stack is currently empty"
        return self.stack[-1]