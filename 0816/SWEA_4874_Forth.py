T = int(input())

for case in range(1, T + 1):
    susik = list(map(str, input().split()))
    stack = []
    result = 0

    for x in susik:
        if x == '.':
            break
        if x not in '+-/*':  # 피연산자면
            stack.append(int(x))
        else:
            # 스택이 1보다 작거나 같으면 정수에 비해 연산자가 많다는 것
            if len(stack) <= 1:
                result = 'error'
                break
            else:
                op2 = stack.pop()  # pop()
                op1 = stack.pop()  # pop()
                if x == '+':  # op1 + op2
                    stack.append(op1 + op2)
                elif x == '-':
                    stack.append(op1 - op2)
                elif x == '*':
                    stack.append(op1 * op2)
                elif x == '/':
                    stack.append(int(op1 / op2))
                result = stack[0]
    # 스택의 개수가 1개보다 크면 정수가 연산자에 비해 많다는 것
    if len(stack) > 1:
        result = 'error'
    print(f'#{case} {result}')