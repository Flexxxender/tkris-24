def tokenize(expression):
    """Разбиваем выражение на токены"""
    tokens = []
    current_number = ''
    
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                tokens.append(int(current_number))
                current_number = ''
            if char in '+-*/()':
                tokens.append(char)
            elif not char.isspace():
                raise ValueError(f"Неподдерживаемый символ: '{char}'")
    
    if current_number:
        tokens.append(int(current_number))
    
    return tokens

def shunting_yard(tokens):
    """Преобразуем в обратную польскую нотацию"""
    if not tokens:
        raise ValueError("Нет токенов для обработки")
    
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    parentheses_count = 0
    
    for token in tokens:
        if isinstance(token, int):
            output.append(token)
        elif token == '(':
            parentheses_count += 1
            operators.append(token)
        elif token == ')':
            parentheses_count -= 1
            if parentheses_count < 0:
                raise ValueError("Несбалансированные скобки")
            
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError("Несбалансированные скобки")
            operators.pop() 
        else:
            if not output and token in '*/':
                raise ValueError(f"Оператор '{token}' в неправильной позиции")
            
            while (operators and operators[-1] != '(' and 
                   precedence.get(operators[-1], 0) >= precedence.get(token, 0)):
                output.append(operators.pop())
            operators.append(token)
    
    if parentheses_count != 0:
        raise ValueError("Несбалансированные скобки")
    
    if not output:
        raise ValueError("Некорректное выражение")
    
    while operators:
        op = operators.pop()
        if op == '(':
            raise ValueError("Несбалансированные скобки")
        output.append(op)
    
    return output

def evaluate_rpn(tokens):
    """Вычисляем выражение в обратной польской нотации"""
    stack = []
    
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("Некорректное выражение: недостаточно операндов")
            
            b = stack.pop()
            a = stack.pop()
            
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
    
    if len(stack) != 1:
        raise ValueError("Некорректное выражение")
    
    return stack[0]

def calculate(expression):
    tokens = tokenize(expression)
    rpn_tokens = shunting_yard(tokens)
    return evaluate_rpn(rpn_tokens)