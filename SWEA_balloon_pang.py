T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr += [list(map(int, input().split()))]

    # 가운데와 상하좌우를 포함한 델타 리스트를 만든다.
    d_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 꽃가루의 합을 max_value 로 둔다.
    max_value = 0
    for r in range(N):
        for c in range(M):
            # 처음의 합을 선택한 풍선의 꽃가루 갯수로 둔다.
            sum_value = arr[r][c]
            for dr, dc in d_list:
                # 선택한 풍선의 꽃가루 갯수 만큼 상하좌우가 추가로 터지니까 그 값만큼 곱한 값을 모두 더해준다.
                for j in range(1, arr[r][c] + 1):
                    nr, nc = r + dr * j, c + dc * j
                    # 범위가 배열을 넘어가면 안되므로 이 사이에 있는 것들만 합을 구한다.
                    if 0 <= nr < N and 0 <= nc < M:
                        sum_value += arr[nr][nc]
            # 최댓값 갱신
            if max_value < sum_value:
                max_value = sum_value

    print(f'#{case} {max_value}')