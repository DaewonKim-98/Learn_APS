T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    result = 0
    for i in range(12):
        if i % 2 == 0:
            player1[arr[i]] += 1
        else:
            player2[arr[i]] += 1

        for p1 in player1:
            if p1 >= 3:
                result = 1
        for p2 in player2:
            if p2 >= 3:
                result = 2
        for p1 in range(8):
            if 0 < player1[p1] and 0 < player1[p1 + 1] and 0 < player1[p1 + 2]:
                result = 1
        for p2 in range(8):
            if 0 < player2[p2] and 0 < player2[p2 + 1] and 0 < player2[p2 + 2]:
                result = 2

        if result != 0:
            break

    print(f'#{case} {result}')
