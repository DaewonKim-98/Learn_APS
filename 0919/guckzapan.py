import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 이동하는 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# dfs로 탐색
def dfs(r, c, cnt, num):
    if cnt == 6:
        if num not in num_set:
            num_set.add(num)
    else:
        for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < 4 and 0 <= nc < 4:
                dfs(nr, nc, cnt + 1, num + arr[nr][nc])



T = int(input())
for case in range(1, T + 1):
    arr = [list(map(str, input().split())) for _ in range(4)]

    num_set = set()
    # 델타 탐색
    for r in range(4):
        for c in range(4):
            num = ''
            num += arr[r][c]
            dfs(r, c, 0, num)

    print(f'#{case} {len(num_set)}')
