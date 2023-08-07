T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())

    arr = []
    for i in range(N):
        arr += [list(input())]
    # 회문의 총 개수를 result
    result = ''
    # 행 우선 탐색
    for r in range(N):
        for c in range(N - M + 1):
            read = True
            # M 에서 2를 나눈 몫만큼 반복을 돌렸을 때 서로 반대편이 하나라도 다르면 False
            for m in range(M // 2):
                if arr[r][c + m] != arr[r][c + M - 1 - m]:
                    read = False
            # read 가 True 면 반대편이 모두 같다는 것이므로
            if read == True:
                for j in range(M):
                    result += arr[r][c + j]

    # 열 우선 탐색
    for c in range(N):
        for r in range(N - M + 1):
            read = True
            # M 에서 2를 나눈 몫만큼 반복을 돌렸을 때 서로 반대편이 하나라도 다르면 False
            for m in range(M // 2):
                if arr[r + m][c] != arr[r + M - 1 - m][c]:
                    read = False
            # read 가 True 면 반대편이 모두 같다는 것이므로
            if read == True:
                for j in range(M):
                    result += arr[r + j][c]

    print(f'#{case} {result}')