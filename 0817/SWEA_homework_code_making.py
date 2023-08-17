T = 10

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int ,input().split()))

    sub = 1
    # 마지막 숫자가 0보다 작거나 같으면 프로그램 종료
    while arr[-1] > 0:
        # 1부터 5까지 감소
        arr[0] = arr[0] - sub
        p = arr.pop(0)
        arr.append(p)

        sub += 1
        # sub는 5가 넘어가면 다시 1로 바뀐다.
        if sub > 5:
            sub = 1

    # 마지막 0으로 만듦
    arr[-1] = 0
    print(f'#{case}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()