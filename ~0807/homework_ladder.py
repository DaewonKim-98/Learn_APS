for case in range(1, 11):
    N = int(input())

    arr = []
    for i in range(100):
        arr += [list(map(int, input().split()))]

    # X의 위치를 찾는다.
    c = 0
    for x in range(100):
        if arr[99][x] == 2:
            c = x

    # 행의 위치가 0이 되면 종료
    r = 99
    while r > 0:
        # r을 0까지 낮춘다.
        r -= 1
        if r == 0:
            break

        # c가 0이나 99에 위치하면
        if c == 99:
            # 현재 위치에서 왼쪽에 1이 있을 때 r을 낮추는거 종료하고 c를 낮춘다.
            if arr[r][c - 1] == 1:
                while True:
                    c -= 1
                    # 더 이상 1이 없을 때, 벽에 다다랐을 때 break 으로 탈출
                    if c == 0:
                        break
                    elif arr[r][c - 1] != 1:
                        break
                pass
            else:
                pass

        # c가 0이나 99에 위치하면
        elif c == 0:
            # 현재 위치에서 왼쪽에 1이 있을 때 r을 낮추는거 종료하고 c를 낮춘다.
            if arr[r][c + 1] == 1:
                while True:
                    c += 1
                    # 더 이상 1이 없을 때, 벽에 다다랐을 때 break 으로 탈출
                    if c == 0:
                        break
                    elif arr[r][c + 1] != 1:
                        break
                pass
            else:
                pass

        # 현재 위치에서 왼쪽에 1이 있을 때 r을 낮추는거 종료하고 c를 낮춘다.
        elif arr[r][c - 1] == 1:
            while True:
                c -= 1
                # 더 이상 1이 없을 때, 벽에 다다랐을 때 break 으로 탈출
                if c == 0:
                    break
                elif arr[r][c - 1] != 1:
                    break
            pass

        # 현재 위치에서 오른쪽에 1이 있을 때 r을 낮추는거 종료하고 c를 낮춘다.
        elif arr[r][c + 1] == 1:
            while True:
                c += 1
                # 더 이상 1이 없을 때, 벽에 다다랐을 때 break 으로 탈출
                if c == 99:
                    break
                elif arr[r][c + 1] != 1:
                    break
            pass

        # 아니면 pass
        else:
            pass

    print(f'#{case} {c}')
