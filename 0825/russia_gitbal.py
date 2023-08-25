T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # 새로 칠해야 하는 칸 개수
    min_new = N * M
    # 3 구간으로 나눠서 범위 계산
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            new = 0
            # 흰색 깃발이 아니면 count
            for r in range(i + 1):
                for c in range(M):
                    if arr[r][c] != 'W':
                        new += 1
            # 흰색 깃발이 아니면 count
            for r in range(i + 1, j + 1):
                for c in range(M):
                    if arr[r][c] != 'B':
                        new += 1
            # 흰색 깃발이 아니면 count
            for r in range(j + 1, N):
                for c in range(M):
                    if arr[r][c] != 'R':
                        new += 1
            if min_new > new:
                min_new = new
    print(f'#{case} {min_new}')