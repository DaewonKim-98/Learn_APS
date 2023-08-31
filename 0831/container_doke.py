T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    arr.sort(key=lambda x: x[0])

    # i가 0이 될 때까지 반복하며 모든 경우의 수를 계산 - 뒤에서부터 세는게 더 효율적
    i = N - 1
    cnt_list = []
    while i >= 0:
        cnt = 1
        last = arr[i][0]
        for j in range(i, -1, -1):
            # 끝 시간이 뒤의 작업 시작시간보다 크면 안되므로
            if last >= arr[j][1]:
                cnt += 1
                # 끝시간 갱신
                last = arr[j][0]

        # 한바퀴를 다 돌면 i와 cnt_list 갱신
        cnt_list.append(cnt)
        i -= 1

    # 가장 많은 작업 횟수
    print(f'#{case} {max(cnt_list)}')