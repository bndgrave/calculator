class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        value = self.items.pop()
        return value


class Calculator:
    def __init__(self,expression:str):
        self.expression = expression
        self.operators = Stack()
        self.operands = Stack()
    
    def decode_expression(self):
        items = self.expression.split(' ')
        for item in items:
            if item.isdigit():
                self.operands.push(item)
            else:
                self.operators.push(item)

    def calc_result(self):
        while not self.operators.is_empty():
            operator = self.operators.pop()
            operands = [self.operands.pop() for index in range(2)]
            self.operands.push(
                str(
                    eval(operands[1] + operator + operands[0])
                )
            )
        return int(self.operands.pop())
