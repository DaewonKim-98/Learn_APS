import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    heights = []
    for i in range(1 << N):
        bubunziphap = []
        for j in range(N):
            if i & (1 << j):
                bubunziphap.append(arr[j])
        if sum(bubunziphap) >= B:
            heights.append(sum(bubunziphap))

    # 최솟값과 높이의 차
    print(f'#{case} {min(heights) - B}')


