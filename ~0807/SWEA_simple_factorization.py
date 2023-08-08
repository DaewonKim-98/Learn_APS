T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = []
    # 모든 abcde를 돌려 찾는다.
    for a in range(25):
        for b in range(20):
            for c in range(15):
                for d in range(15):
                    for e in range(8):
                        if 2 ** a * 3 ** b * 5 ** c * 7 ** d * 11 ** e == N:
                            arr += [a, b, c, d, e]
    print(f'#{case}', end=' ')
    for i in arr:
        print(i, end=' ')
    print()