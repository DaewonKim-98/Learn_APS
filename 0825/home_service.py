T = int(input())

# 운영 영역의 크기가 K 일 때 방범 서비스 영역 범위
def prevent(K):
    # dir
    dir = [[0, 0]]
    for i in range(1, K):
        dir.append([0, i])
        dir.append([0, -i])
        dir.append([i, 0])
        dir.append([-i, 0])
        for j in range(1, i):
            dir.append([j, i - j])
            dir.append([-j, i - j])
            dir.append([j, -(i - j)])
            dir.append([-j, -(i - j)])

    return dir

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열을 돌리면서 운영 영역과 서비스를 받는 집들의 수 관계 파악
    max_house = 0
    for r in range(N):
        for c in range(N):
            # 운영영역 K의 최대는 N
            for K in range(1, N + 2):
                # 서비스 영역 안의 집의 수 / 서비스 영역의 크기
                house = 0
                service = K * K + (K - 1) * (K - 1)
                # 운영영역에 대해 서비스 영역을 델타탐색 서비스 영역 크기 + 1
                dir = prevent(K)
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < N and 0 <= nc < N:
                        # 델타 탐색을 했을 때 집의 수
                        if arr[nr][nc] == 1:
                            house += 1

                # 이익은 집을 얻는 수익 - 전체 서비스 영역
                benefit = house * M - service
                # 이익이 0을 넘었을 때 최대 house 갱신
                if benefit >= 0:
                    if max_house < house:
                        max_house = house

    print(f'#{case} {max_house}')
