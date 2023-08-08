T = int(input())

for case in range(1, T + 1):
    K, N, M= map(int, input().split()) # 최대 이동, 종점
    charging_list = list(map(int, input().split())) # 충전기가 설치된 정류장 번호

    # 충전 횟수와 버스의 이동 칸들을 0으로 둔다.
    charging = 0
    bus = 0
    # 버스가 종점에 도착하기 직전까지 버스를 계속 움직인다.
    while bus < N - K:
        # 버스가 최대로 충전기까지 갈 수 있는 거리를 max_btop 로 둔다.
        max_btop = 0
        # 최대로 충전기까지 갈 수 있는 거리는 항상 버스가 최대로 갈 수 있는 거리보다 작아야 한다.
        for point in charging_list:
            if point - bus <= K:
                if max_btop < point - bus:
                    max_btop = point - bus
            else:
                break

        # max_btop 가 0이면 point - bus 가 K를 넘어간다는 뜻이므로 최대 이동을 넘어간다는 것이므로
        # 종점에 도착할 수 없으므로 charging 은 0
        if max_btop == 0:
            charging = 0
            break
        # 버스는 충전기까지 갈 수 있는 거리만큼 움직이고 충전 횟수를 1 늘려준다.
        bus = bus + max_btop
        charging += 1

    # 충전 횟수를 출력
    print(f'#{case} {charging}')