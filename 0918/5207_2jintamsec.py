import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 이진 탐색
def binary(l, r, i):
    global select_right
    global select_left
    global result
    m = (l + r) // 2
    # 양쪽 번갈아 하는게 실패거나 위치에 도달했으면 종료
    if i == N_list[m]:
        return
    elif i > N_list[m]:
        # 오른쪽을 선택했는데 또 연속으로 오른쪽을 선택한다면 안되므로
        if select_right == True:
            result = False
            return
        # 연속해서 오지 않았으면 오른쪽 선택을 했다하고 왼쪽 선택 지우기
        else:
            select_right = True
            select_left = False
            binary(m + 1, r, i)
    else:
        # 왼쪽 선택도 마찬가지
        if select_left == True:
            result = False
            return
        # 연속해서 오지 않았으면 왼쪽 선택을 했다하고 오른쪽 선택 지우기
        else:
            select_right = False
            select_left = True
            binary(l, m - 1, i)
    if result == False:
        return

T = int(input().strip())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))
    N_list = sorted(N_list)
    # 시작과 끝, 가운데
    l = 0
    r = N - 1

    # M 리스트에서 N 리스트에 없는 것이면 패스
    cnt = 0
    for i in M_list:
        if i not in N_list:
            pass
        else:
            # 오른쪽 선택
            select_right = False
            # 왼쪽 선택
            select_left = False
            # 양쪽 번갈아서 하는게 맞는 경우
            result = True
            binary(l, r, i)
            if result == True:
                cnt += 1

    print(f'#{case} {cnt}')
