T = int(input())

for t in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 낙차 최댓값을 max_down으로 둔다.
    max_down = 0
    for box_index in range(N):
        # 각 인덱스에 대해 낙차 값을 new_down로 두고 자기보다 작은 값들을 count로 둔다.
        new_down = 0
        cnt = 0
        for nbox_index in range(box_index, N):
            # 만약 자기보다 작은 값들이 자신 이후에 있다면 count에 1을 더해준다.
            if boxes[box_index] <= boxes[nbox_index]:
                cnt += 1
        # 낙차 값은 자신의 위치에서 자신보다 작은 값들을 뺀 값이므로 이렇게 계산된다.
        new_down = N - box_index - cnt
        # 낙차 최댓값과 비교해 더 크면 그 값이 최댓값
        if max_down < new_down:
            max_down = new_down

    print(f'#{t} {max_down}')
