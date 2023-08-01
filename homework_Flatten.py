for case in range(1, 11):
    N = int(input())
    box_list = list(map(int, input().split()))

    #
    for dump in range(N):
        # 최고와 최저 인덱스를 둔다.
        max_idx = 0
        min_idx = 0

        # 전체를 돌면서 최고와 최저 인덱스를 갱신한다.
        for num in range(100):
            if box_list[max_idx] < box_list[num]:
                max_idx = num
            if box_list[min_idx] > box_list[num]:
                min_idx = num

        # 최고값에서 최저값으로 박스 하나를 준다.
        box_list[max_idx] -= 1
        box_list[min_idx] += 1

        # 만약 박스가 1개보다 작으면 break
        if box_list[max_idx] - box_list[min_idx] <= 1:
            break
        else:
            pass

    # 마지막으로 찾은 값들은 바뀐 것들이므로 최고 인덱스와 최저 인덱스를 다시 찾아 그 값들의 차를 계산해준다.
    for num in range(100):
        if box_list[max_idx] < box_list[num]:
            max_idx = num
        if box_list[min_idx] > box_list[num]:
            min_idx = num

    result = box_list[max_idx] - box_list[min_idx]
    print(f'#{case} {result}')