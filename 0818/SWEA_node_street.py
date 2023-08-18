T = int(input())

def dfs(S, G, V):
    visited = [0] * (V + 1)
    q = []
    q.append(S)
    visited[S] = 1

    # 큐가 존재하면
    while q:
        t = q.pop(0)
        # t가 G면 G까지 연결되었다는 뜻이므로
        if t == G:
            return visited[G] - 1
        for w in range(1, V + 1):
            # 간선으로 연결되어 있고 방문하지 않았으면
            if arr[t][w] == 1 and visited[w] == 0:
                q.append(w)
                # 간선을 지난 횟수
                visited[w] = visited[t] + 1
    # 다 돌아도 출력이 안되었으면 없는 것이므로
    return 0



for case in range(1, T + 1):
    V, E = map(int, input().split())
    e_list = []
    for i in range(E):
        e_list.append(list(map(int, input().split())))
    S, G = map(int, input().split())

    # 간선을 표시할 배열
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for e in e_list:
        # 방향성이 없으므로
        arr[e[0]][e[1]] = 1
        arr[e[1]][e[0]] = 1

    print(f'#{case} {dfs(S, G, V)}')

