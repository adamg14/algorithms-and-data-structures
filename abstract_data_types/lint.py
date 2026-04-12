from stack import Stack

class Lint:
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    lint_mapping = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    def __init__(self):
        self.lint_stack = Stack()
    
    def linter(self,text):
        self.lint_stack.clear()
        for character in text:
            if character not in Lint.opening and character not in Lint.closing:
                continue
            elif character in Lint.opening and character not in Lint.closing:
                self.lint_stack.push(character)
            else:
                # it is a closing character
                if self.lint_stack.is_empty():
                    return False
                else:
                    opening_char = self.lint_stack.pop()
                    if Lint.lint_mapping[opening_char] == character:
                        continue
                    else:
                        return False

        if self.lint_stack.is_empty():
            return True
        else:
            return False

            