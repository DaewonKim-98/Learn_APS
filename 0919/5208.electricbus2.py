import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# dfs로 정류장까지 도착할 때까지 탐색
def dfs(i, cnt):
    global min_change
    # i에서 교환했을 때 정류장에 도착한다면
    if i + arr[i] >= N:
        if min_change > cnt:
            min_change = cnt
        return
    # i에서 교환했을 때 정류장에 도착하지 않는다면
    else:
        if min_change <= cnt:
            return
        # 다음 i가 갈 수 있는 경우는 i + 1부터 i + arr[i]까지
        for j in range(i + 1, i + arr[i] + 1):
            # print(i, j, cnt)
            dfs(j, cnt + 1)


T = int(input())
for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    arr.pop(0)
    arr = [0] + arr

    i = 1
    cnt = 0
    cnt_list = []
    # 최솟값 설정
    min_change = 100
    dfs(i, cnt)
    # print(cnt_list)
    # 가장 처음에 출발하는 것도 세줬으므로 1 빼주기
    print(f'#{case} {min_change}')
