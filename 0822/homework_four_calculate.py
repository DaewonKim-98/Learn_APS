T = 10

# 후위순회로 계산하기 편하게 한다.
def postorder_travel(n):
    if len(tree[n]) == 1:
        susik.append(tree[n][0])
    elif len(tree[n]) == 3:
        postorder_travel(tree[n][1])
        postorder_travel(tree[n][2])
        susik.append(tree[n][0])

for case in range(1, T + 1):
    N = int(input())
    tree = {}
    for _ in range(N):
        arr = list(map(str, input().split()))
        # arr의 길이가 4면 연산자가 있는 것이므로
        if len(arr) == 4:
            node, operater, ch1, ch2 = arr
            tree[int(node)] = [operater, int(ch1), int(ch2)]
        else:
            node, value = arr
            tree[int(node)] = [int(value)]

    # 루트정점은 1
    n = 1
    # 연산할 수식
    susik = []
    stack = []
    inorder_travel(n)

    # 연산
    for x in susik:
        if str(x) not in '*+-/': # 피연산자면
            stack.append(x)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if x == '+':
                stack.append(op1 + op2)
            elif x == '*':
                stack.append(op1 * op2)
            elif x == '-':
                stack.append(op1 - op2)
            elif x == '/':
                stack.append(op1 / op2)

    # 계산 한 값 출력
    print(f'#{case} {int(stack[0])}')
