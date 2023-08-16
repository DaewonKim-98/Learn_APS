T = 10

for case in range(1, T + 1):
    N = int(input())
    fx = list(input())
    stack = []
    susik = ''

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    for x in fx:
        if x not in '(+-*/)':
            susik += x
        elif x == ')':
            while stack[-1] != '(':
                susik += stack.pop()
        else:
            if len(stack) == 0 or isp[stack[-1]] < icp[x]:
                stack.append(x)
            elif isp[stack[-1]] >= icp[x]:
                while len(stack) > 0 and isp[stack[-1]] >= icp[x]:
                    susik += stack.pop()
                stack.append(x)

    # 스택의 남은 부분들을 다 수식으로
    for _ in range(len(stack)):
        susik += stack.pop()

    for x in susik:
        if x not in '+-/*':  # 피연산자면
            stack.append(int(x))
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
                stack.append(op1 / op2)
    print(f'#{case} {stack[0]}')