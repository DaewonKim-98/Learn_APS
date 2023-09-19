import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(cnt, price):
    global min_price
    if cnt == N:
        if min_price > price:
            min_price = price
            return
    else:
        if price > min_price:
            return
        for num in range(N):
            if visited[num] == 0:
                visited[num] = 1
                dfs(cnt + 1, price + arr[cnt][num])
                visited[num] = 0


T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 순열을 구해서 합들을 구해보면 되므로

    # 앞의 공장이 제품을 등록했는지 확인할 visited
    visited = [0] * N
    # 시작점 돌면서 생산 비용 구하기
    prices = []
    cnt = 0
    price = 0
    min_price = 100 * 15
    dfs(cnt, price)
    print(f'#{case} {min_price}')