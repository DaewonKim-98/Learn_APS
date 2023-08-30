T = int(input())

# 고객의 좌표들을 모두 순열로 돌린 다음에 각 순열들에 대해서 거리를 모두 구하고 비교
def permutaiton(i, N):
    # 순열이 완성되면
    if i == N:
        # 처음 거리는 회사와 첫 번째 고객의 집
        distance = abs(lst[0] - p[0][0]) + abs(lst[1] - p[0][1])
        for i in range(N - 1):
            # 거리는 양 옆의 고객의 집 사이의 거리의 합
            distance += abs(p[i][0] - p[i + 1][0]) + abs(p[i][1] - p[i + 1][1])
        # 마지막 고객과 집까지의 거리도 마지막으로 추가
        distance += abs(lst[2] - p[-1][0]) + abs(lst[3] - p[-1][1])
        distance_list.append(distance)
    # 순열 만들기
    else:
        for j in range(N):
            # 사용하지 않았으면
            if used[j] == 0:
                p[i] = arr[j]
                used[j] = 1
                permutaiton(i + 1, N)
                used[j] = 0

for case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    # 순열로 만들기 위해 좌표들을 모두 리스트화
    arr = []
    for i in range(2, N + 2):
        arr.append([lst[i * 2], lst[i * 2 + 1]])

    # 순열을 이용해 구할 수 있는 모든 경우의 거리 구하기
    p = [[]] * N
    used = [0] * N

    distance_list = []
    i = 0
    permutaiton(i, N)

    print(f'#{case} {min(distance_list)}')
