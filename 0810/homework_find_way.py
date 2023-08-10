T = 10

# dfs에 대한 함수, S: 시작 노드 / G: 도착 노드 / V: 노드 개수 / arr_v: 노드가 표시된 배열
def dfs(S, G, V, arr_v):
    connect_list = [] # 연결된 경로들의 리스트
    stack = [] # 스택 생성
    visited = [0] * (V + 1) # 방문한 곳을 알 수 있는 visited 생성
    visited[S] = 1 # 시작점을 표시
    while True:
        # 오름차순으로 연결된 노드를 찾는다.
        for w in range(1, V + 1):
            # 현재 노드 S에 연결되어 있고 미방문한 w를 찾으면
            if arr_v[S][w] == 1 and visited[w] == 0:
                stack.append(S) # 스택에 S을 쌓는다.
                S = w # S은 다시 연결된 w로 갱신해준다.
                visited[S] = 1 # 연결된 지점에 방문 했다는 것을 표시
                break
        # for 문이 끊기지 않고 모두 돌아간다면 - 맞는 w가 없다면(for else 문)
        else:
            # 스택에 이미 지나온 노드가 있으면, 남아 있으면
            if stack:
                # 더 연결된 노드가 없으면 경로는 바뀌기 때문에 지금까지의 경로를 만들어 connect_list에 추가
                # stack은 마지막 값을 추가하기 전이므로 S를 최종적으로 추가하여 추가
                connect = stack[:]
                connect.append(S)
                connect_list.append(connect)
                # 다시 스택을 제거해주면서 위로 올라가 다른 미방문한 w를 찾는다.
                S = stack.pop()
            # 스택에 아무것도 없으면 0으로 모두 돌았다는 것이므로 종료
            else:
                break

    # 커넥트들에서 도착 노드가 있으면 1을 출력하고 없으면 0을 출력
    for c in connect_list:
        if G in c:
            result = 1
            break
        else:
            result = 0

    # 도착 경로에 대한 값을 출력
    return result


for case in range(1, T + 1):
    N, E = map(int, input().split()) # V 개의 노드. E 개의 간선
    way_list = list(map(int, input().split()))
    S, G = 0, 99 # 출발, 도착 노드
    V = 100

    arr_v = [] # V개의 점들이 간선으로 이어져 있는지 없는지를 표시할 arr
    for i in range(V + 1):
        arr_v.append([0] * (V + 1))

    # E개의 간선에서 way_list 로 알 수 있는 연결되어 있는 노드들을 arr_v에 1로 표시해준다.
    for e in range(E):
        v1, v2 = way_list[e * 2], way_list[e * 2 + 1]
        arr_v[v1][v2] = 1
        # arr_v[v2][v1] = 1

    print(f'#{case} {dfs(S, G, V, arr_v)}')

