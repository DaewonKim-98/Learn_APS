T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # E: 간선의 개수, N: roots
    N2 = N  # c2 탐색 위해 설정. 이 방법이 맞나?
    arr = list(map(int, input().split()))

    # 1. 자식노드 기입을 위한 빈 리스트 생성
    # c1, c2의 인덱스가 부모 노드 (1~6)
    c1 = [0] * (E+2)
    c2 = [0] * (E+2)

    # 2. 간선정보를 하나씩 읽어 c1과 c2에 기입
    for i in range(E):  # 전체 간선의 개수만큼 순회 ∵ 간선 정보를 읽는 것이니까
        p, c = arr[2*i], arr[2*i+1]
        if c1[p] == 0:  # c1의 p번째가 비어있으면
            c1[p] = c   # p부모의 첫 번째 자식으로 c를 기입
        else:           # c1의 p번째가 비어있지 않으면(첫번째 자식이 있으면)
            c2[p] = c   # p부모의 두 번째 자식으로 c를 기입

    # 3. 루트가 N인 서브트리의 노드의 개수
    subnode = 1  # 서브트리의 노드의 개수(root도 포함해야 하므로 1부터 시작)

    while c1[N] != 0:  # c1을 탐색 리프노드가 아니면
        N = c1[N]
        subnode += 1

    while c2[N2] != 0:  # c2를 탐색 리프노드가 아니면
        N2 = c2[N2]
        subnode += 1

    print(f'#{tc} {subnode}')