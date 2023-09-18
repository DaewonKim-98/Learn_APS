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
    dp[3] = min(dp[2] + min(arr[3] * d, m), t)

