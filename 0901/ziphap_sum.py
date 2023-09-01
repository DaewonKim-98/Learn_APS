T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 합이 K가 되는 경우의 수
    cnt = 0
    # 부분집합을 표시하는 i
    for i in range(1 << N):
        # 부분집합의 합
        s = 0
        # j번 비트
        for j in range(N):
            # i의 j번 비트 검사
            if i & (1 << j):
                # 0이 아니면 j번 원소가 부분집합에 포함됨
                s += arr[j]
        if s == K:
            cnt += 1
    print(f'#{case} {cnt}')