T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    # 피자의 번호 리스트
    num = list(range(1, M + 1))

    hwa = []
    # 처음에 화덕의 크기만큼 피자에서 꺼내 화덕으로 돌린다.
    for i in range(N):
        p = num.pop(0)
        hwa.append(p)

    # 피자 리스트에서 피자가 없어질 때까지 반복
    while len(num) > 0:
        # 화덕에서 치즈가 녹아 0이 되어 피자가 하나 줄 때까지 피자를 돌린다.
        while True:
            c = hwa.pop(0)
            pizza[c - 1] = pizza[c - 1] // 2
            # 만약 (피자의 치즈) // 2가 0보다 크면 뒤에 넣어서 계속 돌리고 0이면 깨버린다.
            if pizza[c - 1] > 0:
                hwa.append(c)
            else:
                break

        # 피자가 아직 있으면 피자를 화덕으로 다시 추가
        if len(num) > 0:
            p = num.pop(0)
            hwa.append(p)

    # 피자들이 모두 화덕에 들어왔으므로 마지막 하나가 남을 때까지 반복
    while len(hwa) > 1:
        c = hwa.pop(0)
        pizza[c - 1] = pizza[c - 1] // 2
        # 만약 (피자의 치즈) // 2가 0보다 크면 뒤에 넣어서 계속 돌린다.
        if pizza[c - 1] > 0:
            hwa.append(c)

    print(f'#{case} {hwa[0]}')