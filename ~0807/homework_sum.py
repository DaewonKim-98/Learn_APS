for case in range(1, 11):
    N = int(input())
    arr = []
    for i in range(100):
        row = list(map(int, input().split()))
        arr += [row]

    # 합들의 최댓값을 max_sum 으로 둔다.
    max_sum = 0
    # 각 행의 합
    for r in range(100):
        row_sum = 0
        for c in range(100):
            row_sum += arr[r][c]
        #갱신
        if max_sum < row_sum:
            max_sum = row_sum

    # 각 열의 합
    for c in range(100):
        col_sum = 0
        for r in range(100):
            col_sum += arr[r][c]
        # 갱신
        if max_sum < col_sum:
            max_sum = col_sum

    # 정대각선의 합
    dia1_sum = 0
    for r in range(100):
        for c in range(100):
            if r == c:
                dia1_sum += arr[r][c]
        #갱신
        if max_sum < dia1_sum:
            max_sum = dia1_sum

    # 역대각선의 합
    dia2_sum = 0
    for r in range(100):
        for c in range(100):
            if r == c:
                dia2_sum += arr[r][99 - r]
        #갱신
        if max_sum < dia2_sum:
            max_sum = dia2_sum

    print(f'#{case} {max_sum}')