# 행열 탐색 연습

# 0 으로 초기화 된 N * M 의 2차원 배열 생성하기
from pprint import pprint as pp
m = 5
n = 5

arr = []
for i in range(n):
    row = [0] * m
    arr.append(row)

# 행 우선 순회를 다른 것보다 우선시 하여 학습하자!

num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 행 우선 순회
for r in range(len(num_list)):
    for c in range(len(num_list)):
        print(num_list[r][c])

# 열 우선 순회
for c in range(len(num_list)):
    for r in range(len(num_list)):
        print(num_list[r][c])


# 역-행 우선 순회
for r in range(len(num_list)):
    for c in range(len(num_list) - 1, -1, -1):
        print(num_list[r][c])

# 역-열 우선 순회
for r in range(len(num_list) -1, -1, -1):
    for c in range(len(num_list)):
        print(num_list[r][c])

# 가장자리의 합

def edge_sum(arr):
    # 순회를 하면서, 2차원 리스트의 가장자리에 있는 원소들을 합한다.
    edge_sum_result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # 가장자리 확인
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr) - 1:
                print(arr[i][j])
                edge_sum_result += arr[i][j]
    return edge_sum_result

result = edge_sum(num_list)
print(result)


# 델타 탐색
# 문제에 제시된 제약 조건에 따라 탐색 순서는 달라질 수 있다.

# 상 하 좌 우
d_row = [1, 0, -1, 0]
d_col = [0, 1, 0, -1]

# 대각선
dxy = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

# 벽을 세워야 한다.
# 주어진 2차원 리스트의 범위를 벗어나지 않도록 제한을 두는 행위

# 1. 벽의 제한을 두는데, 벽을 넘어가는 경우, 아무것도 하지 않는다.
# 2. 벽을 넘어가지 않는 경우에만 기능을 수행한다.

x = 0
y = 1
for d in range(4)
    # 다음에 이용할 좌표 담기
    nx = x + dx[d]
    ny = y + dy[d]

    # 1. map 을 벗어나는 경우 아무것도 하지 않기
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        continue
    # 특정 로직 수행

    # 2. map을 넘어가지 않는 경우에만 기능을 수행하기
    if 0 <= nx < N and 0 <= ny < N:
        # 특정 로직 수행

def isSafeArea(nx, ny, N):
    if 0 <= nx < N and 0 <= ny < N:
        return True
    else:
        return False