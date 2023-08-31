T = int(input())

for case in range(1, T + 1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    # 무거운 것부터 옮기는 것이 좋으므로 내림차순으로 정렬
    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    result = 0
    # 트럭을 돌면서 가장 무거운 것부터 옮기기
    for m in m_list:
        for n in n_list:
            if m >= n:
                result += n
                n_list.remove(n)
                break

    # 출력
    print(f'#{case} {result}')