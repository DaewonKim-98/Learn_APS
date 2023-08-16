def search(col, cnt):
    global result

    if cnt > result: # 현재 입시값이 최댓값보다 크다면 유망X
        return
    if col == N:
        if cnt < result:
            result = cnt
    else:
        for row in range(N):
            if not visited[row]: # 방문 하지 않은 열이라면,
                visited[row] = 1 # 방문 표시
                search(col + 1, cnt + arr[col][row])
                visited[row] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 열에 대한 방문 확인
    result = 10 * N # 최솟값
    cnt = 0
    col = 0

    search(cot, cnt)