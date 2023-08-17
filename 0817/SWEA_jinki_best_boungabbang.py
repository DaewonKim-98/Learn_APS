T = int(input())

for case in range(1, T + 1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    result = 'Possible'

    # 들어오는 사람들을 오름차순으로 정렬
    for i in range(N, 1, -1):
        for j in range(1, i):
            if people[j - 1] > people[j]:
                people[j - 1], people[j] = people[j], people[j - 1]

    # 빵 리스트에서 시간 순으로 빵을 얼마나 만들 수 있는지 리스트로 본다.
    bbang_list = []
    for k in range(1, N + 1):
        bbang_list += [M * k] * K
    # 만약 시간 순으로 했을 때 빵 만드는 시간이 하나라도 더 길다면 impossible 하고 종료
    for l in range(N):
        if bbang_list[l] > people[l]:
            result = 'Impossible'
            break

    print(f'#{case} {result}')
