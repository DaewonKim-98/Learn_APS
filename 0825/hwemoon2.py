T = 10

for case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(100)]

    # 최대길이
    max_length = 1
    # 행 우선 탐색으로 회문 찾기
    for r in range(100):
        for c in range(100):
            # 회문의 최대 길이: 100
                length = 0
                # 짝수인 회문
                for i in range(1, 51):
                    nc1, nc2 = c - i, c + i - 1
                    if 0 <= nc1 < 100 and 0 <= nc2 < 100:
                        if arr[r][nc1] == arr[r][nc2]:
                            length += 2
                        else:
                            break
                if max_length < length:
                    max_length = length

                length = 1
                # 홀수인 회문
                for i in range(1, 51):
                    nc1, nc2 = c - i, c + i
                    if 0 <= nc1 < 100 and 0 <= nc2 < 100:
                        if arr[r][nc1] == arr[r][nc2]:
                            length += 2
                        else:
                            break
                if max_length < length:
                    max_length = length

    # 열 우선 탐색으로 회문 찾기
    for c in range(100):
        for r in range(100):
            # 회문의 최대 길이: 100
            length = 0
            # 짝수인 회문
            for i in range(1, 51):
                nr1, nr2 = r - i, r + i - 1
                if 0 <= nr1 < 100 and 0 <= nr2 < 100:
                    if arr[nr1][c] == arr[nr2][c]:
                        length += 2
                    else:
                        break
            if max_length < length:
                max_length = length

            length = 1
            # 홀수인 회문
            for i in range(1, 51):
                nr1, nr2 = r - i, r + i
                if 0 <= nr1 < 100 and 0 <= nr2 < 100:
                    if arr[nr1][c] == arr[nr2][c]:
                        length += 2
                    else:
                        break
            if max_length < length:
                max_length = length

    print(f'#{case} {max_length}')

