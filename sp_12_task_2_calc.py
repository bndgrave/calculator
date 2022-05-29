# Номер посылки - 68684300

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


def calc_result(expression:str):
    elements = expression.split(' ')
    operands = Stack()
    for element in elements:
        if element.isdigit() or element[1:].isdigit():
            operands.push(element)
        else:
            operator = '//' if element == '/' else element
            pair_to_calc = [operands.pop() for index in range(2)]
            operands.push(
                str(
                    eval(pair_to_calc[1] + operator + pair_to_calc[0])
                )
            )
    return operands.pop()

if __name__ == '__main__':
    expression = input()
    result = calc_result(expression)
    print(result)
