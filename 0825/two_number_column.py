T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))

    if N <= M:
        max_sum = 0
        # N을 M에 맞게 돌리면서 곱의 합을 구한다.
        for i in range(M - N + 1):
            sum = 0
            for j in range(N):
                sum += nlist[j] * mlist[i + j]
            if max_sum < sum:
                max_sum = sum

    else:
        max_sum = 0
        # N을 M에 맞게 돌리면서 곱의 합을 구한다.
        for i in range(N - M + 1):
            sum = 0
            for j in range(M):
                sum += nlist[i + j] * mlist[j]
            if max_sum < sum:
                max_sum = sum

    print(f'#{case} {max_sum}')