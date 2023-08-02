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
