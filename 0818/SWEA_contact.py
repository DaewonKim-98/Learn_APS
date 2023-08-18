T = 10

def bfs(S):
    visited = [0] * 101
    q = []
    q.append(S)
    visited[S] = 1

    # q가 있을 때까지 반복
    while q:
        t = q.pop(0)
        for w in range(1, 101):
            if arr[t][w] == 1 and visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

    # visited에서 가장 최댓값의 마지막 인덱스를 구한다.
    max_idx = 0
    for i in range(101):
        if visited[max_idx] <= visited[i]:
            max_idx = i

    return max_idx

for case in range(1, T + 1):
    E, S = map(int, input().split())
    e_list = list(map(int, input().split()))

    # 연결된 간선을 표현할 배열
    arr = [[0] * 101 for _ in range(101)]
    # 방향이 정해져 있으므로
    for i in range(E // 2):
        arr[e_list[i * 2]][e_list[i * 2 + 1]] = 1

    print(f'#{case} {bfs(S)}')
