T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 상하좌우를 표시할 좌표
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    # 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 최대 꽃가루는
    max_pang = 0
    # 배열을 돌면서 델타탐색으로 꽃가루를 터트린다.
    for r in range(N):
        for c in range(M):
            # 상하좌우와 가운데 꽃가루의 합은 처음에는 가운데 풍선의 꽃가루로 둔다.
            sum_pang = arr[r][c]
            # 새로운 r과 c를 만들어 상하좌우를 돌게 한다.
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                # 새로운 r과 c는 배열의 범위인 N과 M을 벗어나면 안되므로
                if 0 <= nr < N and 0 <= nc < M:
                    sum_pang += arr[nr][nc]
            
            # 최대 꽃가루보다 꽃가루가 더 크면 최대 꽃가루 갱신
            if max_pang < sum_pang:
                max_pang = sum_pang
    
    print(f'#{case} {max_pang}')
        