T = int(input())

for case in range(1, T + 1):
    N = int(input())

    # 점의 개수를 셀 cnt를 둔다.
    cnt = 0
    # 사분면으로 원을 나누었을 때 어떤 x와 y에 대해 x^2 + y^2이 반지름 안에 있으면 되므로
    for x in range(-N, N + 1):
        for y in range(-N, N + 1):
            if x ** 2 + y ** 2 <= N ** 2:
                cnt += 1

    print(f'#{case} {cnt}')