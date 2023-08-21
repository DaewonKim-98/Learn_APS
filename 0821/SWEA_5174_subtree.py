T = int(input())

def preorder(N):
    global cnt
    if N:
        cnt += 1
        preorder(ch1[N])
        preorder(ch2[N])
    return cnt

for case in range(1, T + 1):
    E, N = map(int, input().split())
    e_list = list(map(int, input().split()))

    # 부모 인덱스에 대한 자식 노드
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for e in range(E):
        p, c = e_list[e * 2], e_list[e * 2 + 1]
        # 아직 자식 번호가 안들어갔으면
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    print(f'#{case} {preorder(N)}')