T = int(input())

for case in range(1, T + 1):
    N = int(input())

    # 빈 arr 을 만든다.
    arr = []
    for i in range(N):
        arr += [[0] * N]

    # 새로운 배열의 순서를 만들기 위해 리스트와 좌표를 둔다.
    nlist = []
    # 새로운 배열에서 벽에 부딪힐 때까지의 거리를 nmax와 nmin으로 둔다.
    nmax = N
    nmin = 0
    nx, ny = 0, 0
    # 새 배열에 일단 0,0을 추가하고 count를 센다.
    nlist += [(nx, ny)]
    ncount = 1
    # count가 배열의 크기가 되기 전까지 반복을 돌린다.
    while ncount < N ** 2:
        # 처음에는 x만 증가하면 되므로 nmax에 도달할 때까지 증가
        while nx < nmax - 1:
            nx += 1
            nlist += [(nx, ny)]
            ncount += 1
            # 만약 ncount가 N 의 제곱, 배열의 수와 같아지면 탈출
            if ncount == N ** 2:
                break
        # 만약 ncount가 N 의 제곱, 배열의 수와 같아지면 탈출
        if ncount == N ** 2:
            break

        # 다음에는 y만 증가하므로 nmax 에 도달할 때까지 증가
        while ny < nmax - 1:
            ny += 1
            nlist += [(nx, ny)]
            ncount += 1
            # 만약 ncount 가 N 의 제곱, 배열의 수와 같아지면 탈출
            if ncount == N ** 2:
                break

        # 만약 ncount 가 N 의 제곱, 배열의 수와 같아지면 탈출
        if ncount == N ** 2:
            break
        # 다음 돌 때 nmax 는 1 감소해야
        nmax -= 1

        # 이제는 x만 작아져야 하므로 nmin 에 도달할 때까지 감소
        while nx > nmin:
            nx -= 1
            nlist += [(nx, ny)]
            ncount += 1
            # 만약 ncount 가 N 의 제곱, 배열의 수와 같아지면 탈출
            if ncount == N ** 2:
                break
        # 만약 ncount 가 N 의 제곱, 배열의 수와 같아지면 탈출
        if ncount == N ** 2:
            break

        # 다음 돌 때 최솟값이 증가해야하므로 nmin이 1 증가
        nmin += 1
        # 이제는 y만 작아져야 하므로 nmin 에 도달할 때까지 감소
        while ny > nmin:
            ny -= 1
            nlist += [(nx, ny)]
            ncount += 1
            # 만약 ncount 가 N 의 제곱, 배열의 수와 같아지면 탈출
            if ncount == N ** 2:
                break

    # 새로운 리스트들에 있는 순서대로 배열이 만들어져야 하므로 그 값들에 맞게 배열 만들기
    for i in range(N ** 2):
        arr[nlist[i][0]][nlist[i][1]] = i + 1

    # 새로운 배열은 행 열이 반대로 만들어졋으므로 거꾸로 해서 출력
    print(f'#{case}')
    for c in range(N):
        for r in range(N):
            print(arr[r][c], end=' ')
        print()


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    count = 1 # 달팽이가 이동하면서 값을 증가시키고 기록할 변수
    x, y = 0, 0 # 시작 좌표 설정 x: 0, y: 0
    dir = 0 # 이동할 방향
    arr[x][y] = count # 시작 위치에 1을 기록

    while count < N ** 2: # N*N 만큼 판이 만들어지니까
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 다음 조사 위치가 0보다 크거나 같고, N 보다 작다면 / 그리고 다음 위치가 0이면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            count += 1
            arr[nx][ny] = count # 현재 조사하는 곳에 count 할당
            x, y = nx, ny # 내 위치 갱신
        else: # 더 이상 해당 방향으로 이동해 기록할 수 없을 때:
            dir += 1
            # 방향은 4종류 뿐이다.
            if dir >= 4:
                dir = 0 # 다시 우측으로 이동하도록 초기화

    print(f'# {tc}')
    for r in arr:
        for c in arr:
            print(arr[r][c], end=' ')
        print()
