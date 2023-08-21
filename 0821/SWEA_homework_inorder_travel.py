T = 10

# 중위순회를 하면서 문자 출력
def inorder_travel(n):
    if n:
        inorder_travel(ch1[n])
        print(n_dic[n], end='')
        inorder_travel(ch2[n])

for case in range(1, T + 1):
    N = int(input())
    E = N - 1
    e_list = []
    # 정점과 정점에 해당하는 문자 딕셔너리
    n_dic = {}
    for i in range(N):
        lst = list(map(str, input().split()))
        # 정점과 해당하는 문자를 딕셔너리에 포함
        n_dic[int(lst[0])] = lst[1]
        # lst의 길이가 2가 넘으면 간선이 생긴다는 말이므로
        if len(lst) > 2:
            # 간선 리스트에 추가
            e_list.append([int(lst[0]), int(lst[2])])
            if len(lst) > 3:
                e_list.append([int(lst[0]), int(lst[3])])

    # 부모 인덱스에 대한 자식 노드
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for [p, c] in e_list:
        # 자식 노드에 부모 노드인덱스의 값이 하나도 안들어 있으면
        if ch1[p] == 0:
            ch1[p] = c
        # 자식 노드에 부모 노드 인덱스의 값이 하나 들어있으면 두번째 리스트에 추가
        else:
            ch2[p] = c
    # 루트는 항상 1
    n = 1
    print(f'#{case}', end=' ')
    inorder_travel(n)
    print()