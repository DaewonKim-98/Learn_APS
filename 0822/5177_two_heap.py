T = int(input())

def minheap(n):
    tree.append(n)
    # 노드에 따라 위치를 바꿔줘야 하므로
    node = len(tree) - 1
    # 노드는 1부터 이므로 node // 2 가 0 보다 클 때 즉 node가 1보다 클 때까지 반복
    while node > 1:
        if tree[node] < tree[node // 2]:
            tree[node], tree[node // 2] = tree[node // 2], tree[node]
        node = node // 2

for case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 처음 tree는 0을 넣고 시작
    tree = [0]
    for num in nums:
        minheap(num)
    # 마지막 노드의 조상 노드에 저장된 정수의 합
    sum_node = 0
    while N > 0:
        N = N // 2
        sum_node += tree[N]
    print(f'#{case} {sum_node}')
