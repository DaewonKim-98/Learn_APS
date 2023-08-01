T = int(input())
for case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    # 최대 최소의 인덱스
    min_idx = 0
    max_idx = 0

    for num in range(N):
        # 다음 인덱스의 값들이 더 작으면 min_idx를 갱신(가장 왼쪽의 인덱스가 나옴)
        if num_list[min_idx] > num_list[num]:
            min_idx = num
        # 다음 인덱스의 값들이 더 크면 max_idx 갱신(가장 오른쪽의 인덱스가 나옴)
        if num_list[max_idx] <= num_list[num]:
            max_idx = num

    if max_idx >= min_idx:
        result = max_idx - min_idx
    else:
        result = min_idx - max_idx

    print(f'#{case} {result}')
