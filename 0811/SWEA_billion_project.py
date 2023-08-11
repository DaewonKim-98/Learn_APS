T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 볼 수 있는 이익을
    profit = 0
    # 뒤에서부터 시작해서 자신보다 큰 것이 나오기 전에는 이득을 볼 수 있으므로
    j = N - 1
    for i in range(N-1, 0, -1):
        # 앞에 나오는 수가 가장 뒤에 수보다 크거나 같을 때 이후부터 가장 뒤에까지 최대 이익
        if arr[i - 1] >= arr[j]:
            # 가장 뒤에 수, 즉 가장 큰 수 * 길이 에서 i부터 j까지의 합을 뺀 것과 같다
            max_value = arr[j] * (j - i)
            for k in range(i, j):
                max_value -= arr[k]
            # 최댓값이 앞으로 땡겨왔으므로 j 갱신
            j = i - 1
            # 만약 계산한 max_value가 0보다 클 때 profit에 추가
            if max_value > 0:
                profit += max_value
        # 처음까지 왔을 때는 계산이 안되므로 추가 계산
        elif i == 1:
            # 가장 뒤에 수, 즉 가장 큰 수 * 길이 에서 i부터 j까지의 합을 뺀 것과 같다
            max_value = arr[j] * (j - i + 1)
            for k in range(0, j):
                max_value -= arr[k]
            # 만약 계산한 max_value가 0보다 클 때 profit에 추가
            if max_value > 0:
                profit += max_value

    print(f'#{case} {profit}')