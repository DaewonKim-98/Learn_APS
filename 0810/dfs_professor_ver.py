'''
7 8 V E

'''

# 인접 행렬 생성
V, E = map(int, input().split()) # 노드, 간선

data = list(map(int, input().split())) # 간선 정보

arr = [[0] * (V + 1) for _ in range(V + 1)]

visited = [0] * (V + 1) # 노드의 방문 여부 체크 리스트

for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    arr[n1][n2] = 1
    arr[n2][n1] = 1

# 재귀
def dfs(v):
    visited[v] = 1
    print(v)
    for w in range(1, V + 1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 반복문
def dfs(v):
    stack = [v]
    # 스택이 빌 때까지 반복
    while len(stack):
        v = stack.pop()
        visited[v] = 1
        for w in range(1, V + 1):
            if arr[v][w] == 1 and visited[w] == 0:
                stack.append(w)