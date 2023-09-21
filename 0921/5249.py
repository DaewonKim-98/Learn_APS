import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq

def prim(v):
    global min_v
    heap = []

    heapq.heappush(heap, (0, v))
    # 합 가중치
    sum_w = 0

    while heap:
        w, v = heapq.heappop(heap)
        if visited[v] == 0:
            sum_w += w
            if sum_w >= min_v:
                return
            visited[v] = 1
            for v2, w2 in e_list[v]:
                if visited[v2] == 0:
                    heapq.heappush(heap, (w2, v2))
        print(heap)
    if min_v > sum_w:
        min_v = sum_w

T = int(input())
for case in range(1, T + 1):
    V, E = map(int, input().split())
    e_list = [[] for _ in range(E)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        e_list[n1].append((n2, w))
        e_list[n2].append((n1, w))

    # 가중치의 합 최소로 갱신
    min_v = 10000
    # for v in range(V + 1):
    visited = [0] * (V + 1)
    prim(0)

    print(f'#{case} {min_v}')