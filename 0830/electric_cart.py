T = int(input())

# 순열 만들기
def permutation(i, N):
    if i == N - 1:
        # 배터리 계산
        battery = 0
        # 처음 시작은 1부터 시작
        battery += arr[1][p[0]]

        for l in range(0, N - 2):
            battery += arr[p[l]][p[l + 1]]

        # 마지막에 배터리는 처음으로 돌아가는 것도 추가해야 하므로
        battery += arr[p[-1]][1]

        battery_list.append(battery)
        return
    # 순열에 들어갈 숫자 결정
    else:
        for j in range(N - 1):
            # 사용되기 전이면
            if used[j] == 0:
                p[i] = nums[j]
                used[j] = 1
                permutation(i + 1, N)
                used[j] = 0


for case in range(1, T + 1):
    N = int(input())
    # 구역을 인덱스로 포현하기 위해 0을 배열 앞에 추가
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    # 이미 사용한 카드인지 표시
    # 1부터는 봐줄 필요 없으므로
    used = [0] * (N - 1)
    p = [0] * (N - 1)
    nums = list(range(2, N + 1))
    i = 0

    battery_list = []
    permutation(i, N)
    min_battery = min(battery_list)

    print(f'#{case} {min_battery}')