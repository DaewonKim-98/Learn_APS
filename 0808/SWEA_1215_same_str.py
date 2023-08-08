for case in range(1, 11):
    N = int(input())

    arr = []
    for i in range(8):
        arr += [list(input())]

    result = 0
    # 행 우선 순회
    for r in range(8):
        for c in range(8 - N + 1):
            # 회문은 참이다
            same = True
            for j in range(N // 2):
                # 하나라도 양 옆이 같지 않으면 False
                if arr[r][c + j] != arr[r][c + N - 1 - j]:
                    same = False
            # 참이면 result += 1
            if same == True:
                result += 1

    # 열 우선 순회
    for c in range(8):
        for r in range(8 - N + 1):
            # 회문은 참이다
            same = True
            for j in range(N // 2):
                # 하나라도 양 옆이 같지 않으면 False
                if arr[r + j][c] != arr[r + N - 1 - j][c]:
                    same = False
            # 참이면 result += 1
            if same == True:
                result += 1

    print(f'#{case} {result}')