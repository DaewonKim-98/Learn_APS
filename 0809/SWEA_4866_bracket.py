T = int(input())

for case in range(1, T + 1):
    sen = input()

    result = 1
    stack = []
    # 문장을 돌면서
    for letter in sen:
        # 글자가 ( 면 스택에 1 추가
        if letter == '(':
            stack.append(1)
        # 글자가 { 면 스택에 2 추가
        elif letter == '{':
            stack.append(2)
        # 글자가 ) 면 스택에서 마지막 것을 빼주는데 추가
        elif letter == ')':
            # stack 의 길이가 0이면 앞에 ( 가 없었다는 것이므로 종료
            if len(stack) == 0:
                result = 0
                break
            else:
                p = stack.pop()
                # 가장 뒤에 것이 2면 { 라는 것이므로 종료
                if p == 2:
                    result = 0
                    break
        # 글자가 ) 면 스택에서 마지막 것을 빼주는데 추가
        elif letter == '}':
            # stack 의 길이가 0이면 앞에 ( 가 없었다는 것이므로 종료
            if len(stack) == 0:
                result = 0
                break
            else:
                p = stack.pop()
                # 가장 뒤에 것이 2면 { 라는 것이므로 종료
                if p == 1:
                    result = 0
                    break

    # 다 돌았을 때 스택의 길이가 0이 아니면 짝을 못이룬 것
    if len(stack) != 0:
        result = 0

    print(f'#{case} {result}')
