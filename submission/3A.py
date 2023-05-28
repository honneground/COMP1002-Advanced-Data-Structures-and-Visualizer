import numpy as np

class Stack:
    def __init__(self):
        self.stack = np.array([])
        self.size = 0

    def push(self, item):
        self.stack = np.append(self.stack, item)
        self.size += 1

    def pop(self):
        if not self.is_empty():
            item = self.stack[-1]
            self.stack = self.stack[:-1]
            self.count -= 1
            return item

    def is_empty(self):
        return len(self.stack) == 0

    def count(self):
        return self.size
        

def check_expression(expression):
    try:
        left_side, right_side = expression.split('=')
        left_stack = parse_side(left_side)
        right_stack = parse_side(right_side)
        return left_stack.count() == right_stack.count()
    except:
        print("Illegal Input Expression!")
        return None
        

def parse_side(side):
    stack = Stack()
    term = ""
    sign_flag = False
    parentheses_flag = 0

    for char in side:
        if char == ' ':
            pass
        
        elif (char == '+' or char == '-') and sign_flag == False and parentheses_flag == 0 and term != "":
            stack.push(term)
            term = ""

        else:
            term += char
            if char == '*' or char == '/' or char == '^':
                sign_flag = True
                
            if char == '+' or char == '-' or char.isdigit():
                sign_flag = False

            if char == '(' :
                parentheses_flag += 1

            if char == ')' :
                parentheses_flag -= 1

    return stack

if __name__ == "__main__":
    # Test the function
    expressions = [
    "A + B + C = X - Y - Z ",
    "A + B - C = X + Y",
    "5x + -n(8.99*-8) = 6.354/20 + 80xy",
    "5x + 8.99 = 6.354/20 + 80xy + 2^99",
    "5x + 8.99 - + 9logn(e^-1) = 6.354/20 + 80xy - 3",
    "5x + 8.99 - y = 6.354/20 + 80xy - 9e(-3loge(k))",
    "Five x plus negative n times eight point nine nine times negative eight equals six point three five four divided by twenty plus eighty x y."]

    for expression in expressions:
        print(expression)
        print(check_expression(expression))
        print()