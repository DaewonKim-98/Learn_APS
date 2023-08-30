T = int(input())

# 방향은 오른쪽과 아래밖에 가지 못한다.
dir = [[0, 1], [1, 0]]

def dfs(r, c, s):
    s += arr[r][c]
    if r == N - 1 and c == N - 1:
        s_list.append(s)
        return
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, s)

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 왼쪽 위부터 시작해서 오른쪽과 아래 방향으로 밖에 움직이면 안되므로
    # 두 경우 중 작은 쪽으로 해서 탐색
    r = 0
    c = 0
    s = 0
    # 처음부터 끝까지의 합 리스트
    s_list = []
    dfs(r, c, s)

    # 정답은 합 리스트에서 최솟값
    print(f'#{case} {min(s_list)}')