T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        row = list(map(int, input().split()))
        arr += [row]

    # 델타 계산을 위해 리스트를 둔다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    # 절대값들의 합을 구하기 위해 total 을 둔다.
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # ni와 nj가 범위 밖으로 벗어나면 안되므로
                if (0 <= ni < N) & (0 <= nj < N):
                    # 인접한 것들의 차의 절댓값을 구하기 위해 if문 사용
                    if arr[i][j] >= arr[ni][nj]:
                        total += arr[i][j] - arr[ni][nj]
                    else:
                        total += arr[ni][nj] - arr[i][j]

    print(f'#{case} {total}')