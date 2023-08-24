T = int(input())

# 웜홀끼리 잇는 것을 표현하는 함수
def connect_hole(r, c, dr, dc, visited, q):
    global cnt
    nr, nc = r + dr, c + dc
    if (dr == 0) and (dc == -1):
        if (0 <= nr < N) and (0 <= nc < M):
            if (arr[nr][nc] == 1 or arr[nr][nc] == 3 or arr[nr][nc] == 4 or arr[nr][nc] == 5) and (visited[nr][nc] == 0):
                # 큐에 추가, 방문 표시, 카운트
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
    elif (dr == 0) and (dc == 1):
        if (0 <= nr < N) and (0 <= nc < M):
            if (arr[nr][nc] == 1 or arr[nr][nc] == 3 or arr[nr][nc] == 6 or arr[nr][nc] == 7) and (visited[nr][nc] == 0):
                # 큐에 추가, 방문 표시, 카운트
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
    elif (dr == -1) and (dc == 0):
        if (0 <= nr < N) and (0 <= nc < M):
            if (arr[nr][nc] == 1 or arr[nr][nc] == 2 or arr[nr][nc] == 5 or arr[nr][nc] == 6) and (visited[nr][nc] == 0):
                # 큐에 추가, 방문 표시, 카운트
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1
    elif (dr == 1) and (dc == 0):
        if (0 <= nr < N) and (0 <= nc < M):
            if (arr[nr][nc] == 1 or arr[nr][nc] == 2 or arr[nr][nc] == 4 or arr[nr][nc] == 7) and (visited[nr][nc] == 0):
                # 큐에 추가, 방문 표시, 카운트
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                cnt += 1


# 주어진 웜홀에 대한 너비우선탐색
def bfs(R, C, L):
    # 방문한 곳 표시
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    # 큐
    q = []
    q.append([R, C])
    # 소요되는 시간 동안 반복
    while len(q) > 0:
        if q:
            [r, c] = q.pop(0)
            # L 시간 이상 소요되었을 때 종료
            if visited[r][c] >= L:
                break
            # 터널 구조물의 모양에 따라서 가야하는 위치가 결정
            if arr[r][c] == 1:
                for dr, dc in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 2:
                for dr, dc in [(-1, 0), (1, 0)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 3:
                for dr, dc in [(0, -1), (0, 1)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 4:
                for dr, dc in [(-1, 0), (0, 1)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 5:
                for dr, dc in [(1, 0), (0, 1)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 6:
                for dr, dc in [(1, 0), (0, -1)]:
                    connect_hole(r, c, dr, dc, visited, q)
            elif arr[r][c] == 7:
                for dr, dc in [(-1, 0), (0, -1)]:
                    connect_hole(r, c, dr, dc, visited, q)


for case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    bfs(R, C, L)

    print(f'#{case} {cnt}')