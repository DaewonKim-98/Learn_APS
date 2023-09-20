import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 두개씩 묶고 정렬하기
    arr2 = [[] for _ in range(M)]
    for i in range(M):
        arr2[i].append(arr[2 * i])
        arr2[i].append(arr[2 * i + 1])
        arr2[i] = sorted(arr2[i])

    # 정렬된 신청서에서 앞의 수를 인덱스로 하고 뒤의 수가 그 인덱스의 리스트에 들어가게 하면
    # 리스트들이 총 조의 수
    M_list = [set() for _ in range(N + 1)]
    for i in range(M):
        # 만약 뒤에 오는 인덱스에 값이 들어가는데 그 인덱스가 앞 리스트에 포함되어 있으면
        # 거기에 추가
        for j in range(i + 1):
            if arr2[i][0] in M_list[j]:
                M_list[j].add(arr2[i][1])
                break
        else:
            M_list[arr2[i][0]].add(arr2[i][1])

    # 여러 사람이 있는 조의 수는 M_list에서 값이 있는 리스트의 수
    groups = 0
    # 조를 만든 사람들을 모두 구하면
    people_group = 0
    for i in M_list:
        if len(i) > 0:
            groups += 1
            people_group += (len(i) + 1)

    # 단독인 조는 전체 사람에서 조를 만든 사람들을 뺀 것이므로 groups에 +
    groups = groups + (N - people_group)
    print(f'#{case} {groups}')


