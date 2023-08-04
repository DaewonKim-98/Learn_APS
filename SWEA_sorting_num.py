T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N, 0, -1):
        for j in range(1, i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

    print(f'#{case}', end=' ')
    for k in arr:
        print(k, end=' ')
    print()