T = 10

for case in range(1, T + 1):
    A, B = map(str, input().split())
    A = int(A)
    B = list(B)

    # 양 옆이 같은게 없을 때까지 반복을 돌린다.
    while True:
        # 양 옆이 같은 것들이 없다
        not_same = True
        i = 0
        # i + 1 > A - 1 이면 인덱스를 넘어가므로 반복문 조건
        while i + 1 <= A - 1:
            # 양 옆이 같은 것들을 찾아서 제거
            if B[i] == B[i + 1]:
                # i 인덱스에 해당하는 것을 제거하고 또 인덱스가 줄어드므로 같이 제거
                B.pop(i)
                B.pop(i)
                # 인덱스 2개가 제거되었으므로 A - 2
                A -= 2
                # 같은 것이 있으므로
                not_same = False
            else:
                # 같은 것들이 없으면 i를 늘리면서 탐색
                i += 1
        # 양 옆에 같은 것들이 없는게 그대로 출력되면 종료
        if not_same == True:
            break

    result = ''.join(B)
    print(f'#{case} {result}')