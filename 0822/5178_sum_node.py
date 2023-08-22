T = int(input())

# 후위 순회로 도는 것이므로
def postorder_travel(n):
    # n은 노드의 개수인 N을 넘어갈 수 없다.
    if n > N:
        return
    # 아직 노드에 저장이 되지 않았으면
    if tree[n] == 0:
        postorder_travel(2 * n)
        postorder_travel(2 * n + 1)
        # 두 자식들의 합: 마지막 2 * n + 1은 N을 넘어갈 수도 있으므로 두 경우로 나눔
        if 2 * n + 1 <= N:
            tree[n] = tree[2 * n] + tree[2 * n + 1]
        else:
            tree[n] = tree[2 * n]

for case in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    # tree에 리프 노드 저장
    for _ in range(M):
        leaf_node, leaf_value = map(int, input().split())
        tree[leaf_node] = leaf_value
    # 루트는 1번
    n = 1
    postorder_travel(n)
    # 지정한 노드 번호의 값 출력
    print(f'#{case} {tree[L]}')