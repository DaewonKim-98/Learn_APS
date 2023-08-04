T = int(input())

for case in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N


    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        # L 과 R 번째의 인덱스만큼 box 를 i로 바꾼다.
        for j in range(L - 1, R):
            box[j] = i

    print(f'#{case}', end=' ')
    for k in range(N):
        print(box[k], end=' ')
    print()