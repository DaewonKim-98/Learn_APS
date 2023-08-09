T = int(input())

# 파스칼 삼각형 함수
def paskar(N):
    if N == 1:
        result = [1]
    elif N == 2:
        result = [1, 1]
    else:
        # 재귀함수로 이전 파스칼을 불러온다.
        lst = paskar(N - 1)
        # 처음은 1로 두고 시작
        result = [1]
        # 이전 파스칼에서 연속된 두 수 합이 아래 파스칼
        for i in range(N -2):
            result.append(lst[i] + lst[i + 1])

        # 마지막에 1 추가
        result.append(1)

    return result

for case in range(1, T + 1):
    N = int(input())

    print(f'#{case}')
    for i in range(1, N + 1):
        # 리스트이므로 숫자열로 변환해서 출력
        for j in paskar(i):
            print(j, end=' ')
        print()


