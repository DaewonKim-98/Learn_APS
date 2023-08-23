T = int(input())

for case in range(1, T + 1):
    N = float(input())
    # N이 2진수로 바뀐다는 것은 N의 마지막이 x*2^12로 끝난다는 뜻이므로
    # N에 2 ** 12를 곱했을 때 2진수로 나타낼 수 있다.
    N = N * (2 ** 12)
    output = ''
    # 만약 곱했는데 정수가 되지 않는다면 12자리 이내의 이진수로 나타날 수 없다는 뜻
    if N != int(N):
        print(f'#{case} overflow')
    else:
        for j in range(11, -1, -1):
            if int(N) & (1 << j):
                output += '1'
            else:
                output += '0'
        print(f'#{case}', end=' ')
        # 가장 뒤에 1 이후의 0은 삭제해야 하므로
        output = list(output)
        while output[-1] != '1':
            output.pop()
        for i in output:
            print(i, end='')
        print()