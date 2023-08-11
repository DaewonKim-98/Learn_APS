T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    length_list = []
    # 행 우선 탐색
    for r in range(N):
        length = 1
        for c in range(M - 1):
            # 연속되게 1이 있으면
            if arr[r][c] == 1 and arr[r][c + 1] == 1:
                length += 1
        length_list.append(length)

    # 열 우선 탐색
    for c in range(M):
        length = 1
        for r in range(N - 1):
            # 연속되게 1이 있으면
            if arr[r][c] == 1 and arr[r + 1][c] == 1:
                length += 1
        length_list.append(length)

    max_value = 0
    for i in length_list:
        if max_value < i:
            max_value = i

    print(f'#{case} {max_value}')
