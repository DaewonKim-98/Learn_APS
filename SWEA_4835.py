T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # M개의 합의 최솟값을 찾기 위해 먼저 처음 M개의 합을 구한다.
    min_M = 0
    for num in range(M):
        min_M += arr[num]

    # i 부터 시작해 N-M+1 번 도는데 i 번째부터 i+M 번째의 합이 min_M보다 작으면 대체
    for i in range(N - M + 1):
        min_sum = 0
        for j in range(i, i + M):
            min_sum += arr[j]
        if min_M > min_sum:
            min_M = min_sum

    # M개의 합의 최댓값을 찾기 위해 먼저 처음 M개의 합을 구한다.
    max_M = 0
    for num in range(M):
        max_M += arr[num]

    # i 부터 시작해 N-M+1 번 도는데 i 번째부터 i+M 번째의 합이 max_M보다 크면 대체
    for i in range(N - M + 1):
        max_sum = 0
        for j in range(i, i + M):
            max_sum += arr[j]
        if max_M < max_sum:
            max_M = max_sum

    print(f'#{t} {max_M - min_M}')

















# while True:
#     sentence = str(input())
#     if sentence == '.':
#         break
#
#     balance = True
#     for i in range(len(sentence)):
#         for j in range(i, len(sentence)):
#