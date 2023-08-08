T = int(input())

for case in range(1, T + 1):
    string = list(input())

    # 거꾸로 돌리고 각 문자들을 반대 문자에 맞게 바꾸어준다.
    new_str = ''
    for i in range(len(string) - 1, -1, -1):
        if string[i] == 'b':
            new_str += 'd'
        elif string[i] == 'd':
            new_str += 'b'
        elif string[i] == 'q':
            new_str += 'p'
        elif string[i] == 'p':
            new_str += 'q'

    print(f'#{case} {new_str}')