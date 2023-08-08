T = int(input())

for case in range(1, T + 1):
    N = int(input())
    # 보라색을 0으로 둔다.
    purple = 0
    # 10 * 10의 배열을 만든다.
    arr = []
    for j in range(10):
        arr += [[0] * 10]
    for i in range(N):
        # 받아오는 좌표와 색상 정보를 coord 로 둔다.
        coord = list(map(int, input().split()))
        # 빨간색 부분은 1, 색이 다른 부분이면 보라색인 3으로 덮는다.
        if coord[4] == 1:
            for r in range(coord[0], coord[2] + 1):
                for c in range(coord[1], coord[3] + 1):
                    if arr[r][c] == 2:
                        arr[r][c] = 3
                    else:
                        arr[r][c] = 1
        # 파란색 부분을 2, 색이 다른 부분이면 보라색인 3으로 덮는다.
        else:
            for r in range(coord[0], coord[2] + 1):
                for c in range(coord[1], coord[3] + 1):
                    if arr[r][c] == 1:
                        arr[r][c] = 3
                    else:
                        arr[r][c] = 2

    # 다 끝나고 나서 다시 돌려서 3인 부분이 있으면 purple 에 1을 추가한다.
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                purple += 1

    print(f'#{case} {purple}')