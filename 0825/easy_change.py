T = int(input())

moeny_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for case in range(1, T + 1):
    N = int(input())

    result = []

    for moeny in moeny_list:
        # 돈으로 나눈 몫을 m
        m = N // moeny
        # 결과에 추가한 뒤
        result.append(m)
        # N을 나머지로 갱신
        N %= moeny

    print(f'#{case}')
    print(*result)