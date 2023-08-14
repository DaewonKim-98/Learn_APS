T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    check_arr = [[0] * N for _ in range(N)]
    result = 0

    # 미로의 방향은 상하좌우
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # 3에서 출발해서 2로 가는 것도 미로를 통과하는 것과 똑같으므로 값이 3인 위치를 찾는다.
    r, c = 0, 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 3:
                r = y
                c = x

    stack = []
    check_arr[r][c] = 1
    # 더 이상 움직일 수 없을 때까지 미로를 돌린다.
    while True:
        if result == 1:
            break
        # 상하좌우 방향으로 새롭게 r, c를 만든다.
        for d in dir:
            # 새롭게 만든 방향으로 갔을 때 길이 있으면 반복
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                # 2가 나오면 도착하는 경로가 존재한다는 것이므로 종료
                if arr[nr][nc] == 2:
                    result = 1
                # 길이 있고 한 번도 간 적이 없는 경로라면 움직이며 r, c 갱신
                if arr[nr][nc] == 0 and check_arr[nr][nc] == 0:
                    stack.append([r, c])
                    r, c = nr, nc
                    check_arr[r][c] = 1
                    break

        # 더 이상 for문에서 break이 일어나지 않으면 더 이상 갈 수 있는 경로가 없다는 뜻이므로
        else:
            if stack:
                rc = stack.pop()
                r = rc[0]
                c = rc[1]
            else:
                break

    print(f'#{case} {result}')



