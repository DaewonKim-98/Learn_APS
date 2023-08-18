T = int(input())

# dir
dir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

# 시작점 찾는 함수
def start(N):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                return r, c

# bfs
def bfs(sr, sc):
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    q = []
    q.append([sr, sc])
    visited[sr][sc] = 1
    while q:
        [r, c] = q.pop(0)
        # 3에 도착하면 출력
        if arr[r][c] == 3:
            return visited[r][c] - 2
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if (0 <= nr < N) and (0 <= nc < N) and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
    # while 문이 다 돌 때까지 도착 안하면 미로가 되지 않는다는 것
    return 0

for case in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 시작점
    sr, sc = start(N)

    print(f'#{case} {bfs(sr, sc)}')

