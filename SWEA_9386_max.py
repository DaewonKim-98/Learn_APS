T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    # 1의 숫자를 세는 cnt와 cnt 중에서 최댓값을 찾는 max_cnt를 둔다.
    max_cnt = 0
    cnt = 1
    for num in range(1, N):
        # 1부터 인덱스를 시작해 자신과 자신 전의 값이 모두 1일 때(연속) cnt에 1을 더한다.
        if (arr[num] == 1) & arr[num - 1]:
            cnt += 1
        # 아니면 다시 cnt를 1로 둔다.
        else:
            cnt = 1
        # max_cnt 가 cnt 보다 작으면 max_cnt를 cnt로 갱신
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{case} {max_cnt}')
