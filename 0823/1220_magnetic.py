T = 10

for case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 교착상태
    result = 0
    # 열에서 일어나는 일이므로 열 우선 탐색
    for c in range(N):
        # 각 열에 대해 N극인 자성체가 처음 나타났을 때 그 아래 N과 S 순서 리스트화
        c_list = []
        for r in range(N):
            # N극인 자성체가 있을 때 그 밑에 있는 것들을 리스트화
            if arr[r][c] == 1:
                for i in range(r, N):
                    if arr[i][c] == 1:
                        c_list.append(1)
                    elif arr[i][c] == 2:
                        c_list.append(2)
                break
        # c_list에서 마지막 S 이후의 N들은 모두 테이블에서 사라지므로 2가 뒤에서 나오기
        # 전까지 뒤에 1들을 모두 삭제
        for c in range(len(c_list)):
            if c_list[-1] == 1:
                c_list.pop()
            else:
                break
        # 나머지 자석들은 모두 교착상태인데 교착상태의 개수는 교착 지점의 개수이므로
        mix = 0
        for i in range(len(c_list) - 1):
            if c_list[i] == 1 and c_list[i + 1] == 2:
                mix += 1
        result += mix
    print(f'#{case} {result}')





