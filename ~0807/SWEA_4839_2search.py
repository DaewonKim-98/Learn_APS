T = int(input())

for case in range(1, T + 1):
    P, A, B = map(int, input().split())

    start = 1
    end = P

    # A 에 대해서 이진 탐색을 하고 탐색을 실행할 때마다 count를 올린다.
    A_count = 0
    while start <= end:
        middle = int((start + end) / 2)
        if middle == A:
            A_count += 1
            break
        elif middle > A:
            end = middle
            A_count += 1
        else:
            start = middle
            A_count += 1

    # B 에 대해서 이진 탐색을 하고 탐색을 실행할 때마다 count를 올린다.
    start = 1
    end = P
    B_count = 0
    while start <= end:
        middle = int((start + end) / 2)
        if middle == B:
            B_count += 1
            break
        elif middle > B:
            end = middle
            B_count += 1
        else:
            start = middle
            B_count += 1

    # 먼저 페이지를 펼치는 사람이 이기므로 작은 사람이 이긴다.
    if A_count < B_count:
        print(f'#{case} A')
    elif A_count > B_count:
        print(f'#{case} B')
    else:
        print(f'#{case} {0}')