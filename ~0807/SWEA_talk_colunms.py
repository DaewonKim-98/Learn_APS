T = int(input())

for case in range(1, T + 1):
    arr = []

    for i in range(5):
        row = list(str(input()))
        # 15 자리로 row 를 채운 후 배열을 만든다.
        if len(row) < 15:
            while len(row) < 15:
                row += ['.']

        arr += [row]

    # 세로로 읽은 순서대로 글자는
    read = ''
    # 세로로 읽어야 하므로 열 우선 순회
    for c in range(15):
        for r in range(5):
            # . 이면 무시
            if arr[r][c] != '.':
                read += arr[r][c]

    print(f'#{case} {read}')