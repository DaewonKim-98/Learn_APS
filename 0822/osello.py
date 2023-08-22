T = int(input())

# 오셀로로 바뀌는 것은 상하좌우 대각선이므로
dir = [[0, -1], [-1, 0], [0, 1], [1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

for case in range(1, T + 1):
    N, M = map(int, input().split())
    # 바둑판은 인덱스가 1부터인 것을 생각해서 N + 1의 크기
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    # 미리 가운데에 배치
    arr[N // 2][N // 2] = 2
    arr[N // 2][N // 2 + 1] = 1
    arr[N // 2 + 1][N // 2] = 1
    arr[N // 2 + 1][N // 2 + 1] = 2

    for _ in range(M):
        c, r, egg = map(int, input().split())
        arr[r][c] = egg
        # 델타 탐색으로 자신과 같은 색을 찾아 그 사이의 색들을 바꾼다.
        for d in dir:
            # 탐색의 범위는 1부터 N - 1까지로 보드의 최대까지 볼 수 있도록
            for e in range(1, N):
                nr, nc = r + d[0] * e, c + d[1] * e
                # nr 과 nc는 보드 판을 벗어나면 안되므로
                if 1 <= nr < N + 1 and 1 <= nc < N + 1:
                    # 만약 같은 색이 나타나면
                    if arr[nr][nc] == egg:
                        # 가로로 탐색했을 때면
                        if nr == r:
                            if nc > c:
                                for i in range(e):
                                    if arr[r][c + i] == 0:
                                        break
                                else:
                                    for i in range(e):
                                        arr[r][c + i] = egg
                            else:
                                for i in range(e):
                                    if arr[r][c - i] == 0:
                                        break
                                else:
                                    for i in range(e):
                                        arr[r][c - i] = egg
                        # 세로로 탐색했을 때면
                        elif nc == c:
                            if nr > r:
                                for i in range(e):
                                    if arr[r + i][c] == 0:
                                        break
                                else:
                                    for i in range(e):
                                        arr[r + i][c] = egg
                            else:
                                for i in range(e):
                                    if arr[r - i][c] == 0:
                                        break
                                else:
                                    for i in range(e):
                                        arr[r - i][c] = egg
                            # print(arr)
                        # 왼위 대각선으로 탐색했을 때면
                        elif nr < r and nc < c:
                            for i in range(e):
                                if arr[r - i][c - i] == 0:
                                    break
                            else:
                                for i in range(e):
                                    arr[r - i][c - i] = egg
                        # 오른아래 대각선으로 탐색했을 때면
                        elif nr > r and nc > c:
                            for i in range(e):
                                if arr[r + i][c + i] == 0:
                                    break
                            else:
                                for i in range(e):
                                    arr[r + i][c + i] = egg
                        # 오른위 대각선으로 탐색했을 때면
                        elif nr < r and nc > c:
                            for i in range(e):
                                if arr[r - i][c + i] == 0:
                                    break
                            else:
                                for i in range(e):
                                    arr[r - i][c + i] = egg
                        # 왼아래 대각선으로 탐색했을 때면
                        elif nr > r and nc < c:
                            for i in range(e):
                                if arr[r + i][c - i] == 0:
                                    break
                            else:
                                for i in range(e):
                                    arr[r + i][c - i] = egg
                        # 중간에 한번 찾았으면 다음 e는 찾을 필요가 없으므로 탈출
                        break

    b_cnt = 0
    w_cnt = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if arr[r][c] == 1:
                b_cnt += 1
            elif arr[r][c] == 2:
                w_cnt += 1
    print(f'#{case} {b_cnt} {w_cnt}')