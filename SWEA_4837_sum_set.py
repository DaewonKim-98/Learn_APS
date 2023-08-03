T = int(input())
A = list(range(1, 13))

for case in range(1, T + 1):
    N, K = map(int, input().split())

    # 결과를 result로 두고 부분 집합의 개수를 set_cnt로 둔다.
    result = False
    set_cnt = 0
    for i in range(1 << 12):  # 부분 집합의 개수
        # 합과 원소의 수를 sum과 cnt로 둔다.
        sum = 0
        cnt = 0
        for j in range(12):  # 원소의 수만큼 비트를 비교
            if i & (1 << j):  # i 의 j번 비트가 1인 경우
                # 부분 집합의 원소의 합과 원소의 개수를 더해준다.
                sum += A[j]
                cnt += 1
        # 합이 K가 되고 원소의 개수가 N개가 되면 결과를 True 로 바꾸고 부분집합의 개수를 추가한다.
        if sum == K and cnt == N:
            result = True
            set_cnt += 1

    # 결과가 True면 부분집합의 개수 출력
    if result == True:
        print(f'#{case} {set_cnt}')
    else:
        print(f'#{case} {0}')