T = int(input())

for case in range(1, T + 1):
    N = int(input())

    # 문자열로 만들어야 합치는게 편하다
    arr = [list(map(str, input().split())) for _ in range(N)]

    # 회전할 모양을 넣을 새로운 리스트
    lst = []

    # 90 도는 열 우선 탐색이면서 좌에서 우로, 하에서부터 상으로
    lst90 = []
    for c in range(N):
        rotate = ''
        for r in range(N - 1, -1, -1):
            rotate += arr[r][c]
        lst90.append(rotate)
    lst.append(lst90)

    # 180 도는 행 우선 탐색이면서 우에서 좌로, 하에서부터 상으로
    lst180 = []
    for r in range(N - 1, -1, -1):
        rotate = ''
        for c in range(N - 1, -1, -1):
            rotate += arr[r][c]
        lst180.append(rotate)
    lst.append(lst180)

    # 270 도는 열 우선 탐색이면서 우에서 좌로, 상에서부터 하으로
    lst270 = []
    for c in range(N-1, -1, -1):
        rotate = ''
        for r in range(N):
            rotate += arr[r][c]
        lst270.append(rotate)
    lst.append(lst270)

    # 지금 lst는 열로 되어 있으므로 이걸 회전시켜서 출력해주면 된다.
    print(f'#{case}')
    for c in range(N):
        for r in range(3):
            print(lst[r][c], end=' ')
        print()