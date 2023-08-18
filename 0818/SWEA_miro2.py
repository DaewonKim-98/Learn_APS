T = 10

# 방향
dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]

# 시작점 함수
def start(N):
    for r in range(N):
        for c in range(N):
            if miro[r][c] == 2:
                return r, c

# bfs
def bfs(sr, sc):
    visited = [[0] * 101 for _ in range(101)]
    q = []
    q.append([sr, sc])
    visited[sr][sc] = 1

    while q:
        [r, c] = q.pop(0)
        # 도착했으면
        if miro[r][c] == 3:
            return 1
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            # 새 좌표가 미로 안에 있고 벽이 아니고 방문하지 않았으면
            if (0 <= nr < 100) and (0 <= nc < 100) and (miro[nr][nc] != 1) and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
    return 0

for case in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(100)]

    # 시작점
    sr, sc = start(100)

    print(f'#{case} {bfs(sr, sc)}')