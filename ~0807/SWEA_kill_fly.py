T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr += [list(map(int, input().split()))]

    # 어느 좌표에서 시작하는 파리채를 flapper 로 둔다.
    flappers = []
    # 파리채의 크기만큼 델타 탐색으로 파리채를 만들 것이므로 파리채를 M 크기로 만든다.
    for j in range(M):
        for k in range(M):
            # 아래에서 배열을 처음 선택한 값은 제외하므로 0, 0은 제외
            if (j != 0) or (k != 0):
                flappers += [(j, k)]
            else:
                pass
    # 죽인 파리의 최댓값
    fly_max = 0
    # 원배열에서 파리채를 뺀 크기만큼 배열을 만들면 파리채를 처음부터 끝까지 돌릴 수 있다.
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            # 죽인 파리의 수, 초기값은 처음 배열의 값
            fly = arr[r][c]
            # 파리채에 대한 델타 탐색을 하고 파리의 수를 더해준다.
            for j, k in flappers:
                nr, nc = r + j, c + k
                fly += arr[nr][nc]

            # 최댓값 갱신
            if fly_max < fly:
                fly_max = fly

    print(f'#{case} {fly_max}')