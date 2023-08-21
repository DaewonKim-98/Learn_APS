T = int(input())

def inorder_travels(n):
    global i
    # n 이 트리의 노드인 N 보다 크면 안되므로
    if n > N:
        return
    # 재귀로 돌아다니면서 노드 번호에 맞게 자연수를 이진 트리에 저장한다.
    inorder_travels(2 * n)
    # 가장 왼쪽은 2의 제곱수인데 그것은 1이므로 1부터 넣으면서 시작
    lst[n] = i
    # 넣었으면 다음 자연수로 더하기
    i += 1
    # 오른쪽 아래는 부모 노드에서 2 곱한 값을 +1 한 것
    inorder_travels(2 * n + 1)

for case in range(1, T + 1):
    N = int(input())
    lst = [0] * (N + 1)
    # lst의 노드 번호 인덱스에 넣을 자연수
    i = 1
    # 처음 노드 번호는 1
    n = 1
    inorder_travels(n)
    print(f'#{case} {lst[1]} {lst[N // 2]}')