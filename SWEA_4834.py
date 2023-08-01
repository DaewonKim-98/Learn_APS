T = int(input())

for case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input()))

    # 가장 많은 카드의 숫자를 셀 max_num 와 장수를 셀 max_cnt 를 둔다.
    max_cnt = 0
    max_num = num_list[0]
    for num in range(N):
        # 자신과 똑같은 카드가 오면 장수를 셀 cnt 를 둔다.
        cnt = 0
        for nnum in range(N):
            # 만약 num 인덱스의 카드와 nnum 인덱스의 카드가 같으면 cnt 에 1을 추가한다.
            if num_list[num] == num_list[nnum]:
                cnt += 1
        # 가장 많은 카드의 숫자를 갱신하는데 뒤에까지 생각해주기 위해 <=을 해준다.
        if max_cnt <= cnt:
            max_cnt = cnt
            # max_cnt 가 갱신 될때마다 카드의 최댓값을 갱신해주어 가장 큰 값이 남도록 한다.
            if max_num < num_list[num]:
                max_num = num_list[num]

    print(f'#{case} {max_num} {max_cnt}')