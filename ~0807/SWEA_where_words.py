T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        arr += [list(map(int, input().split()))]

    # 연속된 흰 부분의 개수를 리스트 안에 넣을 수 있게 cnt_list를 둔다.
    cnt_list = []
    # 가로에 대해서 단어를 넣을 곳 찾기
    for r in range(N):
        # 흰색, 1의 개수를 셀 cnt 를 둔다.
        cnt = 0
        for c in range(N):
            # 흰색 부분이면 cnt 에 1 추가
            if arr[r][c] == 1:
                cnt += 1
            # 흑색이 나오면 연속된 흰 부분들을 cnt_list 에 추가하고 cnt = 0
            else:
                cnt_list += [cnt]
                cnt = 0
            # 마지막에 닿으면 cnt_list 에 추가
            if c == N - 1:
                cnt_list += [cnt]

    # 세로에 대해서 단어를 넣을 곳 찾기
    for c in range(N):
        # 흰색, 1의 개수를 셀 cnt 를 둔다.
        cnt = 0
        for r in range(N):
            # 흰색 부분이면 cnt 에 1 추가
            if arr[r][c] == 1:
                cnt += 1
            # 흑색이 나오면 연속된 흰 부분들을 cnt_list 에 추가하고 cnt = 0
            else:
                cnt_list += [cnt]
                cnt = 0
            # 마지막에 닿으면 cnt_list 에 추가
            if r == N - 1:
                cnt_list += [cnt]

    result = 0
    # cnt_list 에서 K를 찾으면 단어를 넣을 수 있는 칸들을 찾는 것
    for length in cnt_list:
        if length == K:
            result += 1

    print(f'#{case} {result}')