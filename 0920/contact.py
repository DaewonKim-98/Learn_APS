import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(S):
    visited = [0] * 101
    q = []
    visited[S] = 1
    q.append(S)
    last_call = 0
    while len(q) > 0:
        p = q.pop(0)
        for i in N_list[p]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[p] + 1
        last_call = p

    max_i = 0
    for i in range(101):
        if visited[i] == visited[last_call]:
            max_i = i

    return max_i

T = 10
for case in range(1, T + 1):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    # 연결된 간선 리스트
    N_list = [[] for _ in range(101)]
    for i in range(N // 2):
        if arr[i * 2 + 1] not in N_list[arr[i * 2]]:
            N_list[arr[i * 2]].append(arr[i * 2 + 1])
            N_list[arr[i * 2]] = sorted(N_list[arr[i * 2]])

    print(f'#{case} {bfs(S)}')
