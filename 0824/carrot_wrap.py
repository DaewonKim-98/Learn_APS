T = int(input())

for case in range(1, T + 1):
    N = int(input())
    carrot_size = list(map(int, input().split()))

    # 당근의 크기를 인덱스로 하는 리스트를 만들어 개수를 카운트한다.
    size_idx = [0] * 31
    for carrot in carrot_size:
        size_idx[carrot] += 1

    # 0개가 아닌 개수별로 리스트를 만든다.
    count_list = []
    for size in size_idx:
        if size != 0:
            count_list.append(size)


    # 개수의 최댓값이 N // 2를 넘어가거나 개수가 2개 이하면 포장할 수 없다.
    if (max(count_list) > (N // 2)) or (len(count_list) < 3):
        print(f'#{case} {-1}')
    # 슬라이싱을 통해 합을 구하고 각 합들에서 최댓값과 최솟값의 차를 구한 뒤 그 차들의 최소 출력
    else:
        length = len(count_list)
        min_sub = 30
        for i in range(1, length - 1):
            for j in range(2, length):
                # 구간마다의 당근 개수의 합
                a = sum(count_list[:i])
                b = sum(count_list[i:j])
                c = sum(count_list[j:])
                # 당근의 개수 차이
                sub = max([abs(a - b), abs(b - c), abs(c - a)])
                # 차이의 최솟값 갱신
                if min_sub > sub:
                    min_sub = sub
        print(f'#{case} {min_sub}')
