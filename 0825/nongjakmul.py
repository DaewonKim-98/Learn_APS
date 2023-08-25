T = int(input())

# 농장 탐색
def harvest(middle):
    sum = arr[middle][middle]
    for i in range(1, middle + 1):
        sum += arr[middle][middle + i]
        sum += arr[middle][middle - i]
        sum += arr[middle + i][middle]
        sum += arr[middle - i][middle]
        for j in range(1, i):
            sum += arr[middle + j][middle + i - j]
            sum += arr[middle - j][middle + i - j]
            sum += arr[middle + j][middle - (i - j)]
            sum += arr[middle - j][middle - (i - j)]

    return sum

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 가운데부터 시작
    middle = N // 2

    print(f'#{case} {harvest(middle)}')
