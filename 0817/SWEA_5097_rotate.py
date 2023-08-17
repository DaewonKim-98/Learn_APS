T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 맨 앞의 숫자를 맨 뒤로
    for i in range(M):
        p = arr.pop(0)
        arr.append(p)

    # 맨 앞에 있는 수 출력
    print(f'#{case} {arr[0]}')