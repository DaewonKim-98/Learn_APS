T = int(input())

for case in range(1, T + 1):
    arr = list(input())

    # arr 의 처음이 들어있는 스택을 만든다.
    stack = [arr[0]]

    for letter in range(1, len(arr)):
        if len(stack) > 0:
            # 만약 letter 가 stack 의 마지막에 있으면 stack 의 마지막을 없앤다.
            # 그러면 연속된 숫자가 제거됨
            if arr[letter] == stack[-1]:
                stack.pop()
            # 아니면 그냥 스택에 추가
            else:
                stack.append(arr[letter])

        # 스택의 개수가 0이면 그냥 추가
        elif len(stack) == 0:
            stack.append(arr[letter])

    print(f'#{case} {len(stack)}')