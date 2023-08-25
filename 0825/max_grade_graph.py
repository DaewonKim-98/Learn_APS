T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 내림차순으로 정렬
    arr.sort(reverse=True)
    # K개의 과목을 잘라 narr에 추가
    narr = arr[:K]

    print(f'#{case} {sum(narr)}')
