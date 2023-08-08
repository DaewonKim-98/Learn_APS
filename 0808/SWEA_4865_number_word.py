T = int(input())

for case in range(1, T + 1):
    # 중복 제거
    str1 = set(list(input()))
    str2 = list(input())

    # 글자의 최대 수를 출력
    max_cnt = 0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s2 == s1:
               cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{case} {max_cnt}')

