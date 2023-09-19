import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    d, m, t, y = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    # dp로 풀기
    dp = [0] * 13
    dp[1] = min(arr[1] * d, m)
    dp[2] = dp[1] + min(arr[2] * d, m)
    dp[3] = min(dp[2] + min(arr[3] * d, m),
                t)

    # 11월 까지
    for i in range(4, 12):
        dp[i] = min(dp[i - 3] + t,
                    dp[i - 1] + min(arr[i] * d, m))

    # 12월
    dp[12] = min(dp[9] + t,
                 dp[10] + t,
                 dp[11] + min(arr[12] * d, m),
                 y)

    print(f'#{case} {dp[12]}')



