T = int(input())


# 순열 구하는 함수
def f(i, N, idx):
    global min_s
    if i == N:
        # 순열이 정해졌으므로 각 행과 순열의 열에서의 숫자의 합을 구한다.
        s = 0
        for r in range(N):
            s += arr[r][idx[r]]
            if min_s <= s:
                break
        # 최솟값 갱신
        if min_s > s:
            min_s = s
    else:
        for j in range(i, N):  # 자신부터 오른쪽 끝까지
            idx[i], idx[j] = idx[j], idx[i]
            f(i + 1, N, idx)
            idx[i], idx[j] = idx[j], idx[i]

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 각 행에 대한 인덱스 순열 - 같은 열이면 안되기 때문에
    idx = list(range(N))
    # 최소 합
    min_s = 9 * N
    f(0, N, idx)

    print(f'#{case} {min_s}')