T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상하좌우 방향
    dir1 = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    # 대각선 방향
    dir2 = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    # 최대의 파리 수
    max_fly = 0
    # 배열을 돌면서 파리 잡기
    for r in range(N):
        for c in range(N):
            # 한 좌표에 대해 잡을 수 있는 파리의 합
            # 처음은 좌표의 파리 수
            sum_fly = arr[r][c]
            # 상하좌우로 잡을 때
            for d in dir1:
                # 스프레이의 세기
                for m in range(1, M):
                    # 델타탐색으로 스프레이로 잡는 파리들 탐색
                    nr, nc = r + d[0] * m, c + d[1] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
            # 최대의 파리 수 갱신
            if max_fly < sum_fly:
                max_fly = sum_fly

            sum_fly = arr[r][c]
            # 대각선으로 잡을 때
            for d in dir2:
                # 스프레이의 세기
                for m in range(1, M):
                    # 델타탐색으로 스프레이로 잡는 파리들 탐색
                    nr, nc = r + d[0] * m, c + d[1] * m
                    if 0 <= nr < N and 0 <= nc < N:
                        sum_fly += arr[nr][nc]
            # 최대의 파리 수 갱신
            if max_fly < sum_fly:
                max_fly = sum_fly

    print(f'#{case} {max_fly}')