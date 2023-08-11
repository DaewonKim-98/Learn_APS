T = int(input())

for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 단조 리스트
    danlist = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            # 곱을 만들고
            mul = arr[i] * arr[j]
            # 곱이 단조인지 확인
            dan = True
            for k in range(len(str(mul)) - 1):
                # 만약 곱에서 앞의 수가 뒤에 수보다 크면 False
                if str(mul)[k] > str(mul)[k + 1]:
                    dan = False
                    break
            # 하나라도 앞의 수가 큰게 없으면 True로 들어오므로 단조
            if dan == True:
                danlist.append(mul)

    # 단조 중에서 최댓값 출력
    if danlist:
        print(f'#{case} {max(danlist)}')
    else:
        print(f'#{case} {-1}')