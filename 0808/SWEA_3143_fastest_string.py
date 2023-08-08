T = int(input())

for case in range(1, T + 1):
    A, B = map(str, input().split())

    len_A = 0
    for i in A:
        len_A += 1

    len_B = 0
    for i in B:
        len_B += 1

    # 중복되는 B의 개수를 세준다.
    cnt = 0
    i = 0
    # i는 끝까지 돌고 대신 똑같은 것이 나오면 B를 건너 뛰어 다음부터 계산
    while i <len_A - len_B + 1:
        if A[i:i + len_B] == B:
            cnt += 1
            i += len_B
        else:
            i += 1

    # 결과는 A의 글자 개수에서 (B - 1) * cnt 를 해준 값과 같다.
    result = len_A - (len_B - 1) * cnt
    print(f'#{case} {result}')