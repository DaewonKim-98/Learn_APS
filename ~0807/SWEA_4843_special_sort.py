T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, N - 1, 2):
        minIdx = i
        # 최솟값은 홀수번째, 대신 앞에서 한 것과 인덱스가 같은 부분은 건너뛰기
        k = list(range(1, i + 1, 2))
        for j in range(0, N):
            if j not in k:
                if arr[minIdx] > arr[j]:
                    minIdx = j
        arr[minIdx], arr[i] = arr[i], arr[minIdx]

    for i in range(0, N - 1, 2):
        maxIdx = i
        # 최댓값은 짝수번째, 대신 앞에서 한 것과 인덱스가 같은 부분은 건너뛰기
        k = list(range(0, i + 1, 2))
        for j in range(0, N):
            if j not in k:
                if arr[maxIdx] < arr[j]:
                    maxIdx = j
        arr[maxIdx], arr[i] = arr[i], arr[maxIdx]

    print(f'#{case}', end=' ')
    # 10 개까지 출력
    for i in range(10):
        print(arr[i], end=' ')
    print()