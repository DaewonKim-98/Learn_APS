T = int(input())

for case in range(1, T + 1):
    arr = list(str(input()))

    # 겹치는 쇠 파이프의 개수를 cnt
    cnt = 0
    # 잘린 쇠 파이프의 개수를 cnt_cut
    cnt_cut = 0
    for i in range(0, len(arr) - 1):
        # 만약 레이져에 도달한다면 지금까지 센 cnt 를 더한다.
        if arr[i] == '(' and arr[i + 1] == ')':
            cnt_cut += cnt
        # 파이프의 개수에 '(' 면 레이저 도달 전까지 계속 추가
        elif arr[i] == '(' and arr[i + 1] != ')':
            cnt += 1
        if i > 0:
            # 파이프가 끝나면 cnt_cut 잘린 쇠 파이프에 1 추가, 파이프 개수 1 감소
            if arr[i - 1] != '(' and arr[i] == ')':
                cnt_cut += 1
                cnt -= 1

    # 마지막은 안바줬으므로 마지막에 1 추가
    if arr[-2] != '(' and arr[-1] == ')':
        cnt_cut += 1

    print(f'#{case} {cnt_cut}')