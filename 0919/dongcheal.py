import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(cnt, posibility):
    global max_success
    if cnt == N:
        if max_success < posibility:
            max_success = posibility

    else:
        if max_success > posibility:
            return
        for num in range(N):
            if arr[cnt][num] == 0:
                continue
            if visited[num] == 0:
                visited[num] = 1
                dfs(cnt + 1, posibility * (arr[cnt][num] / 100))
                visited[num] = 0


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_success = 0
    # 일을 했다면 나타낼
    visited = [0] * N
    # 일을 선택한 횟수와 확률
    cnt = 0
    posibility = 1
    dfs(cnt, posibility)
    print(f'#{case} {max_success * 100:.6f}')