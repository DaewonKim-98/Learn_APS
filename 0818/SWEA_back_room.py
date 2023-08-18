T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))

    room_list = [0] * 401
    # 구간이 최대로 겹친만큼 최소 단위가 만들어진다. 4변겹치면4 / 최대 2개 겹치면 2
    # 따라서 방봐 방 사이의 범위에 맞는 room_list의 인덱스의 값에 +1 해줘서 중복을 찾는다.
    for lst in arr:
        lst.sort()
        if lst[0] % 2 == 0:
            lst[0] -= 1
        if lst[1] % 2 == 1:
            lst[1] += 1
        for room in range(lst[0], lst[1] + 1):
            room_list[room] += 1
    m = 0
    for room in room_list:
        if m < room:
            m = room


    print(f'#{case} {m}')