T = int(input())

for case in range(1, T + 1):
    str1 = list(map(str, input()))
    str2 = list(map(str, input()))

    # 최댓값을 max_str 로 두고 만약 같은게 있으면 cnt 를 추가해주고 max_str 갱신
    max_str = 0
    for i in str1:
        cnt = 0
        for j in str2:
            if j == i:
                cnt += 1
        if max_str < cnt:
            max_str = cnt

    print(f'#{case} {max_str}')