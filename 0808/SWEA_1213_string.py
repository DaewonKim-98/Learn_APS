T = 10

for case in range(1, T + 1):
    N = int(input())
    str1 = input()
    str2 = input()

    len_1 = 0
    for i in str1:
        len_1 += 1

    len_2 = 0
    for i in str2:
        len_2 += 1

    # 인덱스를 처음부터 찾아서 len_1 길이만큼의 문자열이 str1 과 같으면 cnt + 1
    cnt = 0
    for i in range(len_2 - len_1 + 1):
        if str2[i:i + len_1] == str1:
            cnt += 1

    print(f'#{case} {cnt}')