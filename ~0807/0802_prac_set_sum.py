T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input().split()))

    for i in range(1 << 10):  # 부분 집합의 개수
        sum = 0
        for j in range(10):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i 의 j번 비트가 1인 경우
                sum += arr[j]
        # 합이 0이 되는게 있으면 1 출력
        if sum == 0:
            print(f'#{case} {1}')
            break
        else:
            sum = 1

    # 합이 0이 되는게 없으면 0 출력
    if sum == 1:
        print(f'#{case} {0}')