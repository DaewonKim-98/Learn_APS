def bfs(arr, start):
    visited = set() # 방문 여부
    queue = [start] # 시작 노드를 큐에 삽입

    while queue: # 큐가 빌때까지 반복
        node = queue.pop(0) # 큐에서 노드를 하나씩 꺼낸다
        # 방문 여부 확인
        if node not in visited: # 방문 리스트에 노드가 존재하지 않는다면
            visited.add(node) # 방문처리
            print(node, end=' ')
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

V, E = map(int, input().split())
N = int(input())
temp = [list(map(int, input().split())) for _ in range(N)]
graph = {}

# 간선 정보 기록
