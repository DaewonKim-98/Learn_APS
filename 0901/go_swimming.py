T = int(input())

# 갈 수 있는 방향은 상하좌우
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# 물로 가는 경로 찾기
def bfs(water_cor):
    move_sum = 0
    # 방문한 곳을 셀 cnt
    cnt = len(water_cor)
    q = [0] * (N * M * 2)
    for w in range(len(water_cor)):
        r, c = water_cor[w][0], water_cor[w][1]
        q[2 * w] = r
        q[2 * w + 1] = c
    i = len(water_cor)
    j = 0
    while cnt < N * M:
        r, c = q[j * 2], q[j * 2 + 1]
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            # 땅이면 간다
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == -1:
                q[i * 2], q[i * 2 + 1] = nr, nc
                # 방문한 땅은 거리로 바꿔주기
                arr[nr][nc] = arr[r][c] + 1
                move_sum += arr[nr][nc]
                # 방문 횟수 추가
                cnt += 1
                i += 1
        j += 1

    # 모두를 다 방문했으면
    return move_sum


for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    # 물의 좌표
    water_cor = []
    for i in range(N):
        a = list(input())
        for j in range(M):
            # 물의 좌표 찾기
            if a[j] == 'W':
                a[j] = 0
                water_cor.append([i, j])
            else:
                a[j] = -1
        arr.append(a)

    # 물의 좌표 모두에서 bfs로 거리 찾기

    print(f'#{case} {bfs(water_cor)}')