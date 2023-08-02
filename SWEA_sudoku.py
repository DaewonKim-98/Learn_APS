T = int(input())

for case in range(1, T + 1):
    arr = []
    for i in range(9):
        arr += [list(map(int, input().split()))]

    # 답은 처음에 True 로 두고 겹치는 숫자가 있으면 False 로 바꿀것
    answer = 1
    # 행에서 같은 숫자가 있으면 answer 을 False 로 바꾼다. 같은 위치는 제외
    for r in range(9):
        for c in range(8):
            for nc in range(c + 1, 9):
                if arr[r][c] == arr[r][nc]:
                    answer = 0

    # 열에서 같은 숫자가 있으면 answer 을 False 로 바꾼다.
    for c in range(9):
        for r in range(8):
            for nr in range(r + 1, 9):
                if arr[r][c] == arr[nr][c]:
                    answer = 0

    # 델타 탐색으로 돌려 줄 3 X 3 의 정사각형을 만든다. 같은 위치는 제외
    square = []
    for j in range(3):
        for k in range(3):
            square += [(j, k)]

    # 격자를 돌린 것에서 같은 숫자가 있으면 answer 을 False 로 바꾼다.
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            for j, k in square:
                nr, nc = r + j, c + k
                for nj, nk in square:
                    nnr, nnc = r + nj, c + nk
                    # 같은 위치는 제외하기 위해
                    if (nr != nnr) or (nc != nnc):
                        if arr[nr][nc] == arr[nnr][nnc]:
                            answer = 0

    # 정답 출력
    print(f'#{case} {answer}')