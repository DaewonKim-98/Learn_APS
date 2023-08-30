T = int(input())

# 상하좌우 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 방 이동 함수
def move(r, c, cnt):
    for d in dir:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
            cnt += 1
            move(nr, nc, cnt)

    room.append(cnt)

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방 번호와 방 이동 횟수
    room_list = []
    # 배열을 돌면서 방 이동 값
    for r in range(N):
        for c in range(N):
            cnt = 1
            room = [arr[r][c]]
            move(r, c, cnt)
            room_list.append(room)

    # 방 리스트를 방 번호에 대해 오름차순으로 정렬
    room_list.sort(key=lambda x: x[0])

    # 방 횟수가 최대인 방 인덱스
    max_move_idx = 0
    for i in range(N * N):
        if room_list[max_move_idx][1] < room_list[i][1]:
            max_move_idx = i

    print(f'#{case} {room_list[max_move_idx][0]} {room_list[max_move_idx][1]}')