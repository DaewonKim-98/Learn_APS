T = int(input())

for case in range(1, T + 1):
    N = int(input())
    # A 와 B 를 넣어 줄 ab_list 를 만든다.
    ab_list = []
    for n in range(N):
        A, B = map(int, input().split())
        ab_list += [(A, B)]
    P = int(input())
    # 버스 정류장의 좌표인 C 리스트를 만들어 준다
    c_list = []
    for c in range(P):
        C = int(input())
        c_list += [C]

    # 정류장을 지나는 버스 노선의 개수를 표시할 cnt_list 를 만든다.
    cnt_list = [0] * 5001
    # cnt_list 의 인덱스에서 A 와 B 사이의 수들에 1 씩 더해주면
    for A, B in ab_list:
        for cnt in range(A, B + 1):
            cnt_list[cnt] += 1

    print(f'#{case}', end=' ')
    # 버스 정류장의 좌표가 인덱스인 cnt_list 를 출력
    for i in c_list:
        print(cnt_list[i], end=' ')
    print()